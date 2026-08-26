#!/usr/bin/env python3
"""Scaffold a minimal pytest test file (the RED step of TDD).

Given a module and one or more function names, this generates a pytest test
skeleton where every test starts as a failing assertion (import/not-implemented)
so you begin in the RED state and write the implementation to turn it GREEN.

Safe: only writes a new test file (refuses to overwrite by default).
No network, no secrets, no destructive commands.
"""
import argparse
import os
import sys

TEMPLATE = '''\
import pytest

# Target module under test. Adjust the import to your project layout.
# from {module} import {first_func}


def test_{first_func}__returns_expected():
    """RED: this should fail until {first_func} is implemented."""
    # result = {first_func}(<inputs>)
    # assert result == <expected>
    pytest.fail("RED: implement {first_func} and uncomment the assertions above")


{extra_tests}'''

EXTRA = '''\
def test_{func}__returns_expected():
    """RED: this should fail until {func} is implemented."""
    # result = {func}(<inputs>)
    # assert result == <expected>
    pytest.fail("RED: implement {func} and uncomment the assertions above")
'''


def main():
    p = argparse.ArgumentParser(description="Scaffold a RED pytest test file.")
    p.add_argument("module", help="Module name under test, e.g. myapp.calc")
    p.add_argument("functions", nargs="+", help="Function names to scaffold tests for")
    p.add_argument("-o", "--output", default=None,
                   help="Output path (default: test_<module basename>.py)")
    p.add_argument("--overwrite", action="store_true",
                   help="Allow overwriting an existing file")
    args = p.parse_args()

    first = args.functions[0]
    extra = "".join(EXTRA.format(func=f) for f in args.functions[1:])
    content = TEMPLATE.format(module=args.module, first_func=first, extra_tests=extra)

    out = args.output or f"test_{args.module.split('.')[-1]}.py"
    if os.path.exists(out) and not args.overwrite:
        sys.exit(f"Refusing to overwrite existing file '{out}'. Use --overwrite or -o.")

    with open(out, "w") as fh:
        fh.write(content)
    print(f"Wrote RED test scaffold -> {out}")
    print("Next: run `pytest {0}` (should FAIL), then implement to go GREEN.".format(out))


if __name__ == "__main__":
    main()
