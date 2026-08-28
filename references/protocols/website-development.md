# Website Development Protocol

Use this protocol for a new long-lived website, a major website phase or cross-module capability, or an explicit website-planning request. It does not apply to an ordinary website bug, UI adjustment, or local feature; use the daily or professional implementation flow for those.

## Establish the current phase before building

For a new website or major phase, first establish the intended audience, product goal, core functions, non-goals, and acceptance conditions. Update an existing project product document when one exists; do not create a duplicate PRD merely to satisfy this protocol.

Map the relevant pages and user journeys: roles and authorization, navigation, critical interactions, and loading, empty, error, responsive, and accessibility states. For new projects or a material direction change, inspect the supported stack first, then define only the needed frontend, backend, data store, file storage, authentication, APIs, deployment boundary, module ownership, data/interface contracts, security controls, and environment-variable handling. The user decides product outcomes; choose ordinary technical details from observed project facts.

## Build in safe increments

Create only the smallest skeleton needed for the current phase, including applicable environment validation, tests, logging, and error handling. Do not speculate by creating a large directory tree or unused service layers.

Before broad feature work, make one real end-to-end vertical slice run through the intended path. Then add bounded modules in sequence: requirement delta, data/API contract, UI states, implementation, risk-matched tests, and project-authorized integration or handoff. Keep each business rule owned by one authoritative module; reuse existing capability before adding another path.

Use [Implementation](implementation.md) for code-level lifecycle details and [Verification Policy](../rules/verification-policy.md) for risk-matched checks. Independent review remains risk-triggered, not a per-module default.

## Prepare and release proportionately

Before a deployment or production release, inspect only applicable concerns: staging, configuration, domain/TLS, permissions and secrets, backup/migration/rollback, upload or payment boundaries, error pages, logs, performance, and accessibility. Load the relevant security, Git, verification, and promotion rules rather than duplicating them here.

Bind a release to the project-required verified commit or artifact. Semantic versioning, tags, and rollback follow project rules; do not create them automatically. Later iterations repeat the smallest applicable daily or professional flow.

## Approval boundary

For a new website or major cross-module direction, form a concise product-phase plan before broad construction. Pause for confirmation only when the user explicitly asks for plan-first, the product boundary is materially unresolved, or a risk gate applies. When direct implementation is clearly authorized, do not repeatedly ask the user to decide normal low-level technical choices.
