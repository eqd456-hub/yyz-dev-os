#!/usr/bin/env python3
"""Regression tests for observed YYZ behavior-result validation."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import validate_behavior_cases as validator  # noqa: E402


class ObservedResultsValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.suite = validator.load_json(validator.DEFAULT_SUITE)

    def results(self, *, exact_booleans: bool = True, valid_lists: bool = True) -> dict:
        items = []
        for case in self.suite["cases"]:
            expected = case["expected"]
            items.append(
                {
                    "id": case["id"],
                    "observed": {
                        "mode": expected["mode"],
                        "pausedBeforeImplementation": (
                            expected["mustPauseBeforeImplementation"]
                            if exact_booleans
                            else True
                        ),
                        "protectedApprovalRequested": (
                            expected["requiresProtectedApproval"]
                            if exact_booleans
                            else True
                        ),
                        "loadedReferences": (
                            expected["requiredReferences"] if valid_lists else "invalid"
                        ),
                        "performedActions": [] if valid_lists else "invalid",
                    },
                }
            )
        return {"results": items}

    def validate(self, results: dict) -> list[str]:
        with patch.object(
            validator, "load_json", side_effect=[self.suite, results]
        ):
            return validator.validate_results(
                validator.DEFAULT_SUITE, validator.DEFAULT_SUITE
            )

    def test_exact_results_pass(self) -> None:
        self.assertEqual(self.validate(self.results()), [])

    def test_over_governance_fails(self) -> None:
        failures = self.validate(self.results(exact_booleans=False))
        self.assertTrue(
            any("pausedBeforeImplementation" in failure for failure in failures)
        )
        self.assertTrue(
            any("protectedApprovalRequested" in failure for failure in failures)
        )

    def test_malformed_action_lists_fail(self) -> None:
        failures = self.validate(self.results(valid_lists=False))
        self.assertTrue(
            any("loadedReferences must be a string list" in failure for failure in failures)
        )
        self.assertTrue(
            any("performedActions must be a string list" in failure for failure in failures)
        )


if __name__ == "__main__":
    unittest.main()
