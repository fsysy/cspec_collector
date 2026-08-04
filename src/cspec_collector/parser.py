from __future__ import annotations

import hashlib
import re
from collections.abc import Iterable
from typing import Any
from urllib.parse import unquote

from . import PARSER_VERSION
from .models import CriterionRecord, DocumentRecord

BASE_URL = "https://cspec.genome.network"


def scalar(value: Any) -> str | None:
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip() or None
    if isinstance(value, (int, float, bool)):
        return str(value)
    if isinstance(value, dict):
        for key in ("label", "name", "title", "value", "@id", "id"):
            result = scalar(value.get(key))
            if result:
                return result
    return None


def first_recursive(obj: Any, keys: Iterable[str]) -> Any:
    wanted = {k.casefold() for k in keys}
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key.casefold() in wanted and value not in (None, "", [], {}):
                return value
        for value in obj.values():
            found = first_recursive(value, wanted)
            if found not in (None, "", [], {}):
                return found
    elif isinstance(obj, list):
        for value in obj:
            found = first_recursive(value, wanted)
            if found not in (None, "", [], {}):
                return found
    return None


def list_value(value: Any) -> list[Any]:
    if value is None:
        return []
    return value if isinstance(value, list) else [value]


def classify_document(raw: dict[str, Any], detail: dict[str, Any] | None = None) -> str:
    content = raw.get("entContent", raw)
    legacy_replaced = first_recursive(content, ["legacyReplaced"])
    fully_superseded = first_recursive(content, ["legacyFullySuperseded"])
    if legacy_replaced is True:
        return "legacy_replaced"
    if fully_superseded is True:
        return "superseded"
    states = list_value(content.get("states"))
    names = [str(s.get("name", "")) for s in states if isinstance(s, dict)]
    current = [
        str(s.get("name", "")) for s in states if isinstance(s, dict) and s.get("current") is True
    ]
    status = scalar((detail or {}).get("currentStatus")) or scalar(content.get("currentStatus"))
    status = status or (current[0] if len(current) == 1 else None)
    lower = (status or "").casefold()
    if "archive" in lower or "retire" in lower:
        return "archived"
    if "supersed" in lower:
        return "superseded"
    if lower == "released" and "Released" in names:
        return "current_released"
    if any(token in lower for token in ("review", "submitted", "approved", "prep", "pilot")):
        return "under_review"
    return "ambiguous"


def parse_document(
    raw: dict[str, Any], detail: dict[str, Any], body: bytes, fetched_at: str
) -> DocumentRecord:
    cspec_id = scalar(raw.get("entId")) or _id_from_url(scalar(detail.get("@id")))
    if not cspec_id:
        raise ValueError("Document has no CSpec ID")
    content = raw.get("entContent", {}) if isinstance(raw.get("entContent"), dict) else {}
    rulesets = list_value(detail.get("ruleSets"))
    genes = []
    diseases: list[Any] = []
    inheritance: list[Any] = []
    for ruleset in rulesets:
        if not isinstance(ruleset, dict):
            continue
        for gene in list_value(ruleset.get("genes")):
            if not isinstance(gene, dict):
                continue
            symbol = scalar(gene.get("label"))
            hgnc = _hgnc_id(gene)
            gene_diseases = list_value(gene.get("diseases"))
            genes.append({"symbol": symbol, "hgnc_id": hgnc})
            for disease in gene_diseases:
                if isinstance(disease, dict):
                    diseases.append(
                        {"id": scalar(disease.get("@id")), "label": scalar(disease.get("label"))}
                    )
                    inheritance.extend(_labels(disease.get("modeOfInheritance")))
    affiliation = detail.get("affiliation") if isinstance(detail.get("affiliation"), dict) else {}
    states = list_value(content.get("states"))
    return DocumentRecord(
        cspec_id=cspec_id,
        title=scalar(detail.get("label")) or scalar(content.get("title")),
        vcep=scalar(affiliation.get("label"))
        or scalar(first_recursive(raw.get("ldFor"), ["title"])),
        version=scalar(detail.get("version")) or scalar(content.get("version")),
        document_status=classify_document(raw, detail),
        status_history=states,
        release_date=scalar(content.get("approvedOn")) or _released_date(states),
        modified_at=scalar(detail.get("lastUpdated")) or scalar(raw.get("modified")),
        genes=_unique_dicts(genes),
        diseases=_unique(diseases),
        modes_of_inheritance=_unique(inheritance),
        legacy_replaced=_bool_or_none(first_recursive(content, ["legacyReplaced"])),
        legacy_fully_superseded=_bool_or_none(first_recursive(content, ["legacyFullySuperseded"])),
        source_api_url=f"{BASE_URL}/cspec/api/SequenceVariantInterpretation/id/{cspec_id}",
        source_ui_url=f"{BASE_URL}/cspec/SequenceVariantInterpretation/id/{cspec_id}",
        fetched_at=fetched_at,
        content_sha256=hashlib.sha256(body).hexdigest(),
        parser_version=PARSER_VERSION,
    )


