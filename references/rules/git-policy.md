# Git Policy

## Delivery lifecycle

Use this lifecycle for material work:

`Base → managed/isolated worktree → implementation → tests → candidate → independent review → repair if required → verification → accepted release`

Observe the base directly and bind the candidate to it. Keep the implementation report separate from candidate acceptance. Use project-defined managed branches and worktrees; do not assume a branch name or storage path.

## Safety rules

- Do not modify the stable production or default branch directly for material development.
- Do not allow multiple agents to write the same worktree concurrently.
- Do not force-push by default.
- Do not rewrite history, discard user changes, delete branches/worktrees, or promote without explicit authority and exact target verification.
- Preserve unrelated user changes and stop if they overlap the authorized scope in a way that cannot be safely isolated.
- Keep promotion/release distinct from ordinary implementation.

Before promotion, verify candidate identity, ancestry, diff scope, required evidence, independent review state, approval state, and rollback/recovery path. Prefer fast-forward or another project-approved non-destructive promotion method.
