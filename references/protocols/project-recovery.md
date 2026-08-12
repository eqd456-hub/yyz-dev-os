# Project Recovery Protocol

Run these steps in order before answering project state or beginning work:

1. Identify the project and repository.
2. Read and validate `.aidev/recovery-entry.json`.
3. Load the declared compatible YYZ Dev OS version.
4. Read and verify actual Git state: repository identity, working tree, refs, HEAD, ancestry, and relevant diff facts.
5. Read validated project Operating Rules.
6. Read `current-state.json`.
7. Read `roadmap.json`.
8. Read `decisions.json`.
9. Read `known-issues.json`.
10. Read the declared trusted checkpoint when present.
11. Read the declared Global and Project Capability Ledger bindings when present.
12. Detect conflicts, stale timestamps/bases, missing sources, unsupported versions, proposed-versus-accepted state, and unverified claims.
13. Build a Recovery Context with project identity, loaded Skill version, observed Git facts, accepted state, proposed state, blockers, next eligible work, evidence gaps, and conflicts.
14. Only after recovery succeeds, answer the status question or begin implementation.

Never use chat memory as project truth. Use it only as a low-authority hint to locate durable sources. When chat disagrees with authoritative durable state, explicitly discard the stale chat claim and proceed from re-observed durable facts.

If recovery is incomplete, state `RECOVERY_INCOMPLETE`, list the missing or invalid authority source, and limit work to safe diagnostics or repair explicitly authorized by the user.
