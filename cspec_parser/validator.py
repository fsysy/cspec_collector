from __future__ import annotations

from collections import Counter
from typing import Any

from .models import RuleRecord
from .normalizer import CRITERIA, direction


def validate_rule(rule: RuleRecord, gene_symbols: set[str]) -> list[dict[str, Any]]:
    errors = []
    if rule.criterion not in CRITERIA:
        errors.append({"code": "INVALID_CRITERION", "message": rule.criterion})
    if rule.direction != direction(rule.criterion):
        errors.append({"code": "DIRECTION_MISMATCH", "message": rule.criterion})
    if rule.gene and rule.gene not in gene_symbols:
        errors.append({"code": "UNKNOWN_GENE", "message": rule.gene})
    if not rule.source_path:
        errors.append({"code": "MISSING_SOURCE_PATH", "message": rule.rule_id})
    for threshold in rule.thresholds:
        if not isinstance(threshold.get("value"), (int, float)):
            errors.append({"code": "INVALID_THRESHOLD_VALUE", "message": rule.rule_id})
    if rule.applicable is False and not rule.rule_text:
        errors.append({"code": "INAPPLICABLE_WITHOUT_TEXT", "message": rule.rule_id})
    return errors


def duplicate_ids(rules: list[RuleRecord]) -> list[str]:
    counts = Counter(rule.rule_id for rule in rules)
    return [key for key, value in counts.items() if value > 1]

