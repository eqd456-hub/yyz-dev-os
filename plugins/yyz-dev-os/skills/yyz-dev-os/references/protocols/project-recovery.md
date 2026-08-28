# Project Recovery Protocol

Run these steps when full recovery is triggered by a status/history request, stale or conflicting state, Context Handoff or context-loss continuation, high-risk dependency on durable state, or an accepted project gate. A newly opened ordinary chat or a small local task does not trigger full recovery by itself.

1. Identify the project and repository.
2. Read the nearest applicable `AGENTS.md` and validate the project's recovery entry.
3. Load the declared compatible YYZ Dev OS version.
4. Read and verify actual Git state: repository identity, working tree, refs, HEAD, ancestry, and relevant diff facts.
5. Read validated project Operating Rules.
6. Resolve current state, roadmap, decisions, and known issues relative to the validated Project Brain root and recovery order. Read architecture, evidence, checkpoint, and ledger sources only from the recovery-entry bindings. Never replace a missing source by inventing another document.
7. Detect conflicts, stale timestamps/bases, missing sources, unsupported versions, proposed-versus-accepted state, and unverified claims.
8. Build a Recovery Context with project identity, loaded Skill version, observed Git facts, accepted state, proposed state, blockers, next eligible work, evidence gaps, and conflicts.
9. Only after recovery succeeds, answer the status question or begin implementation.

Never use chat memory as project truth. Use it only as a low-authority hint to locate durable sources. When chat disagrees with authoritative durable state, explicitly discard the stale chat claim and proceed from re-observed durable facts.

If recovery is incomplete, state `RECOVERY_INCOMPLETE`, list the missing or invalid authority source, and limit work to safe diagnostics or repair explicitly authorized by the user.
