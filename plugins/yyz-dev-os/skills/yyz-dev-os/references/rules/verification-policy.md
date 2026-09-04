# Verification Policy

## Define proof before execution

Match verification depth to the change's scope and risk. For ordinary low-risk work, run the targeted tests and static/build checks needed to establish the requested behavior. Use the complete categories below when a high-risk task, protected surface, release gate, or explicit acceptance contract requires them.

After every code change, inspect the final diff and self-check for duplicated functionality, broken existing interfaces, business-rule ownership drift, architecture-boundary violations, dead or unnecessary code, debug residue, unsuitable dependencies, extensibility concerns, and whether the change needs new or updated tests. This is implementation-author self-review; do not describe it as Independent Review.

Translate governed work into observable acceptance criteria, required checks, protected invariants, and evidence locations. Distinguish:

- Static correctness: types, linting, schema, policy, and build checks.
- Behavioral correctness: tests and reproducible scenarios.
- Feature completeness: every accepted requirement and edge case is accounted for.
- Safety correctness: permissions, secrets, destructive behavior, data migration, rollback, and production boundaries.
- Delivery correctness: the verified commit and artifacts are the exact candidate under review.

Passing a subset of checks proves only that subset. Record skipped, unavailable, flaky, degraded, or untrusted checks explicitly. Never report full completion from partial evidence.

## Ordinary verification and governed evidence

For ordinary local work, record only the risk-matched checks actually run and their results. Mention a skipped, blocked, or partial check only when it affects the conclusion; do not enumerate every inapplicable category. A passing local check does not become Trusted Evidence merely by being reported.

For governed candidates, delivery gates, or explicit trusted-evidence requests, apply the evidence requirements below. Select the complete categories only when the active risk, protected surface, release gate, or acceptance contract requires them.

## Project-configured high-assurance profiles

A project may declare an optional `high-assurance` profile in validated Project Operating Rules for specific protected surfaces or task classes. The profile is not a global default and does not turn every feature into a release-grade workflow.

When the current task matches the declared scope, apply only the configured requirements. They may include named verification commands, a durable architecture decision or architecture review, Independent Review, documentation updates when affected, Project Brain updates when durable state changes, and proof that the candidate scope contains no unintended files or changes. Candidate-scope cleanliness never authorizes cleaning, stashing, resetting, or overwriting unrelated user work in a dirty worktree.

Missing required evidence blocks only the gate that depends on that profile. Do not run every test category automatically, create an architecture record for ordinary local choices, update unaffected documentation or Project Brain files, or claim that an unconfigured project has opted into `high-assurance`.

## Release-scope verification

- For `A — frontend-only`, verify the frontend behavior, relevant static/build checks, visual or interaction states when applicable, and evidence that no backend/API contract changed. Do not require backend integration testing without an observed dependency.
- For `B — frontend/backend coordinated`, verify the authoritative API contract plus relevant producer, consumer, compatibility, error-path, and end-to-end or integration behavior across the affected modules.
- For `C — architecture-changing`, run the complete integration suite declared for the affected architecture boundaries, verify protected invariants and rollback conditions, and satisfy any required architecture decision, critical review, or promotion gate.

Release-scope completeness means complete evidence for the affected boundary, not an automatic whole-repository test run. A failed or unavailable required check cannot be downgraded by relabeling the release scope.

## Evidence requirements

Bind evidence to the candidate identity, command or procedure, environment, time, exit/result, and relevant output. Prefer deterministic and reproducible evidence. Treat mutable local artifacts as untrusted if the environment can modify them unexpectedly; do not bypass enterprise controls to recover trust.

Reuse trustworthy validation evidence when its code, configuration, environment, and relevant state have not changed. Do not repeat a complete investigation merely for reassurance. Never use prior evidence to skip tests required by the current modification.

Re-observe critical Git facts before acceptance and promotion. Require independent review only when requested, risk-justified, or mandated by an accepted project gate. Verify repairs against the original finding and run regression checks appropriate to the affected surface.
