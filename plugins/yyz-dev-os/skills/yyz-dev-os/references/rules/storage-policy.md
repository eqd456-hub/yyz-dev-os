# Storage Policy

## Unified root

Place all controllable YYZ-managed development data under a Configured Unified Storage Root, including projects, worktrees, memory, capability ledgers, runtime state, evidence, artifacts, logs, cache, temporary files, and backups.

Never hard-code a drive, home directory, or machine-specific absolute path in this Skill. Resolve locations from project metadata, configuration, environment, or repository-relative paths. Keep Skill identity, version, and Git history stable when the configured storage root changes.

## External exceptions

Record any system-level storage that a third-party tool does not allow the project to control as an External Storage Exception. Document owner/tool, purpose, location resolution method, sensitivity, retention, backup status, and migration/recovery implications.

No external exception may be the only copy of source code, Project Memory, capability evidence, verification evidence, or user work product. Separate disposable cache/temp data from durable data. Back up durable data and verify recovery, not merely backup creation.
