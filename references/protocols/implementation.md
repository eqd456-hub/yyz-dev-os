# Implementation Protocol

## Ordinary low-risk work

1. Understand the request and read the directly related code, tests, and configuration.
2. Choose the technical solution, fix the root cause, and keep scope bounded.
3. Preserve stable unrelated modules and user changes.
4. Implement the smallest coherent change.
5. Run tests and checks proportional to the affected behavior and risk.
6. Stop when the request is satisfied, necessary checks pass, and no major unresolved risk remains. Report what changed, verification, and risk.

## Governed work

When a recovery, security/data, protected Git, deployment/promotion, shared-core/orchestrator-core, major architecture, trusted-evidence, or independent-review trigger applies:

1. Complete only the recovery needed to establish authoritative inputs and confirm the authorized objective.
2. Define bounded scope, acceptance criteria, protected invariants, required evidence, and rollback/recovery conditions.
3. Observe the Base and preserve unrelated user changes.
4. Create or use one managed isolated worktree when the project gate or risk requires it. Assign at most one writer.
5. Implement the smallest coherent change without expanding scope silently.
6. Run the required static, behavioral, safety, core, and build checks for the affected gate.
7. Inspect the diff for unintended files, generated artifacts, secrets, hard-coded machine paths, and policy violations.
8. Create a traceable Candidate bound to Base only when review or promotion requires it.
9. Produce the evidence/handoff required by the active gate and invoke independent review only when required.

If a check cannot run, preserve the exact limitation and stop before any gate that requires it. Never convert availability problems into a pass.
