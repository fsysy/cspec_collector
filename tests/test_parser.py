import json
from pathlib import Path

from cspec_collector.parser import (
    classify_document,
    first_recursive,
    parse_criteria,
    parse_document,
    scalar,
)

FIXTURE = Path(__file__).parent / "fixtures/GN002.json"


def raw(**content):
    return {"entId": "GN002", "entContent": content, "modified": "2024-01-01", "ldFor": {}}


def test_scalar_is_tolerant():
    assert scalar({"unexpected": 1, "label": "value"}) == "value"
    assert scalar(None) is None


def test_recursive_fallback_finds_nested_field():
    assert first_recursive({"unknown": [{"legacyReplaced": True}]}, ["legacyReplaced"]) is True


def test_current_released_requires_released_history():
    assert (
        classify_document(
            raw(states=[{"name": "Released", "current": True}]), {"currentStatus": "Released"}
        )
        == "current_released"
    )


def test_released_without_history_is_ambiguous():
    assert classify_document(raw(), {"currentStatus": "Released"}) == "ambiguous"


def test_legacy_replaced_precedes_release():
    assert (
        classify_document(raw(legacyReplaced=True, states=[{"name": "Released", "current": True}]))
        == "legacy_replaced"
    )


def test_superseded_flag():
    assert classify_document(raw(legacyFullySuperseded=True)) == "superseded"


def test_under_review_state():
    assert (
        classify_document(raw(states=[{"name": "Pilot Rules Submitted", "current": True}]))
        == "under_review"
    )


def test_parse_document_extracts_gene_disease_and_hgnc():
    detail = json.loads(FIXTURE.read_text(encoding="utf-8"))
    source = raw(
        states=[{"name": "Released", "current": True, "event": {"timeStamp": "2024-02-01"}}]
    )
    doc = parse_document(source, detail, b"body", "2024-02-02T00:00:00Z")
    assert doc.genes == [{"symbol": "MYH7", "hgnc_id": "HGNC:7577"}]
    assert doc.modes_of_inheritance == ["Autosomal dominant"]
    assert doc.document_status == "current_released"


def test_strengths_are_separate_records():
    detail = json.loads(FIXTURE.read_text(encoding="utf-8"))
    doc = parse_document(raw(states=[{"name": "Released", "current": True}]), detail, b"x", "now")
    records = parse_criteria(doc, detail)
    assert len(records) == 2
    assert {r.strength for r in records} == {"Moderate", "Strong"}


def test_unknown_fields_do_not_break_parser():
    detail = json.loads(FIXTURE.read_text(encoding="utf-8"))
    detail["brandNewField"] = {"anything": [1, 2, 3]}
    doc = parse_document(raw(states=[{"name": "Released", "current": True}]), detail, b"x", "now")
    assert doc.cspec_id == "GN002"


def test_missing_gene_is_preserved_not_invented():
    detail = json.loads(FIXTURE.read_text(encoding="utf-8"))
    detail["ruleSets"][0].pop("genes")
    doc = parse_document(raw(states=[{"name": "Released", "current": True}]), detail, b"x", "now")
    assert doc.genes == []


def test_null_values_remain_null():
    detail = json.loads(FIXTURE.read_text(encoding="utf-8"))
    detail["version"] = None
    doc = parse_document(raw(states=[{"name": "Released", "current": True}]), detail, b"x", "now")
    assert doc.version is None
