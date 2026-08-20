# Project Handoff Protocol

Create a durable handoff when accepted project state changes, a governed Candidate reaches a gate, high-risk work pauses with recovery-critical state, or the user/project explicitly requires it. Do not create a durable handoff for every ordinary edit, pause, model change, or chat transition.

1. Re-observe Git and identify the exact state being handed off.
2. Separate accepted, proposed, in-progress, blocked, failed, and unverified facts.
3. Update the narrowest project durable records only when their facts are supported.
4. Record the loaded YYZ Dev OS version and any compatibility/migration requirement.
5. Bind verification and review evidence to the exact Candidate or release.
6. Record unresolved findings, known limitations, next eligible action, required approvals, rollback/recovery information, and external storage exceptions.
7. Validate updated project memory and create/update the trusted checkpoint according to project rules.
8. Report current stage, status, pass state, core issue/result, next step, tool, model, reasoning level, and role/task.

Do not paste a raw chat transcript into Project Brain. Do not mark implementation as accepted, reviewed, promoted, released, or remotely backed up unless each state is independently established.
