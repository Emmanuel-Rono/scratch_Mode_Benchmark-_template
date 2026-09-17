from pathlib import Path
from .base import ArtifactAdapter


class TextAdapter(ArtifactAdapter):
    def __init__(self, path: str | Path):
        self.path = Path(path)
        self.text = self.path.read_text(encoding="utf-8")

    def get(self, selector: str):
        if selector in ("", ".", "text"):
            return self.text
        raise KeyError(f"Unsupported text selector: {selector}")
