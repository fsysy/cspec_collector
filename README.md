[English](./README.md) | [한국어](./README.ko.md)

# ClinGen CSpec Collector

Collects the official ClinGen CSpec Registry API, preserves raw JSON, classifies current versus historical documents, produces gene/criterion normalized data, and builds Custom GPT Knowledge Markdown without summarizing scientific language.

## Project status

Active development. Declared: 2026-08-05.

## Project policy

- **Constitution**: follows the llama agent constitution, version `0.9.0`. Last constitutional review: 2026-08-05, scope: full project (README, source, tests, `.gitignore`, git hygiene).
- **Testing**: pytest is required for this project (parsing/normalization logic needs regression coverage). Reviewed 2026-08-05 — `tests/` has 23 passing tests.
- **Lint**: Ruff is the project linter. Reviewed 2026-08-05 — `ruff check .` passed with no findings.
- **Logging**: console-only via Python's standard `logging` module, controlled by `--log-level` (see Commands below); no persistent log file is kept. Decided 2026-08-05.
- **Package/project management**: uv + `pyproject.toml`, `src/` layout with `cspec_collector` and `cspec_parser` packages. Reviewed 2026-08-05 — compliant, no exemption needed.
- **Generated data in git**: `data/raw/`, `data/normalized/`, `data/transformed/`, and `kb/` are tracked in git (not gitignored) so the collected and parsed ClinGen data can be shared directly from the repository instead of requiring a local pipeline run or a workflow artifact download. Decided 2026-08-05; this supersedes an earlier hygiene fix that had gitignored those paths.

## Requirements and setup

Python 3.11 or newer, managed with [uv](https://docs.astral.sh/uv/).

Install uv if you don't already have it:

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows PowerShell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# or, if you already have Python and pip
pip install uv
```

Then set up the project. `uv sync` creates `.venv` and installs exact locked dependencies from `uv.lock`; `uv run` executes a command inside that environment without manually activating it:

```bash
uv sync --extra dev
uv run pytest
```

## Commands

```bash
uv run python -m cspec_collector inspect
uv run python -m cspec_collector collect --resume
uv run python -m cspec_collector normalize
uv run python -m cspec_collector validate
uv run python -m cspec_collector build-kb
uv run python -m cspec_collector all --resume
```

Common options are `--resume`, `--force`, `--page-size`, `--output-dir`, `--max-retries`, and `--log-level`. Requests use a 60-second timeout, at least 0.5 seconds between calls, and exponential-backoff retries. If a list page fails, collection automatically retries at page sizes 10 and 5. `--resume` reuses valid saved pages and documents; `--force` ignores caches.

Raw server responses live under `data/raw/`; normalized output under `data/normalized/`; Knowledge files under `kb/`; inspection, failure, validation, change, and HTTP manifest reports under `reports/`.

`normalize` also writes `data/normalized/cspec_evidence_index.jsonl`, a per-document index for knowledge-base lookups. One line per `cspec_id`, with:

- `gene_symbols`: list of genes the document covers.
- `applicable`: criterion/strength combinations whose `applicability` is some form of "applicable" (e.g. `PM1_Strong`, `PM2_Supporting`; no strength suffix when a code has none), each with `description` (the criterion's general ACMG/AMP meaning) and `specification` (the VCEP's specific application text for that strength, when the source provides one).
- `not_applicable`: the same token format, for combinations the VCEP explicitly does not use. These never carry a description in the source data, so they are kept as a plain list.

A document with no gene in the source API (see `reports/validation_report.md`) has an empty `gene_symbols` list; nothing is invented.

The API sometimes omits HGNC IDs, status fields, and legacy flags. The collector keeps those values null or classifies the document as `ambiguous`; it never invents them. More than one current released document for a gene is preserved and reported as a warning.

## Manual refresh

`.github/workflows/refresh_cspec.yml` runs only on manual dispatch (no schedule). It tests, collects, validates, uploads all results as an artifact, and opens/updates the `cspec-data-update` pull request when repository permissions allow. Enable **Settings → Actions → General → Workflow permissions → Read and write permissions** and allow Actions to create pull requests. The workflow never merges into `main` automatically.

## API endpoints

- List: `GET https://cspec.genome.network/cspec/SequenceVariantInterpretation/id`
- JSON-LD: `GET https://cspec.genome.network/cspec/api/SequenceVariantInterpretation/id/{cspec_id}`
- Versions: `GET https://cspec.genome.network/cspec/SequenceVariantInterpretation/id/{cspec_id}/version`

The collector uses observed live response shapes and tolerates unknown additional fields. Run `inspect` to recreate `reports/api_structure.md` from live samples.

## Transform an existing document JSONL

The standalone transformer reads `cspec_documents.jsonl` (or any compatible JSONL path) and writes a metadata index, explicit ACMG/AMP rules, and a machine-readable validation report:

```bash
uv run python transform_cspec.py \
  --input cspec_documents.jsonl \
  --criteria-input cspec_criteria.jsonl \
  --index-output cspec_document_index.jsonl \
  --rules-output cspec_rules.jsonl \
  --report-output cspec_validation_report.json
```

`--criteria-input` should point at the normalized `cspec_criteria.jsonl` produced by `normalize`; without it, the input JSONL alone carries no embedded rule content and `cspec_rules.jsonl` will be created empty (with a `NO_RULE_CONTENT_FOUND` warning per document) — this is not a bug, just a signal that no criteria source was supplied.

Use `--include-non-current` to include legacy, superseded, and other non-current documents. The transformer recognizes all standard ACMG/AMP criteria, pathogenic/benign direction, strength variants such as `PVS1_Strong` and `PM2 Supporting`, applicability phrases, numeric thresholds, regions, conditions, exclusions, and source paths. It creates a rule only when an explicit criterion-bearing node is present. Metadata-only records produce an empty rules file plus a `NO_RULE_CONTENT_FOUND` warning; no scientific rule is invented.

The transformer is intentionally loss-preserving: original criterion text, source paths, references, and ambiguous values remain in each rule record. Conflicts, missing source paths, malformed JSON lines, invalid thresholds, and duplicate IDs are reported while later lines continue processing. Run its tests with `uv run pytest`.
