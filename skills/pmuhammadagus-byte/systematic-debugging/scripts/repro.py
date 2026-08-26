#!/usr/bin/env python3
"""Capture a reproducible run as evidence for systematic debugging.

Supports the Reproduce and Verify steps: run a command (e.g. a test, a script,
a reproduction case), capture exit code + stdout/stderr, and emit a structured
report you can paste into your debugging notes.

Safe: runs ONLY the command you pass (no extra mutations). Intended for
reproduction/verification, not for destructive commands.
"""
import argparse
import json
import subprocess
import sys
from datetime import datetime


def main():
    p = argparse.ArgumentParser(description="Run a reproduction command and capture evidence.")
    p.add_argument("command", nargs=argparse.REMAINDER,
                   help="The command to run for reproduction, e.g. pytest tests/test_x.py::test_y")
    p.add_argument("--label", default="repro", help="Short label for the report")
    p.add_argument("--json", dest="as_json", action="store_true",
                   help="Emit JSON instead of human-readable text")
    args = p.parse_args()

    if not args.command:
        p.error("provide a command to run, e.g. repro.py -- pytest -q")

    try:
        proc = subprocess.run(args.command, capture_output=True, text=True)
    except FileNotFoundError as e:
        sys.exit(f"Command not found: {e}")

    report = {
        "label": args.label,
        "command": " ".join(args.command),
        "exit_code": proc.returncode,
        "passed": proc.returncode == 0,
        "stdout": proc.stdout,
        "stderr": proc.stderr,
        "timestamp": datetime.now().isoformat(timespec="seconds"),
    }

    if args.as_json:
        print(json.dumps(report, indent=2))
    else:
        status = "PASS" if report["passed"] else "FAIL"
        print(f"[{status}] {report['label']} (exit {report['exit_code']})")
        print(f"  command: {report['command']}")
        print(f"  at:      {report['timestamp']}")
        if proc.stdout.strip():
            print("  --- stdout ---")
            print(proc.stdout.rstrip())
        if proc.stderr.strip():
            print("  --- stderr ---")
            print(proc.stderr.rstrip())
        print("Evidence captured. Compare against the expected behavior to confirm reproduction.")


if __name__ == "__main__":
    main()
