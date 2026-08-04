from __future__ import annotations

import re
from typing import Any

CRITERIA = (
    "PVS1",
    "PS1",
    "PS2",
    "PS3",
    "PS4",
    "PM1",
    "PM2",
    "PM3",
    "PM4",
    "PM5",
    "PM6",
    "PP1",
    "PP2",
    "PP3",
    "PP4",
    "PP5",
    "BA1",
    "BS1",
    "BS2",
    "BS3",
    "BS4",
    "BP1",
    "BP2",
    "BP3",
    "BP4",
    "BP5",
    "BP6",
    "BP7",
)
STRENGTHS = ("Very Strong", "Strong", "Moderate", "Supporting", "Stand-alone")


def normalize_criterion(value: Any) -> tuple[str | None, str | None, str | None]:
    """Return normalized criterion, strength, and original text."""
    raw = str(value or "").strip()
    upper = raw.upper().replace("_", "-")
    criterion = next(
        (code for code in CRITERIA if re.search(rf"(?<![A-Z0-9]){code}(?![A-Z0-9])", upper)),
        None,
    )
    if not criterion:
        return None, None, raw or None
    strength = None
    for label in STRENGTHS:
        compact = label.replace("-", "")
        if re.search(
            rf"(?i)(?<![A-Za-z]){re.escape(label)}(?![A-Za-z])", raw
        ) or compact.lower() in raw.lower().replace(" ", "").replace("_", ""):
            strength = label
            break
    return criterion, strength, raw or None


def direction(criterion: str) -> str:
    return "benign" if criterion.startswith(("BA", "BS", "BP")) else "pathogenic"


def is_not_applicable(text: str) -> bool:
    return bool(
        re.search(
            r"(?i)\b(?:not applicable|do not use|should not be applied|not recommended|not used|cannot be applied)\b",
            text,
        )
    )


def text_of(value: Any) -> str:
    if isinstance(value, str):
        return value.strip()
    if isinstance(value, (int, float, bool)):
        return str(value)
    if isinstance(value, dict):
        return " ".join(
            text_of(value[key])
            for key in ("description", "text", "summary", "label", "value")
            if key in value
        )
    if isinstance(value, list):
        return " ".join(text_of(item) for item in value)
    return ""

