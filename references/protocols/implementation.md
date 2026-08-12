# Implementation Protocol

1. Complete Project Recovery and confirm the authorized objective.
2. Convert intent into bounded scope, acceptance criteria, protected invariants, required evidence, and rollback/recovery conditions.
3. Observe the Base and preserve unrelated user changes.
4. For material work, create or use one managed isolated worktree. Assign at most one writer.
5. Implement the smallest coherent change. Do not expand scope silently.
6. Run project-required static, behavioral, safety, core, and build checks in the required order.
7. Inspect the diff for substantive work, unintended files, generated artifacts, secrets, hard-coded machine paths, and policy violations.
8. Create a traceable Candidate bound to Base only after local verification is complete enough for review.
9. Produce an Implementation Report containing objective, identity (`Tool + Model + Role`), Base, Candidate, changed scope, checks and results, evidence, deviations, risks, and unverified items.
10. Hand the Candidate to independent review. Do not call it accepted.

If a check cannot run, preserve the exact limitation and stop before any gate that requires it. Never convert availability problems into a pass.
