import json
from argparse import Namespace

from cspec_parser.normalizer import direction, normalize_criterion
from cspec_parser.rule_extractor import extract_rules
from cspec_parser.threshold_parser import extract_thresholds
from transform_cspec import index_record, transform


def document(**extra):
    value = {
        "cspec_id": "GN002",
        "title": "x",
        "version": "2.0",
        "document_status": "current_released",
        "genes": [{"symbol": "MYH7", "hgnc_id": None}],
        "source_api_url": "api",
        "source_ui_url": "ui",
    }
    value.update(extra)
    return value


def test_normalizes_criterion_strength_variants():
    assert normalize_criterion("PVS1_Strong")[:2] == ("PVS1", "Strong")
    assert normalize_criterion("PM2 Supporting")[:2] == ("PM2", "Supporting")


def test_direction():
    assert direction("BA1") == "benign" and direction("PS3") == "pathogenic"


def test_not_applicable_rule():
    rules = extract_rules(document(criteria={"PVS1": {"description": "do not use PVS1"}}))
    assert rules[0].applicable is False


def test_threshold_percent_is_fraction():
    threshold = extract_thresholds("REVEL >= 50% and AF < 0.0001")[0]
    assert threshold["value"] == 0.5 and threshold["metric"] == "revel_score"


def test_regions_and_conditions_preserved():
    rules = extract_rules(
        document(
            criteria=[
                {
                    "criterion": "PM1",
                    "description": "domain",
                    "conditions": [{"type": "variant_type", "value": ["missense"]}],
                    "regions": [{"type": "protein_region", "start": 1, "end": 2}],
                }
            ]
        )
    )
    assert rules[0].conditions and rules[0].regions


def test_index_deduplicates_gene_symbols():
    record = index_record(document(genes=[{"symbol": "MYH7"}, {"symbol": "MYH7"}]))
    assert record["gene_symbols"] == ["MYH7"]


def test_metadata_only_warns_without_fabricating_rules(tmp_path):
    source = tmp_path / "docs.jsonl"
    source.write_text(json.dumps(document()) + "\n", encoding="utf-8")
    args = Namespace(
        input=source,
        index_output=tmp_path / "index.jsonl",
        rules_output=tmp_path / "rules.jsonl",
        report_output=tmp_path / "report.json",
        include_non_current=False,
    )
    assert transform(args) == 0
    assert (tmp_path / "rules.jsonl").read_text(encoding="utf-8") == ""
    assert (
        json.loads((tmp_path / "report.json").read_text(encoding="utf-8"))["warnings"][0]["code"]
        == "NO_RULE_CONTENT_FOUND"
    )


def test_non_current_is_skipped_by_default(tmp_path):
    source = tmp_path / "docs.jsonl"
    source.write_text(
        json.dumps(document(document_status="legacy_replaced")) + "\n", encoding="utf-8"
    )
    args = Namespace(
        input=source,
        index_output=tmp_path / "i",
        rules_output=tmp_path / "r",
        report_output=tmp_path / "v",
        include_non_current=False,
    )
    transform(args)
    assert (tmp_path / "i").read_text(encoding="utf-8") == ""


def test_include_non_current(tmp_path):
    source = tmp_path / "docs.jsonl"
    source.write_text(
        json.dumps(document(document_status="legacy_replaced")) + "\n", encoding="utf-8"
    )
    args = Namespace(
        input=source,
        index_output=tmp_path / "i",
        rules_output=tmp_path / "r",
        report_output=tmp_path / "v",
        include_non_current=True,
    )
    transform(args)
    assert (tmp_path / "i").read_text(encoding="utf-8")


def test_malformed_json_continues(tmp_path):
    source = tmp_path / "docs.jsonl"
    source.write_text("{bad}\n" + json.dumps(document()) + "\n", encoding="utf-8")
    args = Namespace(
        input=source,
        index_output=tmp_path / "i",
        rules_output=tmp_path / "r",
        report_output=tmp_path / "v",
        include_non_current=False,
    )
    transform(args)
    assert json.loads((tmp_path / "v").read_text(encoding="utf-8"))["errors"]

