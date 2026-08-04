from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def write_jsonl(path: Path, records: list[Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "".join(
            json.dumps(
                record.model_dump() if hasattr(record, "model_dump") else record, ensure_ascii=False
            )
            + "\n"
            for record in records
        ),
        encoding="utf-8",
    )


def write_report(path: Path, report: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

