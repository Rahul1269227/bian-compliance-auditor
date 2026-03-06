# BIAN Compliance Auditor

![Python](https://img.shields.io/badge/python-3.11%2B-blue)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-green)

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

## Demo

This repo works as a simple standards-checking sample. Run the CLI against the included OpenAPI file to get a JSON summary with a compliance score, issues, and the operations that were evaluated.

## Project Layout

- `src/bian_auditor`: compliance checks and CLI
- `examples/`: neutral sample OpenAPI document
- `tests/`: unit tests for compliant and non-compliant cases

## Safety

- Uses only dummy example data
- Contains no credentials or external integrations
