# Recovery Policy

## Full recovery triggers

Run full Project Recovery when asked to reconstruct project status/history or continue durable work after context loss; when project state is stale, missing, or conflicting; or when a high-risk task depends on checkpoints, accepted state, capability evidence, or promotion history.

Do not run full Project Recovery merely because a new chat/model/session begins or because an ordinary low-risk task changes a local file. For routine work, read project-local instructions, relevant real code/tests/configuration, and current Git status. Escalate if those facts expose a recovery trigger.

Never use chat memory as project truth. If chat conflicts with durable project state, prefer the authoritative durable state, re-observe live facts, and explicitly recalibrate the working context.

## Recovery outcome

Do not claim recovery merely because files were read. Complete recovery only after:

- identifying the project and loaded global Skill version;
- validating the recovery entry and project operating rules;
- observing Git state;
- loading all declared durable sources in order;
- detecting conflicts, staleness, missing evidence, and unsupported schema versions;
- producing a Recovery Context that separates observed, accepted, proposed, stale, and unverified facts.

Fail closed on malformed authority metadata, path traversal, unsupported schema versions, or secret-bearing project memory. Report what remains unavailable without fabricating a replacement state.
