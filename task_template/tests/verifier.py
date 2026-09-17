#!/usr/bin/env python3
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from benchmark_core import grade

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: verifier.py /path/to/submission")
    manifest = Path(__file__).with_name("grading_manifest.json")
    print(json.dumps(grade(manifest, sys.argv[1]), indent=2))
