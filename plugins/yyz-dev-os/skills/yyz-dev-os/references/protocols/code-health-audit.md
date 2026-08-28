# Code Health Audit Protocol

Use this protocol to establish whether a codebase can continue changing safely. It is an evidence-backed assessment, not an authorization to repair, refactor, change stacks, bulk-upgrade dependencies, or move files.

## Choose the smallest audit

For ordinary work, perform an incremental health check only: inspect the changed files, their direct callers/callees, affected tests, configuration, and the smallest relevant data or security boundary. Do not scan the whole repository merely because code changed.

Run a full audit only when the user explicitly requests it, or evidence shows repeated regressions, modification spread, a large new module, a major version/release, or a durable handoff needs a broader health picture. Scope the audit to the relevant application or subsystem when a full repository audit is unnecessary.

## Assess evidence, not appearances

Assess only dimensions supported by observed code, tests, configuration, Git history, and relevant runtime evidence:

1. Structure and module boundaries.
2. Responsibility, complexity, and change isolation.
3. Duplicate business rules and competing sources of truth.
4. State ownership and state-flow consistency.
5. API, data-layer, configuration, and dependency boundaries.
6. Technical debt that materially impairs safe change.
7. Tests, regression protection, and verification feasibility.
8. Cross-module consistency and modification safety.
9. Security, authorization, secrets, privacy, data integrity, file handling, and rollback boundaries when the inspected surface reaches them.

Do not assign a fabricated precise score. State the inspected scope, evidence coverage, and confidence. Mark a dimension `Not assessed` or `INSUFFICIENT_EVIDENCE` when the available facts do not support a conclusion.

## Report and stop

For every finding, report its evidence location, observed condition, plausible impact, priority, whether it needs action now, and the narrowest corrective direction. Set priority from actual impact, likelihood, security or data exposure, affected users, modification frequency, and whether current work is blocked. A large file, duplicate-looking code, or stylistic concern is not automatically P0 or P1.

Separate assessment from repair. Finish the audit after reporting unless the user separately authorizes a bounded change. Do not expand a current task into cleanup because the audit found unrelated debt.
