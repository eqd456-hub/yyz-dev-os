# Repair Loop Protocol

1. Verify each review finding against the Candidate and authoritative requirements.
2. Classify it as `TRUE`, `FALSE_POSITIVE`, or `UNVERIFIED`; preserve the reasoning and evidence.
3. For each true finding, define a bounded repair that does not widen unrelated scope.
4. Repair in the managed worktree and add or update a regression test or reproducible check where appropriate.
5. Re-run the failed check, affected-area checks, and required full gates.
6. Inspect the new diff and bind the repaired Candidate to its Base and predecessor.
7. Return the repair evidence to independent review. Do not self-close material findings.
8. Stop the loop when all true findings are verified fixed, remaining unverified findings are explicitly resolved or accepted by proper authority, and required gates pass.

Do not weaken tests, acceptance criteria, or safety controls merely to make a finding disappear. Escalate repeated or architectural failures instead of applying unlimited patches.
