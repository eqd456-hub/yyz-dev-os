# Recovery Policy

## Mandatory triggers

Run Project Recovery before answering project status or changing files after any new chat, new AI/model, application restart, long-context compaction, explicit continuation request, status question, or next-step question.

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
