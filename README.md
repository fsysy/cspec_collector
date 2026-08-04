# ClinGen CSpec Collector

Collects the official ClinGen CSpec Registry API, preserves raw JSON, classifies current versus historical documents, produces gene/criterion normalized data, and builds Custom GPT Knowledge Markdown without summarizing scientific language.

## Requirements and setup

Python 3.11 or newer:

```bash
python -m venv .venv
. .venv/bin/activate       # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -e '.[dev]'
pytest
```

## Commands

```bash
python -m cspec_collector inspect
python -m cspec_collector collect --resume
python -m cspec_collector normalize
python -m cspec_collector validate
python -m cspec_collector build-kb
python -m cspec_collector all --resume
```

Common options are `--resume`, `--force`, `--page-size`, `--output-dir`, `--max-retries`, and `--log-level`. Requests use a 60-second timeout, at least 0.5 seconds between calls, and exponential-backoff retries. If a list page fails, collection automatically retries at page sizes 10 and 5. `--resume` reuses valid saved pages and documents; `--force` ignores caches.

Raw server responses live under `data/raw/`; normalized output under `data/normalized/`; Knowledge files under `kb/`; inspection, failure, validation, change, and HTTP manifest reports under `reports/`.

The API sometimes omits HGNC IDs, status fields, and legacy flags. The collector keeps those values null or classifies the document as `ambiguous`; it never invents them. More than one current released document for a gene is preserved and reported as a warning.

## Scheduled refresh

`.github/workflows/refresh_cspec.yml` runs weekly and manually. It tests, collects, validates, uploads all results as an artifact, and opens/updates the `cspec-data-update` pull request when repository permissions allow. Enable **Settings ??Actions ??General ??Workflow permissions ??Read and write permissions** and allow Actions to create pull requests. The workflow never merges into `main` automatically.

## API endpoints

- List: `GET https://cspec.genome.network/cspec/SequenceVariantInterpretation/id`
- JSON-LD: `GET https://cspec.genome.network/cspec/api/SequenceVariantInterpretation/id/{cspec_id}`
- Versions: `GET https://cspec.genome.network/cspec/SequenceVariantInterpretation/id/{cspec_id}/version`

The collector uses observed live response shapes and tolerates unknown additional fields. Run `inspect` to recreate `reports/api_structure.md` from live samples.

## Transform an existing document JSONL

The standalone transformer reads `cspec_documents.jsonl` (or any compatible JSONL path) and writes a metadata index, explicit ACMG/AMP rules, and a machine-readable validation report:

```bash
python transform_cspec.py \
  --input cspec_documents.jsonl \
  --index-output cspec_document_index.jsonl \
  --rules-output cspec_rules.jsonl \
  --report-output cspec_validation_report.json
```

Use `--include-non-current` to include legacy, superseded, and other non-current documents. The transformer recognizes all standard ACMG/AMP criteria, pathogenic/benign direction, strength variants such as `PVS1_Strong` and `PM2 Supporting`, applicability phrases, numeric thresholds, regions, conditions, exclusions, and source paths. It creates a rule only when an explicit criterion-bearing node is present. Metadata-only records produce an empty rules file plus a `NO_RULE_CONTENT_FOUND` warning; no scientific rule is invented.

The transformer is intentionally loss-preserving: original criterion text, source paths, references, and ambiguous values remain in each rule record. Conflicts, missing source paths, malformed JSON lines, invalid thresholds, and duplicate IDs are reported while later lines continue processing. Run its tests with `pytest`.

