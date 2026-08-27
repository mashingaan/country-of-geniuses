"""Validate public problem cards against the repository JSON Schema."""

from __future__ import annotations

import argparse
import copy
import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "problem-card.schema.json"
EXAMPLE_PATH = ROOT / "examples" / "problem-card.example.json"
BOSTON_EXAMPLE_PATH = ROOT / "examples" / "boston-open311-damaged-sign.json"
SAN_FRANCISCO_EXAMPLE_PATH = ROOT / "examples" / "san-francisco-muni-elevator.json"
REQUIRED_FILES = (
    "README.md",
    "AGENTS.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "docs/trust-and-safety.md",
    "skills/civic-problem-triage/SKILL.md",
    "skills/open311-read-only-discovery/SKILL.md",
    "skills/russian-public-service-routing/SKILL.md",
    "schemas/problem-card.schema.json",
    "examples/problem-card.example.json",
    "examples/boston-open311-damaged-sign.json",
    "examples/san-francisco-muni-elevator.json",
    "jurisdictions/us/boston/README.md",
    "jurisdictions/us/san-francisco/README.md",
    "jurisdictions/ru/README.md",
    "jurisdictions/registry.yaml",
    "docs/runs/boston-open311-2026-08-27.md",
    "docs/runs/san-francisco-muni-elevator-2026-08-27.md",
    "assets/branding/README.md",
    "assets/branding/country-of-geniuses-logo-v1.png",
    "assets/branding/country-of-geniuses-avatar-v1.png",
    "assets/branding/logo-prompts-v1.md",
    ".github/ISSUE_TEMPLATE/signal.yml",
    "docs/community.md",
    "docs/agent-runbook.md",
    "docs/research/russia-public-service-entrypoints-2026-08-27.md",
    "integrations/catalog.yaml",
    ".gitignore",
)


def load_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"Expected an object in {path}")
    return value


def error_location(error: Any) -> str:
    path = ".".join(str(part) for part in error.absolute_path)
    return path or "<root>"


def validate_card(validator: Draft202012Validator, card: dict[str, Any]) -> list[Any]:
    return sorted(validator.iter_errors(card), key=lambda error: list(error.absolute_path))


def require_valid(validator: Draft202012Validator, label: str, card: dict[str, Any]) -> None:
    errors = validate_card(validator, card)
    if errors:
        details = " | ".join(f"{error_location(error)}: {error.message}" for error in errors)
        raise AssertionError(f"{label} should be valid: {details}")
    print(f"Valid card: {label}")


def require_invalid(validator: Draft202012Validator, label: str, card: dict[str, Any]) -> None:
    errors = validate_card(validator, card)
    if not errors:
        raise AssertionError(f"{label} should be rejected")
    print(f"Rejected invalid card: {label} with {len(errors)} schema error(s)")


def run_regressions(validator: Draft202012Validator, example: dict[str, Any]) -> None:
    invalid_status = copy.deepcopy(example)
    invalid_status["status"] = "bogus"
    require_invalid(validator, "invalid status", invalid_status)

    empty_evidence = copy.deepcopy(example)
    empty_evidence["evidence"] = []
    require_invalid(validator, "empty evidence", empty_evidence)

    missing_jurisdiction = copy.deepcopy(example)
    missing_jurisdiction["status"] = "candidate"
    missing_jurisdiction.pop("jurisdiction")
    require_invalid(validator, "candidate without jurisdiction", missing_jurisdiction)

    discarded_without_reason = copy.deepcopy(example)
    discarded_without_reason["status"] = "discarded"
    discarded_without_reason.pop("responsible_service")
    discarded_without_reason.pop("action")
    require_invalid(validator, "discarded without stop reason", discarded_without_reason)

    closed_without_verification = copy.deepcopy(example)
    closed_without_verification["status"] = "closed"
    closed_without_verification["outcome"] = {
        "public_note": "The service status was not independently verified.",
        "verified_by": "not_verified",
        "verified_at": "2026-08-27T10:00:00Z",
    }
    require_invalid(validator, "closed with not_verified outcome", closed_without_verification)

    discarded = copy.deepcopy(example)
    discarded["status"] = "discarded"
    discarded.pop("responsible_service")
    discarded.pop("action")
    discarded["stop_reason"] = {
        "category": "no_route",
        "reason": "The responsible public service could not be established from official sources.",
    }
    require_valid(validator, "discarded with structured stop reason", discarded)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--card",
        type=Path,
        help="Validate one card instead of the repository example",
    )
    parser.add_argument(
        "--skip-regressions",
        action="store_true",
        help="Skip built-in invalid and status-branch regression cases",
    )
    args = parser.parse_args()

    missing = [path for path in REQUIRED_FILES if not (ROOT / path).is_file()]
    if missing:
        raise FileNotFoundError("Missing required file(s): " + ", ".join(missing))

    schema = load_json(SCHEMA_PATH)
    example = load_json(EXAMPLE_PATH)
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())

    if args.card:
        card_path = (ROOT / args.card).resolve()
        card = load_json(card_path)
        require_valid(validator, str(card_path.relative_to(ROOT)), card)
    else:
        require_valid(validator, str(EXAMPLE_PATH.relative_to(ROOT)), example)
        require_valid(validator, str(BOSTON_EXAMPLE_PATH.relative_to(ROOT)), load_json(BOSTON_EXAMPLE_PATH))
        require_valid(validator, str(SAN_FRANCISCO_EXAMPLE_PATH.relative_to(ROOT)), load_json(SAN_FRANCISCO_EXAMPLE_PATH))

    if not args.skip_regressions and not args.card:
        run_regressions(validator, example)

    print("Country of Geniuses JSON Schema checks passed")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as error:
        print(f"Validation failed: {error}", file=sys.stderr)
        raise SystemExit(1)
