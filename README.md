# ClinGen CSpec Collector

Collects the official ClinGen CSpec Registry API, preserves raw JSON, classifies current versus historical documents, produces gene/criterion normalized data, and builds Custom GPT Knowledge Markdown without summarizing scientific language.

Pick a language below — click a heading to expand it (GitHub Markdown has no real tabs, so this uses collapsible sections instead).

<details open>
<summary><strong>🇬🇧 English</strong></summary>

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
  --index-output cspec_document_index.jsonl \
  --rules-output cspec_rules.jsonl \
  --report-output cspec_validation_report.json
```

Use `--include-non-current` to include legacy, superseded, and other non-current documents. The transformer recognizes all standard ACMG/AMP criteria, pathogenic/benign direction, strength variants such as `PVS1_Strong` and `PM2 Supporting`, applicability phrases, numeric thresholds, regions, conditions, exclusions, and source paths. It creates a rule only when an explicit criterion-bearing node is present. Metadata-only records produce an empty rules file plus a `NO_RULE_CONTENT_FOUND` warning; no scientific rule is invented.

The transformer is intentionally loss-preserving: original criterion text, source paths, references, and ambiguous values remain in each rule record. Conflicts, missing source paths, malformed JSON lines, invalid thresholds, and duplicate IDs are reported while later lines continue processing. Run its tests with `uv run pytest`.

</details>

<details>
<summary><strong>🇰🇷 한국어</strong></summary>

## 프로젝트 상태

활성 개발 중(Active development). 선언일: 2026-08-05.

## 프로젝트 정책

- **헌법(Constitution)**: llama 에이전트 헌법 `0.9.0` 버전을 따릅니다. 마지막 헌법심판: 2026-08-05, 범위: 프로젝트 전체(README, 소스, 테스트, `.gitignore`, git 위생).
- **테스트**: 파싱/정규화 로직에 회귀 테스트가 필요하므로 pytest가 필수입니다. 2026-08-05 검토 — `tests/`에 23개 테스트 통과.
- **린트**: Ruff를 프로젝트 린터로 사용합니다. 2026-08-05 검토 — `ruff check .` 통과, 지적 사항 없음.
- **로깅**: Python 표준 `logging` 모듈을 통한 콘솔 출력만 사용하며(`--log-level`로 제어), 영구 로그 파일은 남기지 않습니다. 2026-08-05 결정.
- **패키지/프로젝트 관리**: uv + `pyproject.toml`, `cspec_collector`와 `cspec_parser` 패키지를 둔 `src/` 레이아웃을 사용합니다. 2026-08-05 검토 — 규정 준수, 예외 불필요.
- **생성 데이터의 git 추적**: `data/raw/`, `data/normalized/`, `data/transformed/`, `kb/`를 gitignore하지 않고 git에 그대로 추적합니다. 파이프라인을 로컬에서 실행하거나 워크플로 아티팩트를 내려받지 않아도 저장소에서 바로 수집·정제된 ClinGen 데이터를 공유할 수 있도록 하기 위함입니다. 2026-08-05 결정 — 이전에 이 경로들을 gitignore했던 위생 조치를 대체합니다.

## 요구사항 및 설치

Python 3.11 이상이 필요하며, [uv](https://docs.astral.sh/uv/)로 패키지를 관리합니다.

uv가 아직 없다면 먼저 설치하세요:

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows PowerShell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# 이미 Python과 pip이 있다면
pip install uv
```

그다음 프로젝트를 설정합니다. `uv sync`는 `.venv`를 만들고 `uv.lock`에 고정된 의존성을 정확히 설치합니다. `uv run`은 가상환경을 수동으로 활성화하지 않고도 그 안에서 명령을 실행합니다:

```bash
uv sync --extra dev
uv run pytest
```

## 명령어

```bash
uv run python -m cspec_collector inspect
uv run python -m cspec_collector collect --resume
uv run python -m cspec_collector normalize
uv run python -m cspec_collector validate
uv run python -m cspec_collector build-kb
uv run python -m cspec_collector all --resume
```

