# Source of Truth

## Authority order

Resolve project facts in this order:

1. Observed Git facts
2. Validated project operating rules
3. Accepted Project Brain
4. Verified execution and review evidence
5. Trusted checkpoint
6. Verified capability ledger
7. Runtime memory
8. Chat or AI self-report

Use live observations only for the facts they can actually prove. For example, Git can prove commits, ancestry, refs, diffs, and working-tree state; it cannot prove that a user-facing behavior meets an unstated requirement.

## Permanent truth rules

- AI self-report is not truth.
- Reported complete is not verified complete.
- Passing tests is not feature complete.
- A diff is not substantive work by itself.
- A reviewer report is not automatically a verified finding.
- A model rating is not verified performance.

## Conflict handling

Never silently merge or overwrite conflicting facts. Record the competing claims, their provenance, scope, freshness, and authority. Prefer the higher-authority fact; if authorities are equal, prefer direct and reproducible evidence, otherwise mark the fact `UNVERIFIED`.

Treat a project-local proposal as proposed state until the project's acceptance process promotes it. Treat generated summaries as views, not independent truth sources.

Reference authoritative engineering files rather than copying stable rules, architecture, or project facts into every prompt. Send only the current requirement delta unless the referenced source is unavailable or disputed.
