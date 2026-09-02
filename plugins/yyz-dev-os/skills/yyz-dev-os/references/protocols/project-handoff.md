# Project Handoff Protocol

The primary technical lead is a responsibility, not a permanent chat session. Create a durable Context Handoff when an accepted large feature reaches a phase transition, a governed Candidate reaches a gate, high-risk work pauses with recovery-critical state, a new lead must continue long-lived work, or context loss/repeated rereading/unstable understanding is impairing reliability. Do not create a durable handoff for every ordinary edit, small task, pause, model change, new chat, or chat duration alone.

1. Re-observe Git and record the working tree, HEAD, relevant diff facts, and key Commit(s) that identify the exact state being handed off.
2. Separate accepted, proposed, in-progress, blocked, failed, and unverified facts.
3. Read the project's recovery entry and use its declared Project Brain bindings; do not create a parallel fixed set of task, decision, or context files.
4. Update the narrowest project durable records only when their facts are supported: current stage, completed and unfinished work, blockers, next eligible action, and only new long-lived decisions.
5. Remove superseded items from an active view when project rules permit, but preserve accepted decisions, verification evidence, release records, and rollback history needed for recovery or audit.
6. Record the loaded YYZ Dev OS version and any compatibility/migration requirement.
7. Bind verification and review evidence to the exact Candidate or release.
8. Record unresolved findings, known limitations, required approvals, rollback/recovery information, and external storage exceptions.
9. Validate updated project memory and create/update the trusted checkpoint according to project rules. The replacement lead must be able to recover without reading old chat.
10. Report current stage, status, pass state, core issue/result, next step, tool, model, reasoning level, and role/task.

For a long-lived module-orchestrator handoff, also record the exact registered module ID, task identity, responsibility scope, worktree, and active writer owner in the project's existing Operating Rules or declared Project Brain bindings. Do not infer identity from a display name. Transfer writer ownership only after the successor has completed recovery and confirmed the same Git and worktree facts; a temporary native subagent is not a replacement long-lived module task.

Do not paste a raw chat transcript into Project Brain. Do not mark implementation as accepted, reviewed, promoted, released, or remotely backed up unless each state is independently established.

## Managed successor-task rotation

When the handoff trigger is impaired reliability or efficiency rather than a project phase gate, first verify that replacement is preferable to ordinary context reduction. Identify the exact task/session and worktree; never infer identity from a shared display name. Before transferring an active writer, establish a safe stop point from live Git, worktree ownership, locks, Candidate state, and relevant runtime state; never allow the old and successor tasks to write the same responsibility area concurrently.

Reuse or create a successor task only when the current host supports managed task lifecycle operations and either the current request explicitly authorizes the action or validated project-local rules provide standing authority that the host accepts. Otherwise, prepare the durable handoff and ask for the smallest required user action. Preserve a recognizable project/module identity without leaving two active tasks indistinguishable.

The successor must complete Project Recovery and confirm the transferred responsibility before the old task is archived. Archive rather than delete when retention is available, and never treat the archived conversation as project truth. If recovery, writer transfer, or archival status cannot be verified, keep the old task available and report the exact incomplete state.
