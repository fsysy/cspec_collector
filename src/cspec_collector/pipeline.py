from __future__ import annotations

import csv
import json
import logging
from collections import Counter, defaultdict
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from . import PARSER_VERSION
from .http import CSpecClient, atomic_write
from .models import CriterionRecord, DocumentRecord
from .parser import parse_criteria, parse_document

LOG = logging.getLogger(__name__)


def collect(
    root: Path, page_size: int = 25, resume: bool = False, force: bool = False, max_retries: int = 5
) -> None:
    raw_list = root / "data/raw/list"
    raw_docs = root / "data/raw/documents"
    reports = root / "reports"
    for directory in (raw_list, raw_docs, reports):
        directory.mkdir(parents=True, exist_ok=True)
    manifest = _load_json(reports / "manifest.json", {"documents": {}, "pages": {}})
    failures = reports / "failures.jsonl"
    all_entries: dict[str, dict[str, Any]] = {}
    page = 1
    with CSpecClient(max_retries=max_retries) as client:
        while True:
            target = raw_list / f"page_{page:04d}.json"
            payload: dict[str, Any]
            if resume and target.exists() and not force:
                payload = _load_json(target, {})
            else:
                effective = page_size
                while True:
                    try:
                        result = client.get(
                            "/cspec/SequenceVariantInterpretation/id",
                            {"pg": page, "pgSize": effective, "detail": "high"},
                        )
                        atomic_write(target, result.body)
                        payload = json.loads(result.body)
                        manifest["pages"][str(page)] = {
                            "status": result.status_code,
                            "fetched_at": result.fetched_at,
                            "page_size": effective,
                        }
                        break
                    except Exception:
                        if effective > 10:
                            effective = 10
                        elif effective > 5:
                            effective = 5
                        else:
                            raise
            items = payload.get("data", []) if isinstance(payload, dict) else []
            if not isinstance(items, list) or not items:
                break
            for item in items:
                if isinstance(item, dict) and item.get("entId"):
                    all_entries[str(item["entId"])] = item
            LOG.info("Collected list page %d (%d records)", page, len(items))
            if len(items) < manifest.get("pages", {}).get(str(page), {}).get(
                "page_size", page_size
            ):
                break
            page += 1
        for cspec_id, raw in sorted(all_entries.items()):
            target = raw_docs / f"{cspec_id}.json"
            previous = manifest.get("documents", {}).get(cspec_id, {})
            conditional = {}
            if not force:
                if previous.get("etag"):
                    conditional["If-None-Match"] = previous["etag"]
                if previous.get("last_modified"):
                    conditional["If-Modified-Since"] = previous["last_modified"]
            if resume and target.exists() and not force and not conditional:
                continue
            try:
                result = client.get(
                    f"/cspec/api/SequenceVariantInterpretation/id/{cspec_id}",
                    conditional=conditional,
                )
                if result.status_code != 304:
                    atomic_write(target, result.body)
                manifest["documents"][cspec_id] = {
                    "status": result.status_code,
                    "fetched_at": result.fetched_at,
                    "etag": result.headers.get("etag"),
                    "last_modified": result.headers.get("last-modified"),
                }
            except Exception as exc:
                _append_jsonl(failures, {"cspec_id": cspec_id, "error": str(exc), "at": _now()})
                LOG.error("Failed to fetch %s: %s", cspec_id, exc)
    _write_json(reports / "manifest.json", manifest)


def normalize(root: Path) -> tuple[list[DocumentRecord], list[CriterionRecord]]:
    pages = sorted((root / "data/raw/list").glob("page_*.json"))
    raw_by_id: dict[str, dict[str, Any]] = {}
    for page in pages:
        for item in _load_json(page, {}).get("data", []):
            if isinstance(item, dict) and item.get("entId"):
                raw_by_id[str(item["entId"])] = item
    manifest = _load_json(root / "reports/manifest.json", {})
    documents: list[DocumentRecord] = []
    criteria: list[CriterionRecord] = []
    for cspec_id, raw in sorted(raw_by_id.items()):
        path = root / "data/raw/documents" / f"{cspec_id}.json"
        if not path.exists():
            continue
        body = path.read_bytes()
        detail = json.loads(body)
        fetched = manifest.get("documents", {}).get(cspec_id, {}).get("fetched_at", _now())
        doc = parse_document(raw, detail, body, fetched)
        documents.append(doc)
        criteria.extend(parse_criteria(doc, detail))
    out = root / "data/normalized"
    out.mkdir(parents=True, exist_ok=True)
    _write_jsonl(
        out / "cspec_documents.jsonl",
        [d.model_dump() for d in documents if d.document_status == "current_released"],
    )
    _write_jsonl(out / "cspec_all_versions.jsonl", [d.model_dump() for d in documents])
    current_ids = {d.cspec_id for d in documents if d.document_status == "current_released"}
    current_criteria = _dedupe_models([c for c in criteria if c.cspec_id in current_ids])
    _write_jsonl(out / "cspec_criteria.jsonl", [c.model_dump() for c in current_criteria])
    _write_gene_index(out / "cspec_gene_index.csv", documents)
    return documents, current_criteria


