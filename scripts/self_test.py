#!/usr/bin/env python3
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def run(fixture, expect_pass):
    verifier = ROOT / "example" / "tests" / "verifier.py"
    submission = ROOT / "example" / "tests" / "fixtures" / fixture
    proc = subprocess.run([sys.executable, str(verifier), str(submission)], capture_output=True, text=True)
    if not proc.stdout.strip():
        raise RuntimeError(proc.stderr)
    result = json.loads(proc.stdout)
    actual = bool(result["passed"])
    if actual != expect_pass:
        raise AssertionError(f"{fixture}: expected pass={expect_pass}, got {actual}: {result}")
    print(f"OK  {fixture} -> score={result['score']} passed={actual}")

if __name__ == "__main__":
    run("good_submission.json", True)
    run("partial_submission.json", False)
    print("All scratch-mode demo checks passed.")
