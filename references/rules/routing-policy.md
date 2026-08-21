# Routing Policy

## Select from evidence

Represent each capability identity as `Tool + Model + Role`; add environment and version when they materially affect results. Select identities by verified evidence from comparable work, then apply the global decision order: quality, safety, stability, availability/quota, efficiency, cost.

Never bind a tool name permanently to Core, UI, review, or another role. Choose the executor from verified capability and the current task's requirements; change the routing when better project-specific evidence appears.

Do not treat public rankings, vendor claims, or an AI's self-assessment as verified capability. If comparable evidence is absent, state `INSUFFICIENT_EVIDENCE`, use a bounded pilot, and measure the result.

## Preferred Codex orchestration profile

The primary agent owns requirement understanding, overall solution and decomposition, worker coordination, result acceptance, and final reporting. Prefer GPT-5.6 Sol with high reasoning for that role.

Delegate only bounded, independent work when doing so materially improves speed, context quality, or cost:

- Prefer GPT-5.6 Luna with low reasoning for narrow search, discovery, extraction, classification, and log triage.
- Prefer GPT-5.6 Terra with medium or high reasoning for scoped implementation, fixes, and test work.
- Prefer GPT-5.6 Sol with high or xhigh reasoning for difficult architecture, security work, and independent review.

The primary agent must inspect worker evidence before accepting a result. Do not delegate a trivial one-step action when delegation costs more than performing it directly. Never allow multiple agents to write the same worktree.

These are current preferred profiles, not permanent vendor bindings. Adjust them when verified capability evidence, current availability, or task risk requires a different executor.

## Capability ledger contract

Support two layers without requiring a complex platform:

- Global Capability Ledger: cross-project verified history.
- Project Capability Ledger: performance in the current project's domain, repository, constraints, and role.

Store observations with identity, task class, scope, environment, evidence location, verification status, outcome, date, and limitations. Never invent a numeric score without evidence and a defined scoring method.

Use global evidence as a prior. Increase the weight of project-specific evidence as it accumulates. Re-route when availability or quota changes, but never weaken required safety or verification gates merely to keep an execution path active.
