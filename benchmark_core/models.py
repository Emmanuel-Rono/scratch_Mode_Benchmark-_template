from dataclasses import dataclass, asdict
from typing import Any


@dataclass
class CheckResult:
    id: str
    passed: bool
    score: float
    weight: float
    message: str
    observed: Any = None
    expected: Any = None

    def to_dict(self):
        return asdict(self)
