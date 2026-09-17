import json
from pathlib import Path
from .adapters.json_adapter import JsonAdapter
from .adapters.text_adapter import TextAdapter
from .adapters.spreadsheet_adapter import SpreadsheetAdapter
from .checks import run_check


def make_adapter(artifact_type: str, submission_path: str | Path):
    if artifact_type == "json":
        return JsonAdapter(submission_path)
    if artifact_type == "text":
        return TextAdapter(submission_path)
    if artifact_type == "spreadsheet":
        return SpreadsheetAdapter(submission_path, data_only=False)
    raise ValueError(f"Unsupported artifact_type: {artifact_type}")


def grade(manifest_path: str | Path, submission_path: str | Path) -> dict:
    manifest = json.loads(Path(manifest_path).read_text(encoding="utf-8"))
    adapter = make_adapter(manifest["artifact_type"], submission_path)
    results = [run_check(adapter, c) for c in manifest["checks"]]
    total_weight = sum(r.weight for r in results) or 1.0
    earned = sum(r.score for r in results)
    score = earned / total_weight
    threshold = float(manifest.get("pass_threshold", 1.0))
    return {
        "task_id": manifest.get("task_id"),
        "mode": manifest.get("mode"),
        "score": round(score, 6),
        "passed": score >= threshold,
        "pass_threshold": threshold,
        "checks": [r.to_dict() for r in results],
    }
