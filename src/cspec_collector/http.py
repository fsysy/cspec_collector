from __future__ import annotations

import json
import logging
import random
import time
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, Self

import httpx
import truststore

LOG = logging.getLogger(__name__)


@dataclass
class FetchResult:
    body: bytes
    status_code: int
    headers: dict[str, str]
    fetched_at: str


class CSpecClient:
    def __init__(
        self,
        base_url: str = "https://cspec.genome.network",
        timeout: float = 60,
        max_retries: int = 5,
        min_interval: float = 0.5,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.max_retries = max_retries
        self.min_interval = min_interval
        self._last_request = 0.0
        self.client = httpx.Client(
            timeout=timeout,
            follow_redirects=True,
            verify=truststore.SSLContext(),
            headers={
                "Accept": "application/json",
                "User-Agent": "cspec-collector/0.1 (+https://github.com/fsysy/cspec_collector)",
            },
        )

    def close(self) -> None:
        self.client.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(self, *_: object) -> None:
        self.close()

    def get(
        self,
        path: str,
        params: dict[str, Any] | None = None,
        conditional: dict[str, str] | None = None,
    ) -> FetchResult:
        headers = conditional or {}
        last_error: Exception | None = None
        for attempt in range(self.max_retries):
            delay = self.min_interval - (time.monotonic() - self._last_request)
            if delay > 0:
                time.sleep(delay)
            try:
                response = self.client.get(f"{self.base_url}{path}", params=params, headers=headers)
                self._last_request = time.monotonic()
                if response.status_code == 304:
                    return FetchResult(b"", 304, dict(response.headers), _now())
                response.raise_for_status()
                content_type = response.headers.get("content-type", "").lower()
                if "json" not in content_type:
                    raise ValueError(
                        f"Expected JSON but received {content_type or 'unknown content type'}"
                    )
                json.loads(response.content)
                return FetchResult(
                    response.content, response.status_code, dict(response.headers), _now()
                )
            except (httpx.HTTPError, ValueError, json.JSONDecodeError) as exc:
                last_error = exc
                if attempt + 1 == self.max_retries:
                    break
                wait = min(30.0, (2**attempt) + random.random())
                LOG.warning("Request failed (%s); retrying in %.1fs", exc, wait)
                time.sleep(wait)
        assert last_error is not None
        raise last_error


def _now() -> str:
    return datetime.now(UTC).isoformat()


def atomic_write(path: Path, body: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_bytes(body)
    temporary.replace(path)