def validate(root: Path) -> bool:
    docs = [
        DocumentRecord.model_validate(x)
        for x in _read_jsonl(root / "data/normalized/cspec_all_versions.jsonl")
    ]
    criteria = [
        CriterionRecord.model_validate(x)
        for x in _read_jsonl(root / "data/normalized/cspec_criteria.jsonl")
    ]
    current = [d for d in docs if d.document_status == "current_released"]
    warnings: list[str] = []
    errors: list[str] = []
    for d in current:
        if not d.genes:
            warnings.append(
                f"{d.cspec_id}: current document has no gene; source value preserved without inference"
            )
    for c in criteria:
        if not (c.criterion_code or c.criterion_label):
            errors.append(f"{c.cspec_id}: criterion has no code or label")
    duplicates = _duplicates(
        (c.gene_symbol, c.cspec_id, c.ruleset_id, c.criterion_code, c.strength) for c in criteria
    )
    if duplicates:
        errors.append(f"Duplicate criterion records: {len(duplicates)}")
    by_gene: dict[str, list[str]] = defaultdict(list)
    for d in current:
        for gene in d.genes:
            if gene.get("symbol"):
                by_gene[str(gene["symbol"])].append(d.cspec_id)
    collisions = {k: v for k, v in by_gene.items() if len(set(v)) > 1}
    if collisions:
        warnings.append(f"Genes with multiple current released documents: {collisions}")
    missing_details = sum(
        1 for d in docs if not (root / "data/raw/documents" / f"{d.cspec_id}.json").exists()
    )
    zero_criteria = [
        d.cspec_id for d in current if not any(c.cspec_id == d.cspec_id for c in criteria)
    ]
    if zero_criteria:
        warnings.append(f"Current documents with zero criteria: {zero_criteria}")
    failure_count = len(_read_jsonl(root / "reports/failures.jsonl"))
    ambiguous = [d.cspec_id for d in docs if d.document_status == "ambiguous"]
    if ambiguous:
        warnings.append(f"Ambiguous documents: {ambiguous}")
    counts = Counter(d.document_status for d in docs)
    report = [
        "# CSpec validation report",
        "",
        f"Generated: {_now()}",
        "",
        "## Summary",
        "",
        f"- Total list records: {len(docs)}",
        f"- Current released documents: {len(current)}",
        f"- Legacy or superseded documents: {counts['legacy_replaced'] + counts['superseded']}",
        f"- Unique genes: {len(by_gene)}",
        f"- Criterion records: {len(criteria)}",
        f"- Failed HTTP requests: {failure_count}",
        f"- Ambiguous documents: {len(ambiguous)}",
        f"- Duplicate or colliding genes: {len(collisions)}",
        f"- Missing detail documents: {missing_details}",
        "",
        "## Errors",
        "",
    ]
    report += [f"- {x}" for x in errors] or ["- None"]
    report += ["", "## Warnings", ""] + ([f"- {x}" for x in warnings] or ["- None"])
    (root / "reports").mkdir(parents=True, exist_ok=True)
    (root / "reports/validation_report.md").write_text("\n".join(report) + "\n", encoding="utf-8")
    return not errors


