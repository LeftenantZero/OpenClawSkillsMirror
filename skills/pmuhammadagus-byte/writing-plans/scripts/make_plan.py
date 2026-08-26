#!/usr/bin/env python3
"""
make_plan.py — scaffold a SHARP plan and score its accuracy.

Enforces the writing-plans SHARP rule:
  S  single testable goal
  H  every step Has an acceptance check (observable)
  A  every step has a verification command/method
  R  Realistic ordering / dependencies declared
  P  Points of risk named

Usage:
  python3 make_plan.py --title "Add OAuth" \
    --goal "User can log in via Google so returning users skip signup" \
    --step "add schema" --acceptance "users table has oauth_provider column" \
      --verify "sqlite3 app.db '.schema users'" \
    --step "callback handler" --acceptance "GET /oauth/callback creates a session" \
      --verify "curl -i localhost:8000/oauth/callback | grep 200" \
    --out memory/plan-oauth.md

Exit code: 0 if score >= 80 (plan is sharp enough), 2 if below (revise first).
No network, no destructive ops.
"""
import argparse
import os
import re
import sys

VAGUE = [
    r"\bimprove\b", r"\bbetter\b", r"\brobust\b", r"\bfaster\b", r"\bcleaner\b",
    r"\boptimize\b", r"\buser-friendly\b", r"\bsecure\b", r"\bgood\b", r"\bworks\b",
    r"\bfix\b.*\bissue\b",
]


def sharpness(goal, steps):
    score = 100
    notes = []

    # S — goal testable?
    if not goal or len(goal.split()) < 4:
        score -= 20
        notes.append("Goal too short / not testable (S)")
    for v in VAGUE:
        if re.search(v, goal or "", re.I):
            score -= 10
            notes.append(f"Goal uses vague word '{v.strip()}' without a metric (S)")
            break

    if not steps:
        score -= 40
        notes.append("No steps defined (H/A)")
        return max(score, 0), notes

    # H + A — per step
    for i, s in enumerate(steps, 1):
        if not s.get("acceptance") or len(s["acceptance"].split()) < 3:
            score -= 12
            notes.append(f"Step {i}: acceptance missing/unclear (H)")
        else:
            for v in VAGUE:
                if re.search(v, s["acceptance"], re.I):
                    score -= 6
                    notes.append(f"Step {i}: acceptance vague '{v.strip()}' (H)")
                    break
        if not s.get("verify"):
            score -= 12
            notes.append(f"Step {i}: no verify command (A)")
        else:
            if re.search(r"TODO|tbd|<.*>|manual", s["verify"], re.I):
                score -= 6
                notes.append(f"Step {i}: verify is a placeholder (A)")

    # R — dependencies declared on every step after the first
    for i, s in enumerate(steps[1:], 2):
        if s.get("depends") is None:
            score -= 4
            notes.append(f"Step {i}: dependency not declared (R)")

    return max(score, 0), notes


def build_table(steps):
    rows = []
    for i, s in enumerate(steps, 1):
        rows.append(
            f"| {i} | {s['step']} | {s.get('acceptance') or '—'} | "
            f"{s.get('verify') or '—'} | {s.get('depends') or '—'} |"
        )
    return "\n".join(rows)


def main():
    p = argparse.ArgumentParser(description="Scaffold + score a SHARP plan.")
    p.add_argument("--title", required=True)
    p.add_argument("--goal", default="", help="One testable sentence (S)")
    p.add_argument("--step", action="append", default=[], help="Step text (repeatable)")
    p.add_argument("--acceptance", action="append", default=[], help="Acceptance per step (repeatable)")
    p.add_argument("--verify", action="append", default=[], help="Verify command per step (repeatable)")
    p.add_argument("--depends", action="append", default=[], help="Depends-on per step (repeatable)")
    p.add_argument("--risk", action="append", default=[], help="Risk / open question (repeatable)")
    p.add_argument("--out", default=None, help="Output path (default: stdout)")
    args = p.parse_args()

    n = len(args.step)
    if not n:
        args.step = ["<step description>"]
        n = 1
    acc = (args.acceptance + [""] * n)[:n]
    ver = (args.verify + [""] * n)[:n]
    dep = (args.depends + [None] * n)[:n]

    steps = [
        {"step": args.step[i], "acceptance": acc[i], "verify": ver[i], "depends": dep[i]}
        for i in range(n)
    ]

    score, notes = sharpness(args.goal, steps)

    content = f"""# Plan: {args.title}
## Goal (testable)
{args.goal or '<one testable sentence — observable outcome>'}

## Steps (verification matrix)
| # | Step | Acceptance (observable) | Verify (command/method) | Depends |
|---|------|------------------------|-------------------------|---------|
{build_table(steps)}

## Risks / open questions
{chr(10).join('- ' + r for r in args.risk) if args.risk else '- ...'}

## Integration
- branch/PR strategy, cleanup, rollback note

<!-- sharpness score: {score}/100 -->
"""
    if args.out:
        out_dir = os.path.dirname(os.path.abspath(args.out))
        os.makedirs(out_dir, exist_ok=True)
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Wrote plan to {args.out}", file=sys.stderr)

    print(content)
    print(f"[sharpness] score = {score}/100", file=sys.stderr)
    for nt in notes:
        print(f"  - {nt}", file=sys.stderr)
    if score < 80:
        print("[sharpness] BELOW 80 — revise plan before executing.", file=sys.stderr)
        sys.exit(2)
    print("[sharpness] OK — plan is sharp enough to execute.", file=sys.stderr)


if __name__ == "__main__":
    main()
