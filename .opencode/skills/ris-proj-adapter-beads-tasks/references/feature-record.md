# Optional `tasks.feature-record/1` on Beads 1.3.1

Read for `tasks.features.read|update|record-verification|complete`, or
`tasks.items.create` with an initial feature-record. The caller owns feature
content, acceptance, integration and completeness decisions; this adapter
checks references and persists only the authorized tracker result. Advertise
each operation and its conditional guarantees before dependent writes.
`bd show`'s `revision` alone is not CAS. Baseline 1.3.1 help has no
`--if-revision`; detect actual installed capabilities before dependent writes.

## One current payload, Git-owned history

Keep one fenced JSON object in the task **description**, between literal
`<!-- ris.feature-record/1 begin -->` and `<!-- ris.feature-record/1 end -->`.
Preserve all surrounding prose byte-for-byte. The object has exactly these
top-level keys: `schema: "ris.feature-record/1"`, `slug`, `spec_path`,
`requirements`, `design`, `verification`. Slug and spec association remain
immutable; title changes do not change them. `requirements` is required;
not-yet-accepted `design` and not-yet-recorded `verification` are `null`.
Git holds displaced documents and decisions; do not add `history` to Beads.

Each non-null requirements/design reference has:

```json
{
  "path": "docs/specs/example/spec.md",
  "revision": "<full published Git commit>",
  "section": null,
  "acceptance": {
    "address": "<published immutable Git decision address>",
    "decision": "accepted"
  }
}
```

Paths resolve from the selected project root, not the skill installation.
`revision` is the complete Git object ID, not a branch, tag or abbreviated SHA.
`section: null` means the whole file; otherwise it identifies one unambiguous
semantic section (for example `Requirements / Failure behavior`). It is not a
byte range, mandatory Markdown heading syntax, digest or EOF boundary.
Requirements and design can occupy separate sections of one file or separate
files. Require independent identifiable results; refuse ambiguous/overlapping
selectors that prevent establishing which content was separately accepted.

The immutable decision address identifies the Git repository, full decision
commit, path and, if needed, unique decision section. A commit-pinned blob URL
is one possible form; a branch URL or local note is insufficient. Fetch/read
the decision at that commit. Each result has its **own** acceptance decision,
even when both decisions share a file/commit. It explicitly names the accepted
content path, section (including null for whole-file), revision and an accepted
decision attributable to the authorized acceptor. Do not infer acceptance from
the existence of a file or commit.

The decision may use literal `containing-commit` for the **content revision**
only when its content is in the same commit as the decision. Resolve that
literal to the full commit pinned by the immutable decision address, and
compare it with the reference's full `revision`. This avoids a circular
self-hash: the tracker stores the full commit after publication; the decision
inside that commit need not contain its own hash. The tracker reference itself
never uses `containing-commit`.
Pin the commit that actually recorded this decision for its accepted content.
Copying an unchanged decision into a later commit does not renew acceptance or
rebind `containing-commit` to changed content. Keep the original pinned decision
address/reference; for carried historical text, name its original full content
revision or clearly link that original decision. Check Git decision history when
the pinned address could be a later copy, and block an unsupported rebind.

Check the actual document at `revision` (for example `git show <sha>:<path>`),
resolve the selected section semantically and match the decision's path,
section and resolved revision. Establish that both commits are published in
the selected Git remote using fetched remote evidence, not only local object
existence. Record checked addresses/revisions and publication evidence. Missing
content, unreachable decision, ambiguous section or unconfirmed publication
blocks a dependent write; a syntactically valid reference alone is not enough.

Example initial payload (placeholders require real published values):

```json
{"schema":"ris.feature-record/1","slug":"basic-crafting","spec_path":"docs/specs/basic-crafting/spec.md","requirements":{"path":"docs/specs/basic-crafting/spec.md","revision":"<full published Git commit>","section":"Requirements","acceptance":{"address":"<immutable requirements decision>","decision":"accepted"}},"design":null,"verification":null}
```

`verification` contains `git_sha` (full published integrated commit),
`requirements` and `design` (the exact accepted reference objects above), `ac`
(slug-qualified AC IDs mapped to outcome, check and evidence address),
`integration`, `architecture`, `docs` (each with outcome and evidence address),
and `limitations`. These are current references/evidence, not a copied decision
history. Recording failed checks is allowed; it does not permit closure.

## Reads, historical data and creation

Read exactly one matching `task` via `bd show <id> --json`. Confirm selected
epic parent, stable key, spec link and marker cardinality. Return actual data
and which references/content/decisions were checked; unverified references
must be labeled. Duplicate/malformed blocks are `conflict`.

The former payload with `scope`, `sha256`, digest-based verification or
`history` is **historical/unsupported**, despite the same markers/schema.
Return its unchanged data and explicit diagnostics: current operations cannot
use it as accepted input. A task without a block is likewise unsupported.
Use the main result envelope with `status: blocked` and a
`historical/unsupported` diagnostic, not an alternate operational schema;
include the inspected ID and unchanged payload so the data remains readable.
Do not reinterpret the old fields, silently drop history, append a guessed
block or migrate on read/retry/update. An explicitly authorized migration of
one old record is a separate operation outside this current write protocol;
there is no dual-schema API or `/2` fallback. Block dependent writes and leave
the historical record intact.

