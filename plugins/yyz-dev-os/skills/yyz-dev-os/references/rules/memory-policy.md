# Memory Policy

## Separate durable layers

Maintain these distinct layers:

1. Global Development Skill: cross-project rules and protocols.
2. Global Capability Ledger: verified cross-project AI capability history.
3. Project Brain: accepted, project-specific long-lived facts.
4. Project Operating Rules: repository and project constraints.
5. Project Checkpoint: trusted recovery snapshot bound to evidence.
6. Task/session runtime state: temporary execution context.

Chat is not a project database. Never use a raw chat transcript as the authoritative long-lived project state. Treat conversation memory as the lowest-authority convenience layer. A lead role may move between sessions; durable project records must let a replacement lead recover without relying on old chat.

Keep prompts incremental. Reference existing operating rules, architecture, Project Brain, checkpoints, and code instead of re-embedding unchanged content on every task. Load only the durable records needed to resolve the current request or risk.

A technical execution card is task/session runtime state: a compact working model for each non-trivial or cross-module implementation, not a Project Brain record, checkpoint, or independent truth source. Do not create one for a small, clear, low-risk task, including a plan-first task after its plan is approved. Keep every card in task/session runtime by default; persist no card itself. Only when an existing durable handoff rule applies may the narrowest accepted facts that materially improve recovery be persisted, with its required evidence.

## Durable updates

After an accepted event that changes durable project state, update only the narrowest records needed to recover: current state, roadmap, decisions, known issues, checkpoint, verification history, and capability evidence as applicable. Do not write a durable handoff for every ordinary local edit, session pause, new chat, or model change. Bind updates to observed evidence and preserve provenance. Active views may remove superseded items, but do not delete accepted decisions, verification evidence, release records, or rollback history without an authorized retention rule.

Never write a project's current state into the global Skill. Never write general global policy into Project Brain as if it were a project fact; reference the loaded Skill identity and compatible version instead.
