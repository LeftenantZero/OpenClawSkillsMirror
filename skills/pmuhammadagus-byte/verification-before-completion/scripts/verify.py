#!/usr/bin/env python3
"""Run a configurable verification suite and capture evidence before claiming done.
No shell is spawned: commands run as argv lists (shlex.split), avoiding injection.

Supports every step of verification-before-completion: runs the commands you
declare, records exit codes + output, and writes an evidence log so you can state
WHAT you verified and HOW (not from memory).

Config file `verify.json` format:
{
  "commands": [
    {"name": "unit tests", "run": "pytest -q"},
    {"name": "lint",       "run": "ruff check ."},
    {"name": "type check", "run": "mypy src"}
  ]
}
"""
import argparse
import json
import subprocess
import sys
from datetime import datetime


def main():
    p = argparse.ArgumentParser(description="Run verification commands and record evidence.")
    p.add_argument("-c", "--config", default="verify.json",
                   help="JSON config listing commands (default: verify.json)")
    p.add_argument("-o", "--evidence", default="verification-evidence.json",
                   help="Where to write the evidence log")
    args = p.parse_args()

    try:
        with open(args.config) as fh:
            cfg = json.load(fh)
    except (OSError, json.JSONDecodeError) as e:
        sys.exit(f"Could not read config '{args.config}': {e}")

    commands = cfg.get("commands", [])
    if not commands:
        sys.exit("No commands defined in config.")

    results = []
    overall = True
    print(f"Running {len(commands)} verification command(s)...\n")
    for cmd in commands:
        name = cmd.get("name", cmd.get("run"))
        print(f"== {name} ==  $ {cmd['run']}")
        import shlex
        argv = shlex.split(cmd["run"])
        proc = subprocess.run(argv, capture_output=True, text=True)
        ok = proc.returncode == 0
        overall = overall and ok
        if proc.stdout.strip():
            print(proc.stdout.rstrip())
        if proc.stderr.strip():
            print(proc.stderr.rstrip())
        print(f"   -> {'PASS' if ok else 'FAIL'} (exit {proc.returncode})\n")
        results.append({
            "name": name, "run": cmd["run"], "exit_code": proc.returncode,
            "passed": ok, "stdout": proc.stdout, "stderr": proc.stderr,
        })

    evidence = {
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "overall_passed": overall,
        "results": results,
    }
    with open(args.evidence, "w") as fh:
        json.dump(evidence, fh, indent=2)

    verdict = "VERIFIED" if overall else "NOT VERIFIED"
    print(f"{verdict}. Evidence written to {args.evidence}.")
    print("Only claim completion if overall_passed is true; otherwise fix and re-run.")
    sys.exit(0 if overall else 1)


if __name__ == "__main__":
    main()
