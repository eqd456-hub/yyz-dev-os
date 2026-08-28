# Independent Review Protocol

Use this protocol only when independent review is explicitly requested, risk-justified, or required by an accepted project gate. Review the Candidate independently from the implementation claim.

1. Re-observe repository identity, Base, Candidate, ancestry, worktree cleanliness, and diff scope.
2. Load validated project operating rules, acceptance criteria, decisions, known issues, and required evidence.
3. Read the diff, code paths, tests, artifacts, and relevant runtime behavior.
4. Evaluate the Implementation Report last; use it as a map, not truth.
5. Reproduce material findings or mark them `UNVERIFIED`.
6. Record each finding with:
   - ID
   - Severity
   - File or call path
   - Concrete scenario
   - Violated acceptance criterion or invariant
   - Reproduction/evidence
   - Status: `TRUE`, `FALSE_POSITIVE`, or `UNVERIFIED`
   - Bounded fix
7. Re-run or inspect the evidence needed to determine whether the Candidate is ready, needs repair, or cannot yet be judged.

A reviewer report remains a claim. Recheck critical Git and evidence facts before acceptance or promotion. Report no actionable findings only when the reviewed scope and evidence support that result.
