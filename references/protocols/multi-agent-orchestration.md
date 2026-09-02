# Multi-Agent Orchestration Protocol

Use this protocol only when a development task has a registered long-lived module owner, separates into useful independent stages, crosses module boundaries, benefits materially from context isolation or parallel read-only work, or needs risk separation. A small, clear task that the current lead can finish safely should stay direct.

## Logical hierarchy and depth

Use at most two delegation edges:

`PROJECT_ORCHESTRATOR → MODULE_ORCHESTRATOR → bounded worker`

The project orchestrator may also create a direct read-only helper for project-wide discovery, plan comparison, risk analysis, or final review. Every bounded worker created by either orchestrator is terminal: set `mayDelegate` to `false`, and do not let it create another agent. Treat this as a logical authority depth even when the host represents tasks or agents differently.

A native subagent is temporary work created and collected by its current parent. A long-lived module task is a separately registered project responsibility with durable module context. Do not treat them as the same mechanism. Reuse a verified registered module task when one exists. Create, replace, or archive a user-visible long-lived task only when the current host supports it and the user has explicitly authorized that task lifecycle action.

## Assignment contract

Before delegation, provide the smallest complete contract needed for the stage:

- task ID and parent task ID;
- logical role and orchestration depth;
- module ID when module ownership applies;
- bounded objective, responsibility scope, and prohibited scope;
- authoritative code, rules, and evidence locations;
- worktree identity and read/write permission;
- dependencies, acceptance criteria, required tests, and expected evidence;
- `mayDelegate`, which must be `false` for a bounded worker.

Pass requirement deltas and evidence locations instead of copying full project history. Project-specific module names, task identities, paths, worktrees, and dependencies belong in validated project Operating Rules or an equivalent Project Constitution, never in this global protocol.

## Read, write, and cleanup safety

- Independent read-only tasks may run in parallel.
- One worktree may have only one active writer. Parallel writers require verified independent worktrees and non-overlapping responsibility.
- The project orchestrator and a module orchestrator must not write the same responsibility area concurrently.
- A planning, architecture, risk, or review helper is read-only by default.
- A designated cleanup or code-health track remains read-only while other writers are active. Broad deletion, moves, or refactoring require an isolated worktree and project-orchestrator review before integration. A small local cleanup performed by the sole authorized writer remains subject to the ordinary proportional workflow.

## Worker result and acceptance

Every worker returns a compact evidence-bearing result containing:

- task ID and work scope;
- discovery or implementation conclusion;
- modified files;
- Commit when one was authorized and created;
- test commands and results;
- risks and unresolved items;
- whether another module is affected.

A module orchestrator must re-read the relevant code and evidence, inspect the diff, run or verify required tests, and accept, repair, or reject the result. It reports only its own checked conclusion to the project orchestrator. The project orchestrator verifies module boundaries, dependencies, integration evidence, and the final candidate before closing the project-level task. Worker completion is never automatic acceptance.

## Fail closed and recovery

When orchestration is active, stop with `BLOCKED` rather than guessing if a required role is unavailable, module ownership is ambiguous, task assignment conflicts, worktree identity or writer ownership conflicts, a worker exceeds its scope or depth, or required acceptance evidence is missing. This does not block a small direct task merely because the project has no module registry.

For a long-lived module handoff, use the existing Project Handoff and Recovery protocols. Transfer writer ownership only after recording the exact module, task, worktree, Git state, unfinished work, evidence, and next action, and after the successor has recovered successfully.

Use [AI Role Policy](../rules/ai-role-policy.md) for role authority, [Routing Policy](../rules/routing-policy.md) for model selection, [Verification Policy](../rules/verification-policy.md) for evidence, [Independent Review](independent-review.md) for governed review, [Git Policy](../rules/git-policy.md) for worktree and promotion safety, and [Reporting Policy](../rules/reporting-policy.md) for user-visible communication.