def build_kb(root: Path, max_files: int = 10) -> list[Path]:
    docs = [
        DocumentRecord.model_validate(x)
        for x in _read_jsonl(root / "data/normalized/cspec_documents.jsonl")
    ]
    criteria = [
        CriterionRecord.model_validate(x)
        for x in _read_jsonl(root / "data/normalized/cspec_criteria.jsonl")
    ]
    kb = root / "kb"
    kb.mkdir(parents=True, exist_ok=True)
    generated = _now()
    by_gene: dict[str, list[DocumentRecord]] = defaultdict(list)
    for d in docs:
        for gene in d.genes:
            if gene.get("symbol"):
                by_gene[str(gene["symbol"])].append(d)
    index = [
        "# ClinGen CSpec gene index",
        "",
        f"Generated: {generated}",
        f"Parser: {PARSER_VERSION}",
        "",
    ]
    for gene in sorted(by_gene):
        index.append(
            f"- **{gene}**: "
            + "; ".join(
                f"{d.cspec_id} v{d.version or '?'} ({d.document_status}, {d.vcep or 'unknown VCEP'})"
                for d in by_gene[gene]
            )
        )
    index_path = kb / "cspec_gene_index.md"
    index_path.write_text("\n".join(index) + "\n", encoding="utf-8")
    chunks: list[list[str]] = [[]]
    per_file = max(1, (len(by_gene) + max_files - 1) // max_files)
    for i, gene in enumerate(sorted(by_gene)):
        if i and i % per_file == 0:
            chunks.append([])
        lines = chunks[-1]
        lines += [f"# {gene}", ""]
        for d in by_gene[gene]:
            lines += [
                f"Document: {d.title or d.cspec_id}",
                f"CSpec ID: {d.cspec_id}",
                f"VCEP: {d.vcep or ''}",
                f"Version: {d.version or ''}",
                f"Status: {d.document_status}",
                f"Diseases: {_display(d.diseases)}",
                f"Modes of inheritance: {_display(d.modes_of_inheritance)}",
                f"Fetched: {d.fetched_at}",
                f"Source API: {d.source_api_url}",
                "",
            ]
            related = [c for c in criteria if c.cspec_id == d.cspec_id and c.gene_symbol == gene]
            for c in sorted(related, key=lambda x: (x.criterion_code or "", x.strength or "")):
                lines += [
                    f"## {c.criterion_code or c.criterion_label or 'Criterion'} — {c.strength or 'unspecified strength'}",
                    "",
                    c.criterion_description or "",
                    "",
                    f"Applicability: {c.applicability or ''}",
                    "",
                    c.strength_descriptor or "",
                    "",
                ]
    paths = [index_path]
    for number, content in enumerate(chunks, 1):
        path = kb / f"cspec_guidelines_{number:02d}.md"
        header = [f"<!-- Generated: {generated} | Parser: {PARSER_VERSION} -->", ""]
        path.write_text("\n".join(header + content), encoding="utf-8")
        paths.append(path)
    return paths


def change_report(root: Path) -> None:
    current_path = root / "data/normalized/cspec_all_versions.jsonl"
    previous_path = root / "data/previous/cspec_all_versions.jsonl"
    current = {x["cspec_id"]: x for x in _read_jsonl(current_path)}
    previous = {x["cspec_id"]: x for x in _read_jsonl(previous_path)}
    lines = ["# CSpec change report", "", f"Generated: {_now()}", ""]
    if not previous:
        lines.append("No previous normalized snapshot was available; this is the baseline run.")
    else:
        for key in sorted(current.keys() - previous.keys()):
            lines.append(f"- New document: {key}")
        for key in sorted(previous.keys() - current.keys()):
            lines.append(f"- Removed document: {key}")
        for key in sorted(current.keys() & previous.keys()):
            for field in (
                "version",
                "document_status",
                "legacy_replaced",
                "legacy_fully_superseded",
            ):
                if current[key].get(field) != previous[key].get(field):
                    lines.append(
                        f"- {key} {field}: {previous[key].get(field)!r} → {current[key].get(field)!r}"
                    )
    (root / "reports/change_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def _write_gene_index(path: Path, docs: list[DocumentRecord]) -> None:
    fields = [
        "gene_symbol",
        "gene_symbol_normalized",
        "hgnc_id",
        "cspec_id",
        "title",
        "vcep",
        "version",
        "document_status",
        "release_date",
        "modified_at",
        "diseases",
        "modes_of_inheritance",
        "legacy_replaced",
        "legacy_fully_superseded",
        "source_api_url",
        "source_ui_url",
        "fetched_at",
        "content_sha256",
        "parser_version",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fields)
        writer.writeheader()
        for d in docs:
            if d.document_status != "current_released":
                continue
            for gene in d.genes:
                row = d.model_dump(exclude={"genes", "status_history"})
                row.update(
                    gene_symbol=gene.get("symbol"),
                    gene_symbol_normalized=(gene.get("symbol") or "").upper(),
                    hgnc_id=gene.get("hgnc_id"),
                    diseases=json.dumps(d.diseases, ensure_ascii=False),
                    modes_of_inheritance=json.dumps(d.modes_of_inheritance, ensure_ascii=False),
                )
                writer.writerow(row)


def _load_json(path: Path, default: Any) -> Any:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else default


def _write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _append_jsonl(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(value, ensure_ascii=False) + "\n")


def _write_jsonl(path: Path, values: list[Any]) -> None:
    path.write_text(
        "".join(json.dumps(v, ensure_ascii=False) + "\n" for v in values), encoding="utf-8"
    )


def _read_jsonl(path: Path) -> list[Any]:
    if not path.exists():
        return []
    return [
        json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()
    ]


def _duplicates(values: Any) -> list[Any]:
    counts = Counter(values)
    return [x for x, count in counts.items() if count > 1]


def _dedupe_models(values: list[CriterionRecord]) -> list[CriterionRecord]:
    seen: set[str] = set()
    result: list[CriterionRecord] = []
    for value in values:
        marker = json.dumps(value.model_dump(), sort_keys=True, ensure_ascii=False)
        if marker not in seen:
            seen.add(marker)
            result.append(value)
    return result


def _display(values: list[Any]) -> str:
    return "; ".join(
        (x.get("label") or x.get("id") or "") if isinstance(x, dict) else str(x) for x in values
    )


def _now() -> str:
    return datetime.now(UTC).isoformat()
