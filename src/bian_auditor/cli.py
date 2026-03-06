from __future__ import annotations

import argparse
import json

from bian_auditor.auditor import audit_spec


def main() -> None:
    parser = argparse.ArgumentParser(description="Audit an OpenAPI spec for BIAN-style conventions.")
    parser.add_argument("spec_path")
    args = parser.parse_args()
    print(json.dumps(audit_spec(args.spec_path), indent=2))


if __name__ == "__main__":
    main()
