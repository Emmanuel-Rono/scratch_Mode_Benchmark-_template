import json
from pathlib import Path
from .base import ArtifactAdapter


class JsonAdapter(ArtifactAdapter):
    def __init__(self, path: str | Path):
        self.path = Path(path)
        self.data = json.loads(self.path.read_text(encoding="utf-8"))

    def get(self, selector: str):
        # Dot-path selector, e.g. metrics.total or items.0.name
        cur = self.data
        if selector in ("", "."):
            return cur
        for part in selector.split("."):
            if isinstance(cur, list):
                cur = cur[int(part)]
            else:
                cur = cur[part]
        return cur
