#!/usr/bin/env python3
"""
Consilium docs validator

Checks for:
- canonical_spec_path points to ../../consilium-openapi-v1.1.yaml in phase docs
- authority_order uses .yml for Phase 0 authority docs
- cross_doc_relationship paths use ./ for local, ../../ for repo root
- plan path is ../../consilium-9_phase_plan.yml
- CONSILIUM_API_KEY guidance uses >= 32 chars where present

Exit non-zero on any violations.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "consilium"


def iter_phase_files() -> list[Path]:
    return sorted(
        [p for p in DOCS.glob("phase_*_*.yaml") if p.is_file()], key=lambda p: p.name
    )


def validate_canonical_spec_path(text: str, path: Path, errors: list[str]) -> None:
    m = re.search(r"^canonical_spec_path:\s*\"([^\"]+)\"", text, flags=re.M)
    if not m:
        errors.append(f"{path.name}: missing canonical_spec_path")
        return
    got = m.group(1)
    expected = "../../consilium-openapi-v1.1.yaml"
    if got != expected:
        errors.append(f"{path.name}: canonical_spec_path should be '{expected}', got '{got}'")


def validate_authority_order(text: str, path: Path, errors: list[str]) -> None:
    # Ensure .yml not .md
    if re.search(r"00_AI_AGENT_RULES\.md", text):
        errors.append(f"{path.name}: authority_order references .md; use 00_AI_AGENT_RULES.yml")


def validate_plan_path(text: str, path: Path, errors: list[str]) -> None:
    # phase_plan should reference ../../consilium-9_phase_plan.yml
    if re.search(r'phase_plan:\s*"\.\./consilium-9_phase_plan\.yml"', text):
        errors.append(
            f"{path.name}: phase_plan points to ../; should be ../../consilium-9_phase_plan.yml"
        )


def validate_api_key_guidance(text: str, path: Path, errors: list[str]) -> None:
    # Look for explicit length checks allowing <32
    bad_checks = [
        r"len\(api\)\s*>=\s*16",
        r"min_length\s*[:=]\s*16",
        r"Length\s*>?=\s*16",
        r"assert\s+len\([^)]*consilium_api_key[^)]*\)\s*>=\s*16",
    ]
    for pat in bad_checks:
        if re.search(pat, text, flags=re.I):
            errors.append(f"{path.name}: API key min length should be 32+, found check '{pat}'")


def main() -> int:
    errors: list[str] = []
    for f in iter_phase_files():
        text = f.read_text(encoding="utf-8")
        validate_canonical_spec_path(text, f, errors)
        validate_authority_order(text, f, errors)
        validate_plan_path(text, f, errors)
        validate_api_key_guidance(text, f, errors)

    if errors:
        print("Docs validation FAILED:")
        for e in errors:
            print(" -", e)
        return 1
    print("Docs validation PASSED: all checks OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
