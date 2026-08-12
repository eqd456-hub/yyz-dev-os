# Verification Policy

## Define proof before execution

Translate the request into observable acceptance criteria, required checks, protected invariants, and evidence locations before material implementation. Distinguish:

- Static correctness: types, linting, schema, policy, and build checks.
- Behavioral correctness: tests and reproducible scenarios.
- Feature completeness: every accepted requirement and edge case is accounted for.
- Safety correctness: permissions, secrets, destructive behavior, data migration, rollback, and production boundaries.
- Delivery correctness: the verified commit and artifacts are the exact candidate under review.

Passing a subset of checks proves only that subset. Record skipped, unavailable, flaky, degraded, or untrusted checks explicitly. Never report full completion from partial evidence.

## Evidence requirements

Bind evidence to the candidate identity, command or procedure, environment, time, exit/result, and relevant output. Prefer deterministic and reproducible evidence. Treat mutable local artifacts as untrusted if the environment can modify them unexpectedly; do not bypass enterprise controls to recover trust.

Re-observe critical Git facts before acceptance and promotion. Independently review material changes. Verify repairs against the original finding and run regression checks appropriate to the affected surface.
