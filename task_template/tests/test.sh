#!/usr/bin/env sh
set -eu
python tests/verifier.py "${1:-/output/submission.<ext>}"
