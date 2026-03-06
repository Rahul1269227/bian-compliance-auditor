from pathlib import Path

from bian_auditor.auditor import audit_spec


BASE_DIR = Path(__file__).resolve().parents[1]


def test_sample_service_is_marked_compliant() -> None:
    result = audit_spec(BASE_DIR / "examples" / "sample_service.yaml")

    assert result["compliant"] is True
    assert result["score"] == 100
    assert result["issues"] == []


def test_non_bian_style_operation_lowers_score(tmp_path: Path) -> None:
    spec_path = tmp_path / "bad_service.yaml"
    spec_path.write_text(
        """
openapi: 3.0.3
info:
  title: Bad Service
  version: 1.0.0
paths:
  /items:
    get:
      operationId: getItems
      responses:
        "200":
          description: ok
components:
  schemas:
    Item:
      type: object
      properties:
        value:
          type: string
""".strip(),
        encoding="utf-8",
    )

    result = audit_spec(spec_path)

    assert result["compliant"] is False
    assert result["score"] < 70
    assert result["issues"]
