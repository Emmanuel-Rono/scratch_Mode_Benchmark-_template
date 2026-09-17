#!/usr/bin/env python3
import argparse
from pathlib import Path

REQUIRED = [
    "instruction.md",
    "task.toml",
    "environment",
    "solution",
    "tests",
    "tests/verifier.py",
]


def main():
    p = argparse.ArgumentParser()
    p.add_argument("task_dir")
    args = p.parse_args()
    root = Path(args.task_dir)
    failures = []
    for item in REQUIRED:
        if not (root / item).exists():
            failures.append(item)
    if failures:
        print("INVALID TASK BUNDLE")
        for item in failures:
            print(f"  missing: {item}")
        raise SystemExit(1)
    print(f"VALID TASK BUNDLE: {root}")


if __name__ == "__main__":
    main()
