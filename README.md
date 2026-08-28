# YYZ Dev OS

YYZ Dev OS is an on-demand, project-independent professional development and engineering-governance Skill. Its current version is recorded in [`VERSION`](VERSION). It keeps ordinary small development lightweight while preserving durable recovery, evidence, security, Git, review, and promotion controls for work that needs them.

## Invoke

- Explicitly: `Use $yyz-dev-os to bootstrap this project.`
- Plan or implement a feature: `Use $yyz-dev-os to turn this request into a scoped development plan and implement it when authorized.`
- Recover existing work: `Use $yyz-dev-os to recover this project, verify its actual state, and tell me the next step.`
- Govern a risky delivery: `Use $yyz-dev-os to apply the relevant security, evidence, review, or promotion gates.`

The Skill may trigger automatically for non-trivial features, cross-module behavior changes, plan-first requests, durable recovery, data/security risk, high-risk Git or deployment, shared core/orchestrator core, major architecture, trusted evidence, independent review, or promotion. Routine clear bugs, UI work, prompts, and small local features remain lightweight: read the relevant code, make the bounded change, run necessary checks, and report briefly without loading full governance.

## Adopt in a project

Copy the JSON templates from `assets/templates/` into `<project>/.aidev/`, replace placeholders, and validate the recovery entry against `assets/schemas/recovery-entry.schema.json`. Record `globalSkill: yyz-dev-os` and the actually loaded compatible version. Do not overwrite accepted project facts.

## Validate and upgrade

Run `scripts/validate_skill.py`, then the installed Skill loader validator. Apply PATCH and backward-compatible MINOR releases only after project compatibility validation. Require explicit migration for every MAJOR release. Update `VERSION` and `CHANGELOG.md` together; commit through the Skill's independent repository, and push only with separate authorization to an already configured private remote.

All paths in the package are relative or configurable. Project-specific state belongs in Project Brain, never here.

## Private team plugin

Team members need access to this private GitHub repository and Git authentication that can read it. Install the team marketplace and plugin with:

```powershell
codex plugin marketplace add eqd456-hub/yyz-dev-os --ref main
codex plugin add yyz-dev-os@yyz-team
```

After a published update, refresh the configured Git marketplace and reinstall the plugin:

```powershell
codex plugin marketplace upgrade yyz-team
codex plugin add yyz-dev-os@yyz-team
```

Start a new Codex task after installation or update so it can discover the updated Skill. The repository root is the maintenance source; run `scripts/build_plugin_package.py` before publishing and `scripts/build_plugin_package.py --check` before promotion.

## Public directory candidate

This package has user authorization for public release and is ready for Portal submission, but it has not been submitted or approved. Until approval and public distribution are completed, installation remains the private-team flow above and still requires repository access.

The candidate is Skills-only: it includes no MCP server, hosted service, API key, or plugin-managed data collection. The maintenance repository keeps public-listing, privacy, terms, support, and review materials in `submission/` and `docs/`; those publication files are intentionally excluded from the runtime Skill snapshot. The red-and-black plugin logo and composer icon are packaged. The public site is expected at `https://eqd456-hub.github.io/yyz-dev-os/`, with support through the issue tracker and Pages privacy/terms URLs. The verified individual publisher is `杨元钊`, while the developer display name is `YYZ`; check the Portal preview for public identity visibility before submission. After approval and public availability, colleagues can install from the public directory without GitHub or private-cloud access.

License: [MIT](LICENSE).
