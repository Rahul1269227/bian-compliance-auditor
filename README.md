# Dummy BIAN Compliance Auditor

Safe sample project for checking whether an OpenAPI spec loosely follows BIAN-style conventions.

## What It Checks

- Whether `operationId` values start with common BIAN verbs
- Whether the API declares a domain hint
- Whether common data model patterns such as `status`, `reference`, or `record` appear

## Quick Start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
PYTHONPATH=src python -m bian_auditor.cli examples/sample_service.yaml
```
