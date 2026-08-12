# YYZ Dev OS

YYZ Dev OS is a global, project-independent AI software development operating system. Version `1.0.0` defines durable rules for project bootstrap and recovery, technical leadership, role routing, verification, Git isolation, memory, storage, approvals, and reporting.

## Invoke

- Explicitly: `Use $yyz-dev-os to bootstrap this project.`
- Recover existing work: `Use $yyz-dev-os to recover this project, verify its actual state, and tell me the next step.`
- Apply to delivery: `Use $yyz-dev-os to implement and verify this change.`

The Skill may also trigger automatically for software-project bootstrap, recovery, implementation, review, repair, release, and related governance work.

## Adopt in a project

Copy the JSON templates from `assets/templates/` into `<project>/.aidev/`, replace placeholders, and validate the recovery entry against `assets/schemas/recovery-entry.schema.json`. Record `globalSkill: yyz-dev-os` and the actually loaded compatible version. Do not overwrite accepted project facts.

## Validate and upgrade

Run `scripts/validate_skill.py`, then the installed Skill loader validator. Apply PATCH and backward-compatible MINOR releases only after project compatibility validation. Require explicit migration for every MAJOR release. Update `VERSION` and `CHANGELOG.md` together; commit and back up only through the Skill's independent private repository.

All paths in the package are relative or configurable. Project-specific state belongs in Project Brain, never here.
