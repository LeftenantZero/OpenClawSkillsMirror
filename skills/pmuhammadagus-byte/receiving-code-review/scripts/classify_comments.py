#!/usr/bin/env python3
"""Classify code-review comments and flag unverified claims.

Supports the "Read fully first" and "Verify technically" steps. Reads review
comments (JSON) and buckets them into must-fix / nit / discussion, and flags any
substantive comment that does not reference a file:line (so you know which claims
still need verifying against the code).

Comments format:
[
  {"id": 1, "body": "This will cause a memory leak in handler.py:42",
   "type": "must-fix"},
  {"id": 2, "body": "Maybe rename this variable", "type": "nit"}
]
"""
import argparse
import json
import re
import sys

REF_RE = re.compile(r"[\w./-]+\.py:\d+|[\w./-]+\.\w+:\d+|\.py\b")


def main():
    p = argparse.ArgumentParser(description="Classify review comments and flag unverified claims.")
    p.add_argument("comments", help="Path to a JSON list of review comments")
    args = p.parse_args()

    try:
        with open(args.comments) as fh:
            comments = json.load(fh)
    except (OSError, json.JSONDecodeError) as e:
        sys.exit(f"Could not read comments: {e}")

    buckets = {"must-fix": [], "nit": [], "discussion": []}
    needs_verify = []
    for c in comments:
        ctype = c.get("type", "discussion")
        buckets.setdefault(ctype, []).append(c)
        # A substantive comment (not a nit) should reference evidence.
        if ctype != "nit" and not REF_RE.search(c.get("body", "")):
            needs_verify.append(c)

    for label in ("must-fix", "nit", "discussion"):
        items = buckets[label]
        print(f"== {label} ({len(items)}) ==")
        for c in items:
            print(f"  #{c.get('id', '?')}: {c.get('body', '')[:80]}")
        print()

    if needs_verify:
        print("UNVERIFIED substantive claims (no file:line reference) — verify against code:")
        for c in needs_verify:
            print(f"  #{c.get('id', '?')}: {c.get('body', '')[:80]}")
    else:
        print("All substantive comments reference code locations. Good.")


if __name__ == "__main__":
    main()
