from __future__ import annotations

import re
from typing import Any

METRICS = {
    "af": "allele_frequency",
    "allele frequency": "allele_frequency",
    "popmax af": "popmax_af",
    "faf95": "faf95",
    "revel": "revel_score",
    "cadd": "cadd_score",
    "spliceai": "spliceai_score",
    "phylop": "phyloP_score",
    "lod": "lod_score",
    "odds ratio": "odds_ratio",
}
OPS = r"<=|>=|<|>|="


def extract_thresholds(text: str) -> list[dict[str, Any]]:
    result = []
    pattern = re.compile(
        rf"(?i)\b(af|allele frequency|popmax af|faf95|revel|cadd|spliceai|phylop|lod|odds ratio)\b\s*({OPS})\s*(-?\d+(?:\.\d+)?)\s*(%|percent)?"
    )
    for match in pattern.finditer(text):
        raw_value = float(match.group(3))
        unit = "fraction"
        if match.group(4):
            raw_value /= 100
            unit = "fraction"
        result.append(
            {
                "metric": METRICS[match.group(1).lower()],
                "operator": match.group(2),
                "value": raw_value,
                "unit": unit,
                "population": None,
                "dataset": None,
                "strength": None,
                "raw_text": match.group(0),
            }
        )
    return result

