from __future__ import annotations

import json
import logging
from pathlib import Path

import typer

from .http import CSpecClient, atomic_write
from .pipeline import build_kb, change_report, collect, normalize, validate

app = typer.Typer(no_args_is_help=True)


def _setup(level: str) -> None:
    logging.basicConfig(
        level=getattr(logging, level.upper()), format="%(asctime)s %(levelname)s %(message)s"
    )


@app.command()
def inspect(output_dir: Path = Path("."), log_level: str = "INFO") -> None:
    """Save a five-record API sample and three representative JSON-LD documents."""
    _setup(log_level)
    reports = output_dir / "reports"
    reports.mkdir(parents=True, exist_ok=True)
    with CSpecClient() as client:
        result = client.get(
            "/cspec/SequenceVariantInterpretation/id", {"pg": 1, "pgSize": 5, "detail": "high"}
        )
        atomic_write(output_dir / "data/raw/inspection/list_sample.json", result.body)
        data = json.loads(result.body).get("data", [])
        ids = [str(x.get("entId")) for x in data[:3] if x.get("entId")]
        for cspec_id in ids:
            doc = client.get(f"/cspec/api/SequenceVariantInterpretation/id/{cspec_id}")
            atomic_write(output_dir / f"data/raw/inspection/{cspec_id}.json", doc.body)
    lines = [
        "# CSpec API structure",
        "",
        "Observed from the live API.",
        "",
        "- List path: `/cspec/SequenceVariantInterpretation/id`",
        "- Valid `detail` values: `nold`, `low`, `med`, `high`",
        "- JSON-LD path: `/cspec/api/SequenceVariantInterpretation/id/{cspec_id}`",
        "- Document fields: `@id`, `label`, `version`, `affiliation`, `currentStatus`, `ruleSets`",
        "- Genes: `ruleSets[].genes[]`; diseases: `genes[].diseases[]`; inheritance: `diseases[].modeOfInheritance[]`",
        "- Criteria: `ruleSets[].criteriaCodes[]`; strengths: `criteriaCodes[].evidenceStrengths[]`",
        "- Status history and legacy flags are available in the high-detail list record under `entContent` when supplied.",
        "",
        "Sample IDs: " + ", ".join(ids),
    ]
    (reports / "api_structure.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


@app.command("collect")
def collect_cmd(
    output_dir: Path = typer.Option(Path("."), "--output-dir"),
    resume: bool = False,
    force: bool = False,
    page_size: int = 25,
    max_retries: int = 5,
    log_level: str = "INFO",
) -> None:
    _setup(log_level)
    collect(output_dir, page_size, resume, force, max_retries)


@app.command("normalize")
def normalize_cmd(
    output_dir: Path = typer.Option(Path("."), "--output-dir"), log_level: str = "INFO"
) -> None:
    _setup(log_level)
    normalize(output_dir)


@app.command("validate")
def validate_cmd(
    output_dir: Path = typer.Option(Path("."), "--output-dir"), log_level: str = "INFO"
) -> None:
    _setup(log_level)
    if not validate(output_dir):
        raise typer.Exit(1)


@app.command("build-kb")
def build_kb_cmd(
    output_dir: Path = typer.Option(Path("."), "--output-dir"), log_level: str = "INFO"
) -> None:
    _setup(log_level)
    build_kb(output_dir)


@app.command()
def all(
    output_dir: Path = typer.Option(Path("."), "--output-dir"),
    resume: bool = False,
    force: bool = False,
    page_size: int = 25,
    max_retries: int = 5,
    log_level: str = "INFO",
) -> None:
    _setup(log_level)
    collect(output_dir, page_size, resume, force, max_retries)
    normalize(output_dir)
    build_kb(output_dir)
    change_report(output_dir)
    if not validate(output_dir):
        raise typer.Exit(1)
