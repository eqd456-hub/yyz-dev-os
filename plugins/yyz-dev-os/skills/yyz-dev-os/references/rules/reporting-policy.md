# Reporting Policy

## Default daily report

For code changes, report briefly with:

- Changes: the user-visible effect first, then files changed and why.
- Architecture: whether the existing structure is affected.
- Validation: checks run and their result.
- Risks: remaining potential risks.

If there is no structural impact or known risk, say so briefly. Include root cause, business-rule ownership, reuse/duplicate prevention, dependency choice, or extensibility only when it materially helps the user understand the outcome; do not turn daily reports into a fixed long checklist.

## Low-noise execution updates

Follow any host-required progress-update cadence and any explicit user request for visibility. Otherwise, do not narrate private reasoning, every command, routine tool/model selection, worktree mechanics, or repetitive review activity. Send an intermediate update only when it communicates a material state change, a blocker, required user input, or useful progress during longer work, and keep it result-oriented and brief.

Pass detailed technical evidence to the responsible lead or active review/release gate only when it is needed for acceptance. Prefer compact conclusions and evidence locations over repeated stable context or full logs. This does not suppress material failures, safety limitations, protected approvals, or the final report.

For governed recovery, review, or promotion work, add stage, exact status, evidence identity, blocker, and next gate only when relevant. Report tool/model/reasoning identity only when required and known; never guess it. Keep low-level commands and logs out of the main report unless they are evidence or the user requests them.

When user action is required, provide the complete copyable command or exact UI action, expected outcome, and safety precondition. Distinguish implementation completion from verification, review, acceptance, promotion, release, and remote backup status.

## Managed multi-task quiet reporting

Treat quiet reporting as an optional global capability activated by the user's explicit preference or validated project Operating Rules, not as a universal silence requirement.

When it is active, each managed worker or long-lived module task keeps its full progress, technical report, evidence pointers, and final result in its own task or project-approved evidence location. Do not push routine progress, intermediate reports, tool logs, or local technical discoveries across tasks into the user's active primary conversation. The responsible orchestrator retrieves those reports through supported task read/wait mechanisms, checks them against real code, Git, tests, Candidate identity, and relevant runtime state, and handles repair or coordination before user-facing closure.

The project orchestrator normally summarizes to the user when the scoped work is complete and ready for product acceptance. It may communicate earlier when the user asks for status, when the host requires a progress update, or when continued work needs a product/business decision, protected approval, credential or user-only action, or resolution of a material safety, security, data, permission, or unrecoverable execution blocker. Keep any required interruption minimal and decision-oriented.

This mode changes the reporting channel, not the standard of truth. Never suppress failures, evidence gaps, approval boundaries, risk status, or required user action. Preserve full technical evidence in the responsible task even when the user-facing summary remains concise.

For a cross-task handoff or control message, use a pointer-only envelope containing only the task ID, current state, authoritative evidence location, requested action, scope or stop boundary, and done condition. Keep history, context dumps, routine acknowledgements, logs, test transcripts, and hash lists in the source task or evidence store. The recipient reads the referenced source evidence and must not treat the compact envelope as proof by itself.
