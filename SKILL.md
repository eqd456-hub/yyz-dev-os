---
name: yyz-dev-os
description: Use for cross-module development, high-impact refactoring, substantial task delegation or subagent orchestration, module collaboration conflicts, security/data boundaries, recovery, release/promotion, or explicit engineering governance and independent code review. Routine single-owner bug fixing, UI, text and local edits use AGENTS.md without loading this skill unless explicitly requested or an actual risk emerges.
---

# YYZ Dev OS

## Daily fast path — decide before loading references

Small, bounded, reversible work under one responsible owner follows:

`read relevant code and Git state → fix → targeted verification → brief result → stop`

If this entry was loaded for such work, stop reference loading here. Do not default to workers, execution cards, full Project Brain recovery, independent review, capability pilots, release classification, or promotion gates. An explicit YYZ invocation alone does not escalate risk. A module registry, multiple reported symptoms, several changed files, or a task taking more than one step does not by itself make work complex.

For unclear failures, inspect the relevant handler, API call and persistence path first; expand only for a concrete unresolved dependency. A short user request is not proof of low risk. Escalate for observed security/data-boundary changes, migration/deletion, contract changes across owners, major architecture, protected Git/release actions, or an applicable project gate.

For a registered module, route module-owned writes through that module orchestrator. If already in the responsible module task, work directly. Otherwise use one compact assignment to that owner; ownership routing alone does not require the full orchestration protocol. Do not bypass the owner for token savings. Unavailable owners, ambiguous responsibility and writer conflicts still block affected writes until explicitly resolved.

## Keep context and authority bounded

- User owns product intent; the lead owns routine technical decisions. Read real code, reuse existing modules, preserve interfaces and unrelated changes; never lower required tests for a pass.
- Reuse already-read rules and verified evidence while their relevant code, configuration and environment remain unchanged. Read deltas, not repeated full files, histories or logs. One owner diagnoses a bounded issue; delegate only when saved work exceeds setup, duplicated context and acceptance cost.
- Keep one writer per worktree and responsibility. Required security, data, approval and release gates survive the fast path. Separate implementation, verification, independent review, approval and promotion when those gates apply.
- Observed code/Git and validated project rules outrank chat and self-report. A passing test or worker report proves only its covered facts. Never invent evidence, capability or acceptance.
- Keep global rules separate from project facts. Never store a project's current commit, branch, candidate, secrets or chat transcript in this skill.
- Stop after scope and necessary verification are satisfied. Report effect, checks and material remaining risk in a few lines. Quiet self-check adds no routine document or review.

## Load only the triggered reference

Follow a link only when its stated condition is present, not simply because another reference links it. For a validated project `high-assurance` profile, apply its declared scope and required evidence.

| Actual need | Start here |
| --- | --- |
| Non-trivial behavior/contract/architecture change | [Implementation](references/protocols/implementation.md), [Verification](references/rules/verification-policy.md) |
| Plan-first, batched feedback, or authority/product decision | [Approval](references/rules/approval-risk-policy.md); add Implementation for non-trivial work or batched feedback |
| Useful delegation, cross-owner coordination, reassignment or writer conflict | [Orchestration](references/protocols/multi-agent-orchestration.md); add [Roles](references/rules/ai-role-policy.md) and [Routing](references/rules/routing-policy.md) only for executor selection |
| Security, secrets, deletion or data boundaries | [Operating principles](references/rules/operating-principles.md), Approval, [Storage](references/rules/storage-policy.md) |
| Protected Git, actual release/promotion | [Git](references/rules/git-policy.md), Verification; apply API Contract and A/B/C from Implementation when relevant |
| Required independent review / repair | [Independent review](references/protocols/independent-review.md), [Repair loop](references/protocols/repair-loop.md) when needed |
| Missing/conflicting project state or recovery | [Source of truth](references/rules/source-of-truth.md), [Recovery policy](references/rules/recovery-policy.md), [Project recovery](references/protocols/project-recovery.md) |
| Durable handoff or memory update | [Handoff](references/protocols/project-handoff.md), [Memory](references/rules/memory-policy.md) |
| New durable project or major website phase | [Bootstrap](references/protocols/project-bootstrap.md) or [Website development](references/protocols/website-development.md) |
| Requested code-health audit or recurring health failures | [Code health](references/protocols/code-health-audit.md) |
| Managed reporting or explicit process evaluation | [Reporting](references/rules/reporting-policy.md) or [Self-audit](references/rules/self-audit-policy.md) |

## Update this skill

Make evidence-backed, narrow global changes in the independent Skill repository; preserve project state elsewhere. Use an isolated candidate when the Git gate applies. Bump VERSION/CHANGELOG, run `scripts/validate_skill.py` and the installed loader validator, independently review the changed scope, then commit. Promotion and push require applicable user authorization to the verified target; reuse an approval only for its authorized scope. Breaking major versions require explicit project migration and validation. Bootstrap templates must never overwrite accepted project memory without review.
