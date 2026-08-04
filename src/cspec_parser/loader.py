from __future__ import annotations

import json
from collections.abc import Iterator
from pathlib import Path
from typing import Any


def load_jsonl(path: Path) -> Iterator[tuple[int, dict[str, Any] | None, str | None]]:
    """Yield line number, parsed object, and error text without aborting the file."""
    with path.open(encoding="utf-8") as handle:
        for number, line in enumerate(handle, 1):
            if not line.strip():
                continue
            try:
                value = json.loads(line)
                yield number, value if isinstance(value, dict) else None, None
            except json.JSONDecodeError as exc:
                yield number, None, str(exc)

