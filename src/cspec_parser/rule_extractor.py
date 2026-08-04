from __future__ import annotations

from typing import Any

from .models import RuleRecord
from .normalizer import direction, is_not_applicable, normalize_criterion, text_of
from .threshold_parser import extract_thresholds


def extract_rules(document: dict[str, Any]) -> list[RuleRecord]:
    """Extract explicit criterion-bearing nodes; never create rules from keywords alone."""
    cspec_id = str(document.get("cspec_id", ""))
    genes = document.get("genes") or [{"symbol": None, "hgnc_id": None}]
    candidates: list[tuple[str, Any]] = []

    def walk(value: Any, path: str) -> None:
        if isinstance(value, dict):
            marker = (
                value.get("criterion")
                or value.get("criterion_code")
                or value.get("label")
                or value.get("name")
            )
            criterion, _, _ = normalize_criterion(marker or path.rsplit(".", 1)[-1])
            if criterion:
                candidates.append((path, value))
            for key, child in value.items():
                walk(child, f"{path}.{key}")
        elif isinstance(value, list):
            for index, child in enumerate(value):
                walk(child, f"{path}[{index}]")

    for key in ("criteria", "rules", "specifications", "content", "rule_sets", "ruleSets"):
        if key in document:
            walk(document[key], f"$.{key}")
    output: list[RuleRecord] = []
    seen: dict[tuple[Any, ...], RuleRecord] = {}
    for path, node in candidates:
        raw_marker = (
            node.get("criterion")
            or node.get("criterion_code")
            or node.get("label")
            or node.get("name")
        )
        criterion, strength, raw = normalize_criterion(raw_marker or path.rsplit(".", 1)[-1])
        if not criterion:
            continue
        rule_text = text_of(node)
        if not rule_text:
            rule_text = text_of(node.get("description"))
        allowed = (
            [str(x) for x in node.get("allowed_strengths", node.get("evidenceStrengths", []))]
            if isinstance(node.get("allowed_strengths", node.get("evidenceStrengths", [])), list)
            else []
        )
        applicable = (
            node.get("applicable")
            if isinstance(node.get("applicable"), bool)
            else (False if is_not_applicable(rule_text) else None)
        )
        confidence = "high" if applicable is not None or strength or rule_text else "low"
        review = confidence == "low" or applicable is None
        for gene in genes:
            symbol = gene.get("symbol") if isinstance(gene, dict) else str(gene)
            key = (cspec_id, symbol, criterion, strength, path)
            if key in seen:
                continue
            seq = f"{len(output) + 1:03d}"
            record = RuleRecord(
                rule_id=f"{cspec_id}:{symbol or 'ALL'}:{criterion}:{seq}",
                cspec_id=cspec_id,
                gene=symbol,
                hgnc_id=gene.get("hgnc_id") if isinstance(gene, dict) else None,
                criterion=criterion,
                criterion_raw=raw,
                direction=direction(criterion),
                applicable=applicable,
                strength=strength,
                allowed_strengths=allowed,
                default_strength=node.get("default_strength"),
                thresholds=extract_thresholds(rule_text),
                conditions=node.get("conditions", []),
                exclusions=node.get("exclusions", []),
                variant_types=node.get("variant_types", []),
                regions=node.get("regions", []),
                transcripts=node.get("transcripts", []),
                diseases=document.get("diseases", []),
                modes_of_inheritance=document.get("modes_of_inheritance", []),
                summary=str(node.get("summary", "")),
                rule_text=rule_text,
                notes=list(node.get("notes", []))
                if isinstance(node.get("notes", []), list)
                else [str(node.get("notes"))],
                references=node.get("references", []),
                source_path=path,
                source_paths=[path],
                source_api_url=str(document.get("source_api_url", "")),
                source_ui_url=str(document.get("source_ui_url", "")),
                document_version=document.get("version"),
                document_status=document.get("document_status"),
                release_date=document.get("release_date"),
                extraction_confidence=confidence,
                requires_manual_review=review,
            )
            seen[key] = record
            output.append(record)
    return output


def rules_from_normalized_criteria(criteria: list[dict[str, Any]]) -> list[RuleRecord]:
    """Convert collector criterion records into the standalone rule schema.

    The collector's normalized document index intentionally omits the nested API
    ruleSets, while ``cspec_criteria.jsonl`` retains one loss-preserving record
    for each criterion/strength/gene combination.  This adapter lets the
    transformer consume that stable output without inventing rule content.
    """
    output: list[RuleRecord] = []
    seen: set[tuple[Any, ...]] = set()
    for item in criteria:
        code, strength, raw = normalize_criterion(
            item.get("criterion_code") or item.get("criterion_label")
        )
        if not code:
            continue
        gene = item.get("gene_symbol")
        key = (item.get("cspec_id"), gene, code, strength or item.get("strength"), item.get("ruleset_id"))
        if key in seen:
            continue
        seen.add(key)
        actual_strength = strength or item.get("strength")
        descriptor = str(item.get("strength_descriptor") or "").strip()
        description = str(item.get("criterion_description") or "").strip()
        rule_text = "\n\n".join(value for value in (description, descriptor) if value)
        applicability = str(item.get("applicability") or "").strip()
        applicable = None
        if applicability.casefold() == "applicable":
            applicable = True
        elif applicability.casefold() in {"not applicable", "not-applicable"}:
            applicable = False
        suffix = actual_strength or "unspecified"
        rule_id = f"{item.get('cspec_id')}:{gene or 'ALL'}:{code}:{suffix}"
        source_path = str(item.get("ruleset_id") or "")
        output.append(
            RuleRecord(
                rule_id=rule_id,
                cspec_id=str(item.get("cspec_id") or ""),
                gene=gene,
                hgnc_id=item.get("hgnc_id"),
                criterion=code,
                criterion_raw=raw,
                direction=direction(code),
                applicable=applicable,
                strength=actual_strength,
                allowed_strengths=[actual_strength] if actual_strength else [],
                diseases=item.get("diseases", []),
                modes_of_inheritance=item.get("modes_of_inheritance", []),
                summary=description,
                rule_text=rule_text,
                source_path=source_path,
                source_paths=[source_path] if source_path else [],
                source_api_url=str(item.get("source_api_url") or ""),
                document_version=item.get("version"),
                extraction_confidence="high",
                requires_manual_review=applicable is None,
            )
        )
    return output

