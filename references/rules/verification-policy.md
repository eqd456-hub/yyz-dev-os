# Verification Policy

## Define proof before execution

Match verification depth to the change's scope and risk. For ordinary low-risk work, run the targeted tests and static/build checks needed to establish the requested behavior. Use the complete categories below when a high-risk task, protected surface, release gate, or explicit acceptance contract requires them.

After ordinary code changes, self-check for duplicated functionality, broken existing interfaces, architecture-boundary violations, dead or unnecessary code, and whether the change needs new or updated tests.

Translate governed work into observable acceptance criteria, required checks, protected invariants, and evidence locations. Distinguish:

- Static correctness: types, linting, schema, policy, and build checks.
- Behavioral correctness: tests and reproducible scenarios.
- Feature completeness: every accepted requirement and edge case is accounted for.
- Safety correctness: permissions, secrets, destructive behavior, data migration, rollback, and production boundaries.
- Delivery correctness: the verified commit and artifacts are the exact candidate under review.

Passing a subset of checks proves only that subset. Record skipped, unavailable, flaky, degraded, or untrusted checks explicitly. Never report full completion from partial evidence.

## Evidence requirements

Bind evidence to the candidate identity, command or procedure, environment, time, exit/result, and relevant output. Prefer deterministic and reproducible evidence. Treat mutable local artifacts as untrusted if the environment can modify them unexpectedly; do not bypass enterprise controls to recover trust.

Reuse trustworthy validation evidence when its code, configuration, environment, and relevant state have not changed. Do not repeat a complete investigation merely for reassurance. Never use prior evidence to skip tests required by the current modification.

Re-observe critical Git facts before acceptance and promotion. Require independent review only when requested, risk-justified, or mandated by an accepted project gate. Verify repairs against the original finding and run regression checks appropriate to the affected surface.