For initial create, validate the approved block and published requirements
(and design if supplied), then apply main-skill v1 create checks. Search the
complete **all-state project task set**, not only the selected parent:
`bd list --all --limit 0 --type task --json`. Compare stable key **and**
slug/spec association: collect candidates matching any of key, slug or
specification path/link, including historical blocks. A match on just one
dimension is not absence. Require one exact match on key, type, epic, slug,
spec link, approved content and all accepted references/decisions for reuse.
Different values, multiple matches or unsupported candidate input are an
explicit collision/diagnostic, never permission to overwrite or create again.
If a candidate lacks a parseable identity, inspect it; do not infer a slug
from its title or declare an incomplete search clean.

Ordinary creation is **best-effort collision detection**, without a global
exclusive window or a separate risk question. `--external-ref`/`--spec-id`
are not unique constraints. After `bd --sandbox create ... --json`, read the
returned ID and repeat the **full** key/slug/spec search; verify the epic and
membership. A concurrent duplicate yields `conflict` with every known
persisted ID, not a uniqueness claim. Never delete a duplicate automatically.
After ambiguous command output, do the same reconciliation before retry.
Strict uniqueness is required only if the caller explicitly demands it; then
establish a real guarantee over all feature creators for search/create/check,
or return `conflict` before creating. Exact reuse does not reopen a closed
record or imply readiness/completion.

## Bounded existing-record writes

For update, verification and complete require exact ID, expected current
content and allowed fields. Apply `concurrency.md` from this resource's directory:
freshly compare the exact block and surrounding prose, use applicable native
conditions and only the approved description replacement, then independently
read back the block, preserved prose and relevant composition/blockers. Check
pinned external evidence for applicability before dependent writes. No manual
window or atomic transaction over record, graph and external evidence is required.
Claims, leases, sandbox, status-only guards and read/write/read are not universal
lost-update protection. Name the actual native guarantees and limits; if a stronger
atomic guarantee is explicitly required but unsupported, return its exact limitation
before writing. Unexpected content/ownership/structure changes conflict; never
overwrite a changed acceptance block or silently rebind its pins.

- **Update:** check every new accepted reference and its actual content/decision
  as above. Preserve immutable slug/spec, unrelated prose and fields. On a
  design-only update preserve the entire old requirements reference, including
  its acceptance address and revision. Compare actual applicable requirements
  at that old revision with the new design's revision: inspect `git diff
  <old> <new> -- <requirements-path>` and the relevant semantic section in both
  trees. Changes elsewhere in a shared document do not automatically invalidate
  requirements; same path/section labels alone do not establish equivalence.
  Record applicability evidence; unresolved or material requirements changes
  return `blocked` to their owner for a new acceptance/reference. Do not invent
  a new requirements acceptance or rewrite the old ref to the latest commit.
  For an authorized requirements change, require its new separate decision
  and check design applicability rather than assuming the old design remains
  valid. Any changed result reference invalidates existing verification: set
  it to null unless fresh applicable verification is explicitly authorized.
  Write only the prepared description using `bd --sandbox update <id>
  --body-file <prepared-file> --json` (or stdin `--body-file -`), never stale
  notes/title/labels. Reread the entire description and unaffected fields.
- **Record verification:** require accepted applicable requirements/design,
  confirmed published integrated `git_sha`, complete caller AC set and actual
  outcomes/evidence. At that Git tree, compare the actual applicable content
  with each accepted reference (diff plus semantic section review, not working
  tree or digest-only assertions), and read the separate decisions. Store the
  exact refs in verification; preserve them in the feature record. Replace
  only authorized current verification, without adding history. Failed ACs
  stay failed; local-only tests or unconfirmed Git publication cannot establish
  successful integrated verification. Reread refs, SHA and exact outcomes.
- **Complete:** the caller confirms full mandatory scope (including one-task
  with no artificial child) and separately authorizes closure of this ID.
  Read unlimited children recursively and typed active blockers; compare with
  expected mandatory membership, not just zero open children. Require current
  successful verification on the final published integrated SHA, exact matching
  accepted refs, applicable content and complete AC coverage. Every AC and
  integration/architecture/docs outcome must pass with usable evidence; no
  unresolved limitation may undermine these checks. Open mandatory children,
  missing scope/evidence, changed inputs or blockers block
  closure. Reread immediately before `bd --sandbox close <id> --reason <reason>
  --json` without force/auto-next, then verify record, reason, children/edges
  and unchanged block. Never close its epic automatically.

On ambiguous/nonzero writes, reread actual effects before retry and return
persisted effects, actual stopping cause and exact remainder with causal
`blocked|conflict|error`, never a standalone `partial` status. Git publication and separately authorized
`dolt.publish` with fresh selected-remote revision/reachability confirmation are
separate facts; local exact-content read-back is not remote field equivalence. A local
record write, Git-only or Dolt-only publication cannot mean full remote success.
