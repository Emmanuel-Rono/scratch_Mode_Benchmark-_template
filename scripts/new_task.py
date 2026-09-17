#!/usr/bin/env python3
import argparse
import shutil
from pathlib import Path

MODE = "scratch"

def main():
    p = argparse.ArgumentParser(description="Scaffold a scratch-mode benchmark task")
    p.add_argument("--id", required=True)
    p.add_argument("--out", default="tasks")
    args = p.parse_args()

    repo = Path(__file__).resolve().parents[1]
    source = repo / "task_template"
    destination = Path(args.out) / args.id
    if destination.exists():
        raise SystemExit(f"Destination already exists: {destination}")
    shutil.copytree(source, destination)

    for path in destination.rglob("*"):
        if path.is_file() and path.suffix in {".md", ".toml", ".json", ".py", ".sh"}:
            text = path.read_text(encoding="utf-8")
            path.write_text(text.replace("__TASK_ID__", args.id), encoding="utf-8")

    print(f"Created {MODE}-mode task at {destination}")

if __name__ == "__main__":
    main()
