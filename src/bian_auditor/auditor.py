from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List

import yaml


BIAN_VERBS = [
    "activate",
    "capture",
    "control",
    "evaluate",
    "exchange",
    "execute",
    "initiate",
    "provide",
    "request",
    "retrieve",
    "update",
]


def audit_spec(path: str | Path) -> Dict[str, object]:
    spec = yaml.safe_load(Path(path).read_text(encoding="utf-8"))
    issues: List[str] = []
    score = 100

    operations = _operation_ids(spec)
    for operation_id in operations:
        if not any(operation_id.startswith(verb) for verb in BIAN_VERBS):
            issues.append(f"Operation '{operation_id}' does not start with a common BIAN verb.")
            score -= 10

    info = spec.get("info", {})
    if not any(key in info for key in ("x-domain", "x-bian-domain", "x-service-domain")):
        issues.append("No explicit domain hint found in info metadata.")
        score -= 15

    model_text = json.dumps(spec.get("components", {}).get("schemas", {})).lower()
    required_patterns = ("status", "reference", "record")
    missing = [pattern for pattern in required_patterns if pattern not in model_text]
    if missing:
        issues.append(f"Missing common BIAN data patterns: {', '.join(missing)}.")
        score -= 10

    score = max(score, 0)
    return {
        "compliant": score >= 70,
        "score": score,
        "issues": issues,
        "checked_operations": operations,
    }


def _operation_ids(spec: Dict) -> List[str]:
    ids: List[str] = []
    for methods in spec.get("paths", {}).values():
        for operation in methods.values():
            operation_id = operation.get("operationId")
            if operation_id:
                ids.append(operation_id)
    return ids
