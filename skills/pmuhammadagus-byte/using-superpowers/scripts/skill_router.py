#!/usr/bin/env python3
"""List available skills and match a user request to the best trigger.

Reads every skills/<name>/SKILL.md under a skills directory, parses the
'description' trigger, and ranks matches against a free-text request using
simple keyword overlap. Safe: read-only, no network, no writes.

Usage:
  python3 skill_router.py --skills /path/to/skills --request "write a plan for X"
  python3 skill_router.py --request "create a new skill"   # defaults to cwd/skills
"""
import argparse
import os
import re
import sys

TRIGGER_RE = re.compile(r'^Use when', re.IGNORECASE)


def load_skills(skills_dir):
    skills = []
    if not os.path.isdir(skills_dir):
        return skills
    for name in sorted(os.listdir(skills_dir)):
        skill_md = os.path.join(skills_dir, name, "SKILL.md")
        if not os.path.isfile(skill_md):
            continue
        with open(skill_md, encoding="utf-8") as f:
            text = f.read()
        fm = {}
        if text.startswith("---"):
            end = text.find("\n---", 3)
            if end != -1:
                for line in text[3:end].strip("\n").splitlines():
                    if ":" in line:
                        k, _, v = line.partition(":")
                        fm[k.strip()] = v.strip().strip('"').strip("'")
        skills.append({
            "name": fm.get("name", name),
            "description": fm.get("description", ""),
        })
    return skills


def score(request, description):
    if not description:
        return 0
    req_tokens = set(re.findall(r"[a-z0-9]+", request.lower()))
    desc_tokens = set(re.findall(r"[a-z0-9]+", description.lower()))
    if not req_tokens:
        return 0
    overlap = req_tokens & desc_tokens
    return len(overlap) / len(req_tokens)


def main():
    p = argparse.ArgumentParser(description="Match a request to a skill trigger.")
    p.add_argument("--skills", default=None, help="Skills directory (default: ./skills)")
    p.add_argument("--request", default="", help="Free-text user request")
    args = p.parse_args()

    skills_dir = args.skills or os.path.join(os.getcwd(), "skills")
    skills = load_skills(skills_dir)
    if not skills:
        print(f"No skills found in {skills_dir}", file=sys.stderr)
        sys.exit(1)

    if not args.request:
        print("Available skills:")
        for s in skills:
            print(f"  - {s['name']}: {s['description']}")
        return

    ranked = sorted(
        skills,
        key=lambda s: score(args.request, s["description"]),
        reverse=True,
    )
    top = ranked[0]
    sc = score(args.request, top["description"])
    print(f"Best match: {top['name']} (score {sc:.2f})")
    print(f"  trigger: {top['description']}")
    if sc == 0:
        print("  (no token overlap — read SKILL.md and judge manually)")
    else:
        print("\nOther candidates:")
        for s in ranked[1:4]:
            sc2 = score(args.request, s["description"])
            if sc2 > 0:
                print(f"  - {s['name']} (score {sc2:.2f})")


if __name__ == "__main__":
    main()
