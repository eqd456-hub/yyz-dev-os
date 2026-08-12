# Routing Policy

## Select from evidence

Represent each capability identity as `Tool + Model + Role`; add environment and version when they materially affect results. Select identities by verified evidence from comparable work, then apply the global decision order: quality, safety, stability, availability/quota, efficiency, cost.

Do not treat public rankings, vendor claims, or an AI's self-assessment as verified capability. If comparable evidence is absent, state `INSUFFICIENT_EVIDENCE`, use a bounded pilot, and measure the result.

## Capability ledger contract

Support two layers without requiring a complex platform:

- Global Capability Ledger: cross-project verified history.
- Project Capability Ledger: performance in the current project's domain, repository, constraints, and role.

Store observations with identity, task class, scope, environment, evidence location, verification status, outcome, date, and limitations. Never invent a numeric score without evidence and a defined scoring method.

Use global evidence as a prior. Increase the weight of project-specific evidence as it accumulates. Re-route when availability or quota changes, but never weaken required safety or verification gates merely to keep an execution path active.
