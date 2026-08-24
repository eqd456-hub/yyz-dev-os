# Reporting Policy

## Default daily report

For ordinary code changes, report briefly with:

- Changes: files changed and why.
- Architecture: whether the existing structure is affected.
- Validation: checks run and their result.
- Risks: remaining potential risks.

If there is no structural impact or known risk, say so briefly.

For governed recovery, review, or promotion work, add stage, exact status, evidence identity, blocker, and next gate only when relevant. Report tool/model/reasoning identity only when required and known; never guess it. Keep low-level commands and logs out of the main report unless they are evidence or the user requests them.

When user action is required, provide the complete copyable command or exact UI action, expected outcome, and safety precondition. Distinguish implementation completion from verification, review, acceptance, promotion, release, and remote backup status.
