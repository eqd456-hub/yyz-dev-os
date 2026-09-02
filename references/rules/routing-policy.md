# Routing Policy

## Select from evidence

Represent each capability identity as `Tool + Model + Role`; add environment and version when they materially affect results. Select identities by verified evidence from comparable work, then apply the global decision order: quality, safety, stability, availability/quota, efficiency, cost.

Never bind a tool name permanently to Core, UI, review, or another role. Choose the executor from verified capability and the current task's requirements; change the routing when better project-specific evidence appears.

Do not treat public rankings, vendor claims, or an AI's self-assessment as verified capability. If comparable evidence is absent, state `INSUFFICIENT_EVIDENCE`, use a bounded pilot, and measure the result.

## Preferred Codex orchestration profile

The project orchestrator owns requirement understanding, overall solution and decomposition, worker coordination, integration acceptance, and final reporting.

Keep the current preferred model mapping in this policy rather than embedding model names in role definitions or protocols:

| Role | Preferred model profile |
| --- | --- |
| `PROJECT_ORCHESTRATOR` | GPT-5.6 Sol, high reasoning |
| `MODULE_ORCHESTRATOR` | GPT-5.6 Sol, high reasoning |
| `EXPLORER` | GPT-5.6 Luna, low reasoning |
| `IMPLEMENTER` | GPT-5.6 Terra, medium or high reasoning |
| `STANDARD_REVIEWER` | GPT-5.6 Terra, medium or high reasoning |
| `CRITICAL_REVIEWER` | GPT-5.6 Sol, high or xhigh reasoning |

This table is a capability-informed default, not a permanent vendor binding. Override it when verified Global or Project Capability Ledger evidence, availability, or the current risk supports a better identity; preserve the logical role and its authority boundary.

Before substantial execution, perform one brief routing check. For a bounded, independent stage, delegation is the default when it materially improves speed, context quality, quality assurance, or cost:

- Route search, code maps, call chains, logs, documentation, batch inspection, and read-only audit to `EXPLORER`.
- Route bounded features, bug fixes, UI changes, interfaces, tests, and limited refactoring to `IMPLEMENTER`.
- Route ordinary diff, missing-test, and maintainability review to `STANDARD_REVIEWER`.
- Keep architecture, permissions, security, data migration, cross-module coordination, major refactoring, and difficult failures under `PROJECT_ORCHESTRATOR`; use `CRITICAL_REVIEWER` when independent critical review is required.

When the orchestration interface supports explicit model or role selection, request the intended identity explicitly; do not assume an unlabeled worker uses the preferred model. The project orchestrator may keep a stage direct only when it is a trivial one-step action, cannot be separated safely, would create a same-worktree write conflict, lacks an available suitable executor, or costs more to delegate than to perform. The responsible orchestrator must inspect worker evidence before accepting a result. Never allow multiple agents to write the same worktree.

## Minimize total workflow tokens

Optimize total context and avoided rework across the primary agent, advisors, and workers; do not count moving usage to another model as a saving. Keep one owner for the complete technical plan. Pass requirement deltas, authoritative file locations, evidence pointers, constraints, and acceptance criteria instead of repeating stable rules, full code, full logs, or complete project history. Each executor reads only the real artifacts needed for its bounded stage and returns a compact evidence-bearing handoff.

Use an additional model only when the expected reduction in rereading, duplicated reasoning, or later rework exceeds its handoff and verification cost. Do not ask multiple models to independently produce full plans by default.

## Optional ChatGPT planning advisor

Use an existing callable ChatGPT planning advisor only for a non-trivial architecture or cross-module decision where multiple viable approaches exist, a wrong choice would cause material rework, and a compact sanitized brief is sufficient. The consultation must be within granted authority; do not create a user-owned task automatically, assume a subscription tier or model identity, or block the task when no suitable advisor is available.

Send one bounded consultation by default. Include only the goal, observed project facts and evidence locations, constraints, decision questions, and desired compact output. Never send secrets, credentials, private user data, full repository context, or unrelated project history. Ask for alternatives, a recommendation, major risks, and unknowns—not implementation or external actions.

The project orchestrator must validate the advice against real code, Git facts, and project rules, then accept, modify, or reject it. The advisor never owns the final plan. Skip the consultation when its identity or availability is unverified, the context cannot be shared safely, the brief would be large, the task is ordinary, or coordination is unlikely to prevent enough rework. Report `INSUFFICIENT_EVIDENCE` rather than claiming token savings until a bounded pilot measures total tokens, latency, quality, and rework.

## Make routing observable

When a worker or planning advisor is used, include one compact `Routing` line in the final report with the actual model or agent identity, role, bounded objective, and acceptance result. If a stage was clearly eligible for delegation or consultation but remained direct, use that line to state the reason. Omit it for ordinary tasks where routing was not applicable; do not create user-owned tasks merely to make internal routing visible.

These are current preferred profiles, not permanent vendor bindings. Adjust them when verified capability evidence, current availability, or task risk requires a different executor.

## Capability ledger contract

Support two layers without requiring a complex platform:

- Global Capability Ledger: cross-project verified history.
- Project Capability Ledger: performance in the current project's domain, repository, constraints, and role.

Store observations with identity, task class, scope, environment, evidence location, verification status, outcome, date, and limitations. Never invent a numeric score without evidence and a defined scoring method.

Use global evidence as a prior. Increase the weight of project-specific evidence as it accumulates. Re-route when availability or quota changes, but never weaken required safety or verification gates merely to keep an execution path active.
