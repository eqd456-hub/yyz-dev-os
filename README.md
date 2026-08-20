# YYZ Dev OS

YYZ Dev OS is an on-demand, project-independent engineering governance Skill. Version `2.0.0` preserves durable recovery, evidence, security, Git, review, and promotion controls while keeping ordinary low-risk development lightweight.

## Invoke

- Explicitly: `Use $yyz-dev-os to bootstrap this project.`
- Recover existing work: `Use $yyz-dev-os to recover this project, verify its actual state, and tell me the next step.`
- Govern a risky delivery: `Use $yyz-dev-os to apply the relevant security, evidence, review, or promotion gates.`

The Skill may trigger automatically when a task involves durable recovery, data/security risk, high-risk Git or deployment, shared core/orchestrator core, major architecture, trusted evidence, independent review, or promotion. Routine bugs, UI work, prompts, and small local features should follow the project's concise `AGENTS.md` without loading full governance.

## Adopt in a project

Copy the JSON templates from `assets/templates/` into `<project>/.aidev/`, replace placeholders, and validate the recovery entry against `assets/schemas/recovery-entry.schema.json`. Record `globalSkill: yyz-dev-os` and the actually loaded compatible version. Do not overwrite accepted project facts.

## Validate and upgrade

Run `scripts/validate_skill.py`, then the installed Skill loader validator. Apply PATCH and backward-compatible MINOR releases only after project compatibility validation. Require explicit migration for every MAJOR release. Update `VERSION` and `CHANGELOG.md` together; commit and back up only through the Skill's independent private repository.

All paths in the package are relative or configurable. Project-specific state belongs in Project Brain, never here.
