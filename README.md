# BIAN Compliance Auditor

Small public-safe Python tool for checking whether an OpenAPI spec loosely follows BIAN-style conventions.

## What It Checks

- Whether `operationId` values start with common BIAN verbs
- Whether the API exposes a service-domain hint in metadata
- Whether common model patterns such as `status`, `reference`, and `record` appear

## Quick Start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
PYTHONPATH=src python -m bian_auditor.cli examples/sample_service.yaml
```

## Run Tests

```bash
PYTHONPATH=src python3 -m pytest -q
```

## Project Layout

- `src/bian_auditor`: compliance checks and CLI
- `examples/`: neutral sample OpenAPI document
- `tests/`: unit tests for compliant and non-compliant cases

## Safety

- Uses only dummy example data
- Contains no credentials or external integrations
