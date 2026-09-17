import math
import re
from typing import Any
from .models import CheckResult


def run_check(adapter, spec: dict) -> CheckResult:
    cid = spec["id"]
    kind = spec["type"]
    weight = float(spec.get("weight", 1.0))
    selector = spec.get("selector", "")
    expected = spec.get("expected")

    try:
        if kind == "exists":
            passed = adapter.exists(selector)
            observed = passed
            msg = "selector exists" if passed else "selector missing"

        elif kind == "exact":
            observed = adapter.get(selector)
            passed = observed == expected
            msg = "exact match" if passed else "exact value mismatch"

        elif kind == "numeric_tolerance":
            observed = float(adapter.get(selector))
            expected_f = float(expected)
            abs_tol = float(spec.get("abs_tolerance", 0.0))
            rel_tol = float(spec.get("rel_tolerance", 0.0))
            passed = math.isclose(observed, expected_f, abs_tol=abs_tol, rel_tol=rel_tol)
            msg = f"within tolerance" if passed else f"outside tolerance (abs={abs_tol}, rel={rel_tol})"

        elif kind == "nonempty":
            observed = adapter.get(selector)
            passed = observed is not None and str(observed).strip() != ""
            msg = "non-empty" if passed else "empty"

        elif kind == "contains":
            observed = str(adapter.get(selector))
            passed = str(expected) in observed
            msg = "contains required text" if passed else "required text missing"

        elif kind == "regex":
            observed = str(adapter.get(selector))
            passed = re.search(str(expected), observed) is not None
            msg = "regex matched" if passed else "regex did not match"

        elif kind == "formula_present":
            observed = adapter.get(selector)
            passed = isinstance(observed, str) and observed.startswith("=")
            msg = "formula present" if passed else "formula missing or hard-coded"

        elif kind == "formula_contains_refs":
            observed = adapter.get(selector)
            refs = spec.get("references", [])
            passed = isinstance(observed, str) and observed.startswith("=") and all(r in observed for r in refs)
            msg = "required references present" if passed else "required formula references missing"
            expected = refs

        elif kind == "number_format":
            observed = adapter.number_format(selector)
            passed = observed == expected
            msg = "number format matched" if passed else "number format mismatch"

        else:
            raise ValueError(f"Unknown check type: {kind}")

    except Exception as exc:
        return CheckResult(cid, False, 0.0, weight, f"check error: {exc}", None, expected)

    return CheckResult(cid, passed, weight if passed else 0.0, weight, msg, observed, expected)
