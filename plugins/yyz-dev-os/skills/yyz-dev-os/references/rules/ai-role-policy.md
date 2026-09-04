# AI Role Policy

## Separate responsibilities

Assign explicit roles and prevent one role from silently acquiring another role's authority:

- Product/project owner: define intent, priorities, product tradeoffs, and high-impact human approvals.
- Technical lead: choose architecture, decomposition, tools, verification strategy, and risk controls.
- Planning advisor: propose alternatives, tradeoffs, risks, and unknowns from a bounded brief without acquiring project authority or implementation permission.
- Implementer: modify only authorized scope and produce an implementation handoff.
- Verifier: run and inspect required checks and preserve evidence.
- Independent reviewer: challenge the candidate against source-of-truth and acceptance criteria.
- Approver: accept or reject risk and product decisions within granted authority.
- Promoter/releaser: move a verified, approved candidate into the stable channel.

Treat product acceptance and technical readiness as separate evidence. A user's confirmation of visible behavior, interaction, output, or another product outcome does not prove code, architecture, security, data, regression, Candidate, or release readiness. Technical verification does not invent user acceptance for a subjective product outcome that the user has not reviewed. Neither state silently grants protected-action authority.

For ordinary low-risk development, one AI may implement and run necessary self-checks. Do not call that work an independent review. A planning advisor's proposal is input to the technical lead, not a project decision or source of truth. Separate reviewer, approver, and promoter authority only when the task requests it, risk requires it, or an accepted project gate mandates it. A reviewer finding remains a claim until its evidence is reproduced or otherwise verified.

## Orchestration role registry

Use these stable logical roles when multi-agent or long-lived module orchestration is active. Keep role definitions separate from model selection so a routing change does not rewrite the workflow:

- `PROJECT_ORCHESTRATOR`: own the cross-module plan, dependency order, module assignments, integration verification, and final technical conclusion.
- `MODULE_ORCHESTRATOR`: own one registered module's plan, bounded worker assignments, code acceptance, module tests, and evidence-bearing report to the project orchestrator.
- `EXPLORER`: perform bounded read-only discovery such as code maps, call chains, logs, documentation, and batch inspection.
- `IMPLEMENTER`: make an authorized scoped change in one assigned writable worktree and run the required checks.
- `STANDARD_REVIEWER`: perform ordinary read-only diff, maintainability, and test-gap review; this role does not satisfy a governed Independent Review gate by itself.
- `CRITICAL_REVIEWER`: perform independent read-only review for architecture, permissions, security, data migration, cross-module risk, major refactoring, or another protected gate.

The global registry defines roles, not project assignments. Store project-specific module names, responsibility paths, dependencies, task identities, and worktree bindings only in validated project Operating Rules or an equivalent Project Constitution. A project orchestrator may complete small direct project-level or unowned work without creating a module hierarchy, but must not treat module-owned work as direct merely because it is small.

## Agent coordination

Give every worker one bounded objective, one writable worktree at most, authoritative input locations, prohibited scope, and expected evidence. Never allow multiple agents to write the same worktree concurrently. Parallelize only independent read-only work or isolated writable worktrees.

For module-owned work, the project orchestrator routes the assignment to the registered module orchestrator. Any worker then reports to that module orchestrator, which must inspect the implementation and evidence before reporting an accepted module result to the project orchestrator. A project orchestrator's own read-only exploration, planning, risk, or review helper may report directly to the project orchestrator. Never forward a worker self-report unchanged as acceptance.

When those governed stages apply, keep verification, independent review, user approval, and promotion under separately observable states even if one tool performs multiple mechanical steps.
