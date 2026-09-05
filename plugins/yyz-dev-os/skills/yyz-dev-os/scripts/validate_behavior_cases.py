#!/usr/bin/env python3
"""Validate YYZ Dev OS routing cases and optional observed behavior results."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SUITE = ROOT / "tests" / "behavior-cases.json"
VALID_MODES = {"daily", "plan-first", "professional", "governed"}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_suite(path: Path = DEFAULT_SUITE) -> tuple[list[str], dict[str, int]]:
    failures: list[str] = []
    counts = {mode: 0 for mode in sorted(VALID_MODES)}
    try:
        suite = load_json(path)
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        return [f"Invalid behavior suite: {exc}"], counts

    if not isinstance(suite, dict) or suite.get("schemaVersion") != 1:
        failures.append("Behavior suite schemaVersion must be 1")
        return failures, counts
    cases = suite.get("cases")
    if not isinstance(cases, list) or not cases:
        failures.append("Behavior suite must contain a non-empty cases list")
        return failures, counts

    seen_ids: set[str] = set()
    for index, case in enumerate(cases):
        label = f"cases[{index}]"
        if not isinstance(case, dict):
            failures.append(f"{label} must be an object")
            continue
        case_id = case.get("id")
        if not isinstance(case_id, str) or not case_id.strip():
            failures.append(f"{label}.id must be a non-empty string")
            continue
        label = case_id
        if case_id in seen_ids:
            failures.append(f"Duplicate behavior case id: {case_id}")
        seen_ids.add(case_id)
        if not isinstance(case.get("prompt"), str) or not case["prompt"].strip():
            failures.append(f"{label}.prompt must be a non-empty string")

        expected = case.get("expected")
        if not isinstance(expected, dict):
            failures.append(f"{label}.expected must be an object")
            continue
        mode = expected.get("mode")
        if mode not in VALID_MODES:
            failures.append(f"{label}.expected.mode is invalid: {mode!r}")
        else:
            counts[mode] += 1
        for key in ("mustPauseBeforeImplementation", "requiresProtectedApproval"):
            if not isinstance(expected.get(key), bool):
                failures.append(f"{label}.expected.{key} must be boolean")
        for key in ("requiredReferences", "requiredActions", "forbiddenDefaultActions", "forbiddenReferences"):
            values = expected.get(key, []) if key in ("requiredActions", "forbiddenReferences") else expected.get(key)
            if not isinstance(values, list) or any(
                not isinstance(value, str) or not value.strip() for value in values
            ):
                failures.append(f"{label}.expected.{key} must be a string list")
                continue
            if len(values) != len(set(values)):
                failures.append(f"{label}.expected.{key} contains duplicates")
        for relative in expected.get("requiredReferences", []):
            if isinstance(relative, str) and not (ROOT / relative).is_file():
                failures.append(f"{label} requires missing reference: {relative}")

    missing_modes = sorted(mode for mode, count in counts.items() if count == 0)
    if missing_modes:
        failures.append(f"Behavior suite does not cover modes: {', '.join(missing_modes)}")
    return failures, counts


def validate_results(suite_path: Path, results_path: Path) -> list[str]:
    failures: list[str] = []
    suite = load_json(suite_path)
    results = load_json(results_path)
    if not isinstance(results, dict) or not isinstance(results.get("results"), list):
        return ["Observed results must be an object containing a results list"]

    observed_by_id: dict[str, dict[str, Any]] = {}
    for item in results["results"]:
        if not isinstance(item, dict) or not isinstance(item.get("id"), str):
            failures.append("Every observed result must contain a string id")
            continue
        if item["id"] in observed_by_id:
            failures.append(f"Duplicate observed result id: {item['id']}")
            continue
        observed = item.get("observed")
        if not isinstance(observed, dict):
            failures.append(f"{item['id']}.observed must be an object")
            continue
        observed_by_id[item["id"]] = observed

    for case in suite["cases"]:
        case_id = case["id"]
        expected = case["expected"]
        observed = observed_by_id.get(case_id)
        if observed is None:
            failures.append(f"Missing observed result: {case_id}")
            continue
        if observed.get("mode") != expected["mode"]:
            failures.append(
                f"{case_id}: expected mode {expected['mode']!r}, got {observed.get('mode')!r}"
            )
        for expected_key, observed_key in (
            ("mustPauseBeforeImplementation", "pausedBeforeImplementation"),
            ("requiresProtectedApproval", "protectedApprovalRequested"),
        ):
            observed_value = observed.get(observed_key)
            if not isinstance(observed_value, bool):
                failures.append(f"{case_id}.{observed_key} must be boolean")
            elif observed_value != expected[expected_key]:
                failures.append(
                    f"{case_id}: expected {observed_key}={expected[expected_key]!r}, "
                    f"got {observed_value!r}"
                )

        loaded_values = observed.get("loadedReferences")
        if not isinstance(loaded_values, list) or any(
            not isinstance(value, str) or not value.strip() for value in loaded_values
        ):
            failures.append(f"{case_id}.loadedReferences must be a string list")
            loaded_values = []
        loaded = set(loaded_values)
        missing = sorted(set(expected["requiredReferences"]) - loaded)
        if missing:
            failures.append(f"{case_id}: missing required references: {', '.join(missing)}")
        forbidden_references = sorted(set(expected.get("forbiddenReferences", [])) & loaded)
        if forbidden_references:
            failures.append(f"{case_id}: loaded forbidden references: {', '.join(forbidden_references)}")
        performed_values = observed.get("performedActions")
        if not isinstance(performed_values, list) or any(
            not isinstance(value, str) or not value.strip() for value in performed_values
        ):
            failures.append(f"{case_id}.performedActions must be a string list")
            performed_values = []
        performed = set(performed_values)
        missing_actions = sorted(set(expected.get("requiredActions", [])) - performed)
        if missing_actions:
            failures.append(
                f"{case_id}: missing required actions: {', '.join(missing_actions)}"
            )
        forbidden = sorted(set(expected["forbiddenDefaultActions"]) & performed)
        if forbidden:
            failures.append(f"{case_id}: performed forbidden actions: {', '.join(forbidden)}")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--suite", type=Path, default=DEFAULT_SUITE)
    parser.add_argument(
        "--results",
        type=Path,
        help="Optional JSON results captured by an external Codex evaluation runner",
    )
    args = parser.parse_args()

    failures, counts = validate_suite(args.suite)
    if not failures and args.results:
        try:
            failures.extend(validate_results(args.suite, args.results))
        except (OSError, UnicodeError, json.JSONDecodeError) as exc:
            failures.append(f"Invalid observed results: {exc}")

    if failures:
        print("YYZ Dev OS behavior validation FAILED")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("YYZ Dev OS behavior contract validation PASSED")
    print(f"- cases: {sum(counts.values())}")
    print("- modes: " + ", ".join(f"{mode}={counts[mode]}" for mode in sorted(counts)))
    if args.results:
        print("- observed behavior: matched expected routing and safety gates")
    else:
        print("- observed behavior: not run (no external results supplied)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
