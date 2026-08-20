# Git Policy

## Governed delivery lifecycle

Use this lifecycle when work touches a protected branch/surface, high-risk Git, automated deployment/promotion, a release, or another accepted project gate:

`Base → managed/isolated worktree → implementation → tests → candidate → independent review → repair if required → verification → accepted release`

Observe the base directly and bind the candidate to it. Keep the implementation report separate from candidate acceptance. Use project-defined managed branches and worktrees; do not assume a branch name or storage path. Ordinary low-risk local changes follow project-local Git rules and do not automatically require SHA verification or promotion review.

## Safety rules

- Do not modify a stable production installation or protected/default branch directly when project rules or task risk require isolation.
- Do not allow multiple agents to write the same worktree concurrently.
- Do not force-push by default.
- Do not rewrite history, discard user changes, delete branches/worktrees, or promote without explicit authority and exact target verification.
- Preserve unrelated user changes and stop if they overlap the authorized scope in a way that cannot be safely isolated.
- Keep promotion/release distinct from ordinary implementation.

Before promotion, verify candidate identity, ancestry, diff scope, required evidence, independent review state, approval state, and rollback/recovery path. Prefer fast-forward or another project-approved non-destructive promotion method.