공통 옵션으로 `--resume`, `--force`, `--page-size`, `--output-dir`, `--max-retries`, `--log-level`이 있습니다. 요청은 60초 타임아웃, 호출 간 최소 0.5초 간격, 지수 백오프 재시도를 사용합니다. 목록 페이지 요청이 실패하면 페이지 크기를 10, 5로 낮춰 자동 재시도합니다. `--resume`은 유효한 저장 페이지·문서를 재사용하고, `--force`는 캐시를 무시합니다.

서버 원본 응답은 `data/raw/`, 정규화된 출력은 `data/normalized/`, 지식 파일은 `kb/`, 점검·실패·검증·변경·HTTP 매니페스트 리포트는 `reports/` 아래에 저장됩니다.

API가 HGNC ID, 상태 필드, 레거시 플래그를 종종 누락하는 경우가 있습니다. 수집기는 이런 값을 null로 두거나 문서를 `ambiguous`로 분류할 뿐, 값을 임의로 만들어내지 않습니다. 한 유전자에 현재(current released) 문서가 둘 이상 있으면 그대로 보존하고 경고로 보고합니다.

## 수동 갱신

`.github/workflows/refresh_cspec.yml`은 예약 실행 없이 수동 실행(workflow_dispatch)으로만 동작합니다. 테스트, 수집, 검증을 수행하고 전체 결과를 아티팩트로 업로드하며, 저장소 권한이 허용하면 `cspec-data-update` 풀 리퀘스트를 열거나 갱신합니다. **Settings → Actions → General → Workflow permissions → Read and write permissions**를 활성화하고 Actions가 풀 리퀘스트를 만들 수 있도록 허용하세요. 이 워크플로는 `main`에 자동으로 병합하지 않습니다.

## API 엔드포인트

- 목록: `GET https://cspec.genome.network/cspec/SequenceVariantInterpretation/id`
- JSON-LD: `GET https://cspec.genome.network/cspec/api/SequenceVariantInterpretation/id/{cspec_id}`
- 버전: `GET https://cspec.genome.network/cspec/SequenceVariantInterpretation/id/{cspec_id}/version`

수집기는 실제 응답에서 관찰된 형태를 사용하며 알려지지 않은 추가 필드도 허용합니다. `inspect`를 실행하면 실제 샘플로부터 `reports/api_structure.md`를 다시 생성합니다.

## 기존 문서 JSONL 변환

독립 실행형 변환기는 `cspec_documents.jsonl`(또는 호환되는 임의의 JSONL 경로)을 읽어 메타데이터 색인, 명시적 ACMG/AMP 규칙, 기계 판독 가능한 검증 리포트를 만듭니다:

```bash
uv run python transform_cspec.py \
  --input cspec_documents.jsonl \
  --index-output cspec_document_index.jsonl \
  --rules-output cspec_rules.jsonl \
  --report-output cspec_validation_report.json
```

`--include-non-current`를 주면 레거시, 대체됨(superseded) 등 현재가 아닌 문서도 포함합니다. 변환기는 표준 ACMG/AMP 판정기준 전체, 병원성/양성 방향, `PVS1_Strong`이나 `PM2 Supporting` 같은 강도 변형, 적용 가능성 문구, 수치 임계값, 영역, 조건, 예외, 출처 경로를 인식합니다. 명시적으로 판정기준을 담은 노드가 있을 때만 규칙을 생성합니다. 메타데이터만 있는 레코드는 빈 규칙 파일과 `NO_RULE_CONTENT_FOUND` 경고를 만들 뿐, 과학적 규칙을 임의로 만들어내지 않습니다.

변환기는 의도적으로 정보 손실이 없도록 설계되었습니다. 원본 판정기준 텍스트, 출처 경로, 참고문헌, 모호한 값은 각 규칙 레코드에 그대로 남습니다. 충돌, 누락된 출처 경로, 잘못된 JSON 라인, 유효하지 않은 임계값, 중복 ID는 보고하되 이후 라인 처리는 계속됩니다. 테스트는 `uv run pytest`로 실행하세요.

</details>
