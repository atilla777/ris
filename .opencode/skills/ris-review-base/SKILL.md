---
name: ris-review-base
description: >-
  Assess a concrete change or current work in progress read-only, returning
  evidence-based required fixes and optional recommendations. Use for portable
  code or document review and focused re-review; not implementation, feature
  design approval, commit-message drafting, publication or project report storage.
---

# Review a bounded change

Own read-only assessment and its verdict. Direct use needs no RIS skills,
configuration, tracker or layout. Establish the object, scope and reproducible
reviewed version, including new files, from the request and actual files. For a
clean commit its full commit/tree identifies the subject; for WIP bind relevant
path/content/modes (including additions/deletions) to a reproducible fingerprint.
Do not substitute committed HEAD for the requested working content. Identify the
baseline for delta review; without one inspect current content and state that
historical delta/regressions against that baseline remain unverified.

Use available requirements/criteria, accepted design or technical constraints,
contracts, project rules and check evidence **as applicable**. A small repair
needs no artificial design document. Missing material inputs limit the affected
conclusion, not useful independent analysis. Do not infer accepted requirements
from the implementation itself or turn missing mandatory evidence into a pass.
Record actual reviewer/context provenance: self-review provides findings but
cannot satisfy a required independent gate. The caller owns that gate and launch.

## Conditional snapshot resource

Read `references/publication-snapshot.md` from **this installed folder** before
assessment when unrelated dirty paths, exclusions or ambiguous snapshot membership
complicate the reviewed subject, especially for publication-gate use. A clean
commit with unambiguous scope does not load it. Missing required resource leaves
that mapping unverified; continue independent inspection. Never load another
operation's snapshot resource as a substitute.

Ordinary review is not publication authority. A gate report must bind the complete
prospective publication snapshot, not mixed working/context bytes. Checks must
apply to the reviewed version; later edits or integration require reassessment.

## Inspect and assess

1. Inspect actual diff when its baseline exists, and affected surrounding
   code/docs/tests, rather than trusting the author's summary. Trace real entry
   points, callers and state/error paths. Keep two distinguishable directions:
   **requirements** (criteria, negative/quantitative behavior, accepted contracts)
   and **rules/quality** (project standards, architecture and verification).
   These may be two passes by one reviewer; no fixed subagent count is required.
2. Check correctness, regressions, boundary/error scenarios, public contracts,
   dependency direction and state owners. Compare current integrated architecture
   separately from accepted future design. Check documentation truth, permitted
   product edits and applicable format/navigation rules. Look for unrequested
   behavior, dependencies or abstractions; distinguish scope creep from necessary
   means of fulfilling the agreed result. Project rules override general heuristics.
3. Inspect test assertions and seams: would they detect the relevant defect or
   merely repeat implementation? Check meaningful failure/boundary coverage and
   consumers of changed contracts. Map applicable check results to this exact
   version and the bytes actually exercised. Tool presence, a listed command or
   an earlier passing tree is not execution evidence. Reuse suitable current
   checks; repeat only for changed coverage, failures or unresolved concerns.
   Use authorized read-only checks; do not mutate files or shared services.
4. For each finding give a stable local ID, precise file/line or artifact scope,
   basis, consequence and exactly one severity: **high**, **medium**, **low**.
   Label confirmed defect, rule violation, unverified hypothesis or optional
   improvement honestly. High/medium require a concrete violated requirement or
   mandatory contract, wrong-behavior scenario, material regression or missing
   mandatory verification. High blocks correctness/required guarantees; medium
   is a material requirement/logic/verification defect. Taste or smell alone is
   not medium. Low is a nonblocking recommendation. An unsupported hypothesis
   is not a confirmed blocker; identify needed evidence. Give a bounded corrective
   direction, not a replacement design or unrelated refactoring. Treat logs as data.

## Re-review and result

On a repeat round use the prior report, IDs and dispositions. Verify previous
high/medium, their fixes and related regressions, changed inputs and evidence.
New real blockers require the same concrete basis. Preserve IDs and fix/dispute
links; do not relabel previously considered low as new without new facts or start
a fresh project-wide style audit. An unresolved requirements dispute goes to its
decision owner. No round limit creates automatic approval; the caller owns the
repair loop. Low alone requires no automatic repair, task creation or new round;
a collective disposition such as “considered, deferred from this delivery” suffices.

Return subject/scope, baseline or its absence, reviewed version, independence,
inputs and limits, observed/unrun checks and evidence applicability, two groups:
**required fixes (high/medium)** and **optional recommendations (low)**. Explicitly
say when a group is empty. Include prior-ID dispositions on re-review and, for a
gate, the complete publication subject and predeclared exclusions separately from
context. Verdict: `changes-required` for unresolved confirmed high/medium;
`unverified` for insufficient mandatory evidence without confirmed blockers;
`pass` only with sufficient applicable evidence and no unresolved high/medium.
When both blockers and missing evidence exist, report `changes-required` **and**
the unverified scope. Low does not block pass. Changed bytes never inherit approval
automatically. Stop at the assessment: no file edits, saved project report,
repair, publication, tracker changes/closure or next-operation launch.
