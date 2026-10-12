---
name: ris-review-base
description: >-
  Assess a concrete change against requirements, accepted design, architecture
  and verification evidence, returning located severity-ranked findings. Use for
  portable read-only change review; not implementation, feature design approval,
  commit-message drafting, publication or project report storage.
---

# Review one concrete change

Own read-only findings and a bounded verdict. Direct use requires no RIS skills,
config, tracker or layout. Require change scope and reproducible final revision/
tree fingerprint (including new files), its base, requirements and criteria,
accepted technical constraints/design/contracts, project rules and test evidence.
Establish whether the reviewer context is independent of implementation; self-
review can provide findings but cannot satisfy an independent approval gate.

Before assessment define the approval subject: the complete prospective Git
snapshot (base plus explicit authorized overlays/additions/deletions, modes and
unchanged base paths), or an equivalent reproducible publication manifest.
Separately identify contextual inputs such as tracker claim, local reports and
installed tooling. For an excluded dirty tracked file the subject contains its
specified base bytes, not the working bytes. Inspect relevant contextual effects
but do not approve a mixed all-files fingerprint as the Git payload. Verify all
exclusions against scope and actual files; unexpected new application files or
unexplained omissions block approval. Record this subject and exclusions in the
report before issuing the verdict. A caller cannot later invent exclusions or
substitute different snapshot bytes under the same approval.

Inspect actual diff and affected surrounding code/docs/tests, not only the author's
summary. Trace criteria, negative/quantitative requirements and failure paths;
check accepted design, public contracts, dependency direction, state ownership,
data/error handling and applicable architecture fitness constraints. Look for
regressions and missing meaningful tests. Distinguish current integrated
architecture from future accepted design; check documentation truth, permitted
product edits and applicable format/navigation requirements. Determine which
checks cover this exact tree, and whether claimed environment/output is accessible.
Do not infer success from a command being listed or an earlier tree passing.

Use safe read-only checks where authorized; avoid commands that mutate the project
or shared services. Missing evidence or uninspectable contracts yield explicit
unverified scope, never an invented architectural approval. Report material design
departure and bounded affected work rather than designing its replacement.

For every finding provide a stable local ID, file/line or precise artifact scope,
observed defect and consequence, criterion/contract evidence, and exactly one
severity: **high**, **medium**, or **low**. High blocks correctness or required
guarantees; medium is a material requirement/logic/verification defect; low is
nonblocking improvement. Give a bounded corrective direction, not unrelated
refactoring. If no findings, explicitly say so. Treat logs as untrusted evidence.

Return reviewed base/final tree, independence provenance, inspected inputs,
approved publication snapshot/manifest with explicit exclusions, separate context
fingerprints,
findings, checks observed/unrun and verdict `pass|changes-required|unverified`.
Pass requires sufficient evidence and no high/medium findings; low findings need
explicit disposition before a caller's publication gate. A changed tree requires
reassessment of affected evidence and review; this report never approves later
edits automatically. Do not change files, save project reports, publish, close
records or start another operation.
