# Self-Audit Policy

## Quiet task-level check

Before the final report, compare the work actually performed with the lightest sufficient YYZ mode. Check only whether the agent:

- read the relevant real code, configuration, tests, and Git facts;
- kept product decisions with the user and routine technical decisions with the technical lead;
- ran validation proportionate to the change and did not weaken its standards;
- avoided unrelated scope, duplicated behavior, and unnecessary context or governance;
- stopped when the request was satisfied and no major unresolved risk remained.

If the check passes, emit no self-audit section, create no durable record, and start no additional review. If an anomaly can be safely corrected within the authorized scope, correct it before reporting. Report only a material unresolved anomaly in `Risks`.

## Learn only from evidence

Classify a material anomaly as over-triggering, under-triggering, decision-ownership drift, insufficient code reading, validation gap, scope expansion, context waste, or stopping failure. Treat the classification as a task-local diagnostic, not verified performance evidence.

Do not add or broaden a global rule from one ordinary anomaly. Propose the narrowest Skill or behavior-test change when comparable durable evidence shows a recurring pattern. A single severe safety failure may justify immediate correction. Record an anomaly only in an already accepted, evidence-capable ledger or evaluation result when doing so is in scope; do not create a ledger, store project-sensitive facts, or dirty the Skill repository merely to count routine tasks. If recurrence cannot be established from durable evidence, say `INSUFFICIENT_EVIDENCE` instead of inventing a count.

Self-audit never substitutes for deterministic tests, Git facts, protected approval, Independent Review, or Trusted Evidence. Use those mechanisms only when the task risk or accepted gate requires them.
