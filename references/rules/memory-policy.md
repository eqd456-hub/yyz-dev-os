# Memory Policy

## Separate durable layers

Maintain these distinct layers:

1. Global Development Skill: cross-project rules and protocols.
2. Global Capability Ledger: verified cross-project AI capability history.
3. Project Brain: accepted, project-specific long-lived facts.
4. Project Operating Rules: repository and project constraints.
5. Project Checkpoint: trusted recovery snapshot bound to evidence.
6. Task/session runtime state: temporary execution context.

Chat is not a project database. Never use a raw chat transcript as the authoritative long-lived project state. Treat conversation memory as the lowest-authority convenience layer.

## Durable updates

After an accepted material event, update the narrowest durable project records needed to recover: current state, roadmap, decisions, known issues, checkpoint, verification history, and capability evidence as applicable. Bind updates to observed evidence and preserve provenance.

Never write a project's current state into the global Skill. Never write general global policy into Project Brain as if it were a project fact; reference the loaded Skill identity and compatible version instead.
