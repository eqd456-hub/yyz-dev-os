# AI Role Policy

## Separate responsibilities

Assign explicit roles and prevent one role from silently acquiring another role's authority:

- Product/project owner: define intent, priorities, product tradeoffs, and high-impact human approvals.
- Technical lead: choose architecture, decomposition, tools, verification strategy, and risk controls.
- Implementer: modify only authorized scope and produce an implementation handoff.
- Verifier: run and inspect required checks and preserve evidence.
- Independent reviewer: challenge the candidate against source-of-truth and acceptance criteria.
- Approver: accept or reject risk and product decisions within granted authority.
- Promoter/releaser: move a verified, approved candidate into the stable channel.

An implementer may perform self-checks but cannot independently establish acceptance. A reviewer finding remains a claim until its evidence is reproduced or otherwise verified.

## Agent coordination

Give every worker one bounded objective, one writable worktree at most, authoritative input locations, prohibited scope, and expected evidence. Never allow multiple agents to write the same worktree concurrently. Parallelize only independent read-only work or isolated writable worktrees.

Keep verification, independent review, user approval, and promotion under separately observable states even if one tool performs multiple mechanical steps.
