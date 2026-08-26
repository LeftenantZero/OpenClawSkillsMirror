#!/usr/bin/env python3
"""Prepare a self-review summary + risk checklist before requesting review.

Supports the "Self-review first" and "Highlight risk areas" steps. Runs
read-only git commands to summarize what changed versus a base branch, then
prints a review-request template you can fill in. No mutations, no network.

Safe: only reads git state (diff/log/status). Never commits, pushes, or rewrites.
"""
import argparse
import subprocess
import sys


def git(*args):
    try:
        return subprocess.run(["git", *args], capture_output=True, text=True, check=True).stdout
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        sys.exit(f"git command failed: {e}")


def main():
    p = argparse.ArgumentParser(description="Generate a pre-review self-review summary.")
    p.add_argument("--base", default="main", help="Base branch to diff against (default: main)")
    args = p.parse_args()

    diff_stat = git("diff", "--stat", f"{args.base}...HEAD")
    commits = git("log", "--oneline", f"{args.base}...HEAD")
    status = git("status", "--short")

    changed = [ln for ln in diff_stat.splitlines() if ln.strip() and "|" in ln]
    risky_hints = ("migrat", "security", "concurrency", "lock", "thread", "auth", "permission")

    print("# Pre-Review Self-Check")
    print()
    print(f"Base branch: {args.base}")
    print(f"Commits since base: {len(commits.splitlines())}")
    print()
    print("## What changed")
    print(diff_stat.strip() or "(no diff stat)")
    print()
    print("## Recent commits")
    print(commits.strip() or "(none)")
    print()
    flagged = [c for c in changed if any(h in c.lower() for h in risky_hints)]
    print("## Risk areas to flag for reviewers")
    if flagged:
        for f in flagged:
            print(f"  - {f.strip()}")
    else:
        print("  (none auto-detected — manually flag anything subtle)")
    print()
    print("## Working tree")
    print(status.strip() or "(clean)")
    print()
    print("Reminder: run the suite, write a summary + rationale, name reviewers,")
    print("then request review. Do NOT merge on approval alone — verify once more.")


if __name__ == "__main__":
    main()
