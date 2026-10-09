# Quality and verification

Use before choosing checks, applying completion criteria, or making a final
assessment. Assess the calling skill's contract, the task's acceptance
criteria, and applicable project requirements together; no one replaces the
others. Determine which checks fit the actual result, rather than imposing
tests meant for another kind of change.

For each material completion claim, identify the criterion, suitable check,
observed result, and limit of that evidence. Structure and file presence do
not prove behavior. Use evidence for the current version: after changing an
affected part, reconsider earlier results. Avoid repeating an expensive check
when suitable current evidence already exists. Distinguish checks that passed,
failed, were not run, or genuinely do not apply, with a reason for the latter;
unavailable tools do not make a required check inapplicable.

Do not treat loading a dependency as using it, a small change as exempt from
mandatory checks, a glossary entry as preserving all requirements, or a
rewritten expectation as proof a defect was fixed. Do not bypass a mandatory
storage mechanism when its tool is unavailable. A legitimate scope change,
draft-only request, or actual limitation may alter the achievable result;
report it honestly without retroactively claiming old criteria were met.

If a check fails or behavior diverges from agreed requirements, investigate
the affected part before building on it. If required evidence is absent, mark
that portion unverified; if a critical input, permission, or dependency is
missing, block only the dependent action and continue independent work where
possible. Verify the result within the current task when appropriate; neither
verification nor review automatically starts another lifecycle stage.
