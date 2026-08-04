from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

from cspec_parser.loader import load_jsonl
from cspec_parser.rule_extractor import extract_rules, rules_from_normalized_criteria
from cspec_parser.validator import duplicate_ids, validate_rule
from cspec_parser.writer import write_jsonl, write_report


def is_current(document: dict[str, Any]) -> bool:
    if document.get("document_status") == "current_released":
        return True
    return any(
        isinstance(item, dict) and item.get("current") is True and item.get("name") == "Released"
        for item in document.get("status_history", [])
    )


def index_record(document: dict[str, Any]) -> dict[str, Any]:
    genes = document.get("genes") if isinstance(document.get("genes"), list) else []
    symbols = []
    for gene in genes:
        symbol = gene.get("symbol") if isinstance(gene, dict) else None
        if isinstance(symbol, str) and symbol and symbol not in symbols:
            symbols.append(symbol)
    return {
        "cspec_id": document.get("cspec_id"),
        "title": document.get("title"),
        "vcep": document.get("vcep"),
        "version": document.get("version"),
        "document_status": document.get("document_status"),
        "is_current": is_current(document),
        "release_date": document.get("release_date"),
        "modified_at": document.get("modified_at"),
        "genes": genes,
        "gene_symbols": symbols,
        "diseases": document.get("diseases", []),
        "modes_of_inheritance": document.get("modes_of_inheritance", []),
        "source_api_url": document.get("source_api_url", ""),
        "source_ui_url": document.get("source_ui_url", ""),
        "content_sha256": document.get("content_sha256", ""),
        "parser_version": document.get("parser_version", ""),
    }


def transform(args: argparse.Namespace) -> int:
    indexes, rules, errors, warnings = [], [], [], []
    for line, document, parse_error in load_jsonl(args.input):
        if parse_error:
            errors.append({"line": line, "message": parse_error})
            continue
        assert document is not None
        current = is_current(document)
        if not current and not args.include_non_current:
            continue
        index = index_record(document)
        indexes.append(index)
        extracted = extract_rules(document)
        rules.extend(extracted)
        if not extracted:
            warnings.append(
                {
                    "code": "NO_RULE_CONTENT_FOUND",
                    "message": "The source record contains document metadata but no extractable ACMG/AMP rule content.",
                    "cspec_id": document.get("cspec_id"),
                    "line": line,
                }
            )
    if getattr(args, "criteria_input", None):
        criteria = []
        for line, item, parse_error in load_jsonl(args.criteria_input):
            if parse_error:
                errors.append({"line": line, "message": parse_error, "input": "criteria"})
                continue
            if item is not None:
                criteria.append(item)
        rules = rules_from_normalized_criteria(criteria)
        warnings = [warning for warning in warnings if warning.get("code") != "NO_RULE_CONTENT_FOUND"]
    gene_symbols = {symbol for index in indexes for symbol in index["gene_symbols"]}
    for rule in rules:
        errors.extend(
            {**error, "rule_id": rule.rule_id} for error in validate_rule(rule, gene_symbols)
        )
    duplicates = duplicate_ids(rules)
    errors.extend({"code": "DUPLICATE_RULE_ID", "message": rule_id} for rule_id in duplicates)
    report = {
        "input_documents": len(indexes),
        "indexed_documents": len(indexes),
        "skipped_non_current_documents": 0,
        "rules_created": len(rules),
        "rules_requiring_manual_review": sum(rule.requires_manual_review for rule in rules),
        "errors": errors,
        "warnings": warnings,
    }
    write_jsonl(args.index_output, indexes)
    write_jsonl(args.rules_output, rules)
    write_report(args.report_output, report)
    return 1 if errors else 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Transform CSPEC document JSONL into index and explicit ACMG/AMP rules"
    )
    parser.add_argument("--input", type=Path, default=Path("cspec_documents.jsonl"))
    parser.add_argument("--index-output", type=Path, default=Path("cspec_document_index.jsonl"))
    parser.add_argument("--rules-output", type=Path, default=Path("cspec_rules.jsonl"))
    parser.add_argument("--report-output", type=Path, default=Path("cspec_validation_report.json"))
    parser.add_argument("--include-non-current", action="store_true")
    parser.add_argument(
        "--criteria-input",
        type=Path,
        help="Optional normalized cspec_criteria.jsonl; use it to populate rules while indexing documents.",
    )
    return transform(parser.parse_args())


if __name__ == "__main__":
    raise SystemExit(main())

