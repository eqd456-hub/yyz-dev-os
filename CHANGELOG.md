# Changelog

All notable changes to YYZ Dev OS follow Semantic Versioning and the Keep a Changelog categories.

## [2.0.0] - 2026-08-20

### Changed

- Make ordinary low-risk development use a lightweight code-first workflow instead of full governance by default.
- Load recovery, independent review, trusted evidence, SHA verification, promotion, and durable handoff rules only when risk or an accepted project gate requires them.
- Route executors by verified capability and current task rather than fixed tool-name roles.
- Reuse unchanged trustworthy context and evidence, and stop when the scoped request is satisfied and necessary tests pass.

### Security

- Preserve fail-closed behavior, secrets and permission boundaries, data protection, rollback, high-risk Git controls, and promotion gates.

## [1.0.0] - 2026-08-12

### Added

- Global development priorities, truth rules, source authority, AI role and routing policies.
- Project bootstrap, recovery, implementation, independent-review, repair, and handoff protocols.
- Portable project-memory templates and a recovery-entry JSON Schema.
- Deterministic package validation for structure, versioning, JSON, scope separation, paths, and secrets.

### Changed

- None.

### Deprecated

- None.

### Removed

- None.

### Fixed

- None.

### Security

- Prohibit project-specific live state and secrets in the global skill.
