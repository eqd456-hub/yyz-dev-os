# Project Bootstrap Protocol

Use this bootstrap for a new long-lived project that needs durable recovery/governance, or when explicitly requested. Do not block a small experiment or routine local edit on creating the full governance structure.

1. Identify the project: define `projectId`, `projectName`, repository identity, configured storage root binding, and owners.
2. Observe or initialize Git safely. Define the stable/default branch without assuming its name.
3. Create `.aidev/`. Copy each `assets/templates/<name>.template.json` to `.aidev/<name>.json`; do not retain the `.template` segment in the project filename.
4. Replace every placeholder; never copy project facts from another repository.
5. Populate the recovery entry's `bindings`: define the architecture record and set checkpoint, evidence-index, and Global/Project Capability Ledger paths when used; leave an unused optional binding as `null`.
6. Record `globalSkill: yyz-dev-os`, the actually loaded compatible version, recovery order, and authority order.
7. Set `doNotUseChatMemoryAsProjectTruth` to `true`.
8. Validate `recovery-entry.json` with this Skill's bundled schema. Define project-owned schemas or deterministic validators for Operating Rules and every authoritative Project Brain record; do not treat a template as validated state merely because its JSON parses.
9. Validate JSON, schema versions, repository-relative paths, path traversal protections, and absence of secrets. Define project-specific verification commands, protected surfaces, worktree/candidate flow, approval gates, release rules, and data migration/rollback rules.
10. Observe Git again, create the initial trusted checkpoint only from evidence, and report unresolved items as unknown or unverified.

Do not mark bootstrap complete until a new AI can follow `recovery-entry.json` without chat history and reconstruct an evidence-bounded Recovery Context.