def parse_criteria(document: DocumentRecord, detail: dict[str, Any]) -> list[CriterionRecord]:
    records: list[CriterionRecord] = []
    genes = document.genes or [{"symbol": None, "hgnc_id": None}]
    for ruleset in list_value(detail.get("ruleSets")):
        if not isinstance(ruleset, dict):
            continue
        ruleset_id = scalar(ruleset.get("@id"))
        for criterion in list_value(ruleset.get("criteriaCodes")):
            if not isinstance(criterion, dict):
                continue
            code = scalar(criterion.get("label"))
            label = scalar(criterion.get("name")) or code
            strengths = list_value(criterion.get("evidenceStrengths")) or [None]
            for strength in strengths:
                strength_dict = strength if isinstance(strength, dict) else {}
                strength_label = scalar(strength_dict.get("label"))
                for gene in genes:
                    records.append(
                        CriterionRecord(
                            gene_symbol=gene.get("symbol"),
                            hgnc_id=gene.get("hgnc_id"),
                            cspec_id=document.cspec_id,
                            version=document.version,
                            ruleset_id=ruleset_id,
                            criterion_code=code,
                            criterion_label=label,
                            criterion_description=scalar(criterion.get("description")),
                            strength=strength_label,
                            strength_descriptor=scalar(strength_dict.get("description")),
                            applicability=scalar(strength_dict.get("applicability")),
                            diseases=document.diseases,
                            modes_of_inheritance=document.modes_of_inheritance,
                            source_api_url=document.source_api_url,
                            fetched_at=document.fetched_at,
                        )
                    )
    return records


def _id_from_url(value: str | None) -> str | None:
    return unquote(value.rstrip("/").split("/")[-1]) if value else None


def _hgnc_id(gene: dict[str, Any]) -> str | None:
    value = scalar(first_recursive(gene, ["hgncId", "hgnc_id", "hgnc"]))
    if value:
        match = re.search(r"HGNC:\d+", value, re.IGNORECASE)
        return match.group(0).upper() if match else value
    url = scalar(gene.get("@id"))
    match = re.search(r"HGNC(?::|%3A|/)(\d+)", url or "", re.IGNORECASE)
    return f"HGNC:{match.group(1)}" if match else None


def _labels(value: Any) -> list[Any]:
    return [scalar(item) for item in list_value(value) if scalar(item)]


def _released_date(states: list[Any]) -> str | None:
    for state in states:
        if isinstance(state, dict) and str(state.get("name", "")).casefold() == "released":
            event = state.get("event", {})
            if isinstance(event, dict) and scalar(event.get("timeStamp")):
                return scalar(event.get("timeStamp"))
    return None


def _bool_or_none(value: Any) -> bool | None:
    return value if isinstance(value, bool) else None


def _unique(values: list[Any]) -> list[Any]:
    seen: set[str] = set()
    result = []
    for value in values:
        marker = repr(value)
        if marker not in seen:
            seen.add(marker)
            result.append(value)
    return result


def _unique_dicts(values: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return _unique(values)
