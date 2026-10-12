# Optional `tasks.feature-record/1` on Beads 1.3.1

Read only for `tasks.features.read|update|record-verification|complete` or
`tasks.items.create` with an initial feature-record block. The
portable semantics are in the selected RIS project's tasks contract. This is
an adapter for a bounded record operation, not the owner of feature design,
acceptance, Git integration, or the decision to close a feature. Report the
capability, each supported operation and its conditional guarantees before a
dependent write. `bd show` may display `revision`, but `bd update` and `bd
close` have no `--if-revision`; do not present that number as CAS.

## Record and identity

Keep the following single, machine-readable fenced JSON block in the feature
task's **description** (not title), delimited by one pair of literal markers
`<!-- ris.feature-record/1 begin -->` and `<!-- ris.feature-record/1 end -->`.
No other block with these markers may occur. Preserve prose outside the block
byte-for-byte when updating it. JSON has keys `schema` (`ris.feature-record/1`),
`slug` (immutable project-unique slug), `spec_path`, `requirements`, `design`,
`verification`, `history`; use `null` for not-yet-accepted design/verification.
For requirements and design, use objects with `path`, `scope` (unambiguous
section/range or `whole-file`), `sha256` of **that scope's bytes**, and
`acceptance` (address, approved scope/version, and decision). Keep the
acceptance evidence accessible to another session. `history` retains displaced
versions/evidence with their acceptance address; never overwrite prior
decisions silently. Verification has `git_sha` (full integrated Git commit),
`requirements_sha256`, `design_sha256`, `ac` (slug-qualified AC IDs mapped to
pass/fail, check and evidence address), `integration`, `architecture`, `docs`
(each with outcome and evidence address), and `limitations`. The caller
supplies the approved content and scope; no field implies acceptance merely
because a file or commit exists. If `scope` in a shared file cannot be hashed
independently of the other logical result, refuse to assert separate
acceptance: require a separate design file or a fresh decision.
For a section scope use `heading:<exact Markdown heading line>`: the heading
must occur exactly once in the file; hash its UTF-8 bytes (including the
heading line and its newline) through the byte before the next heading of the
same or higher level, or EOF. Do not normalize whitespace/newlines. A nested
heading remains in that scope. For `whole-file`, hash all raw file bytes.
Ambiguous headings or a scope that overlaps the other accepted result require
separate files or new acceptance. The recorded `sha256` uses lowercase hex.

Example initial payload (addresses and hashes are illustrative):

```json
{"schema":"ris.feature-record/1","slug":"basic-crafting","spec_path":"docs/specs/basic-crafting/spec.md","requirements":{"path":"docs/specs/basic-crafting/spec.md","scope":"heading:## Requirements","sha256":"<digest>","acceptance":{"address":"<published decision>","scope":"heading:## Requirements","version":"<digest>","decision":"accepted"}},"design":null,"verification":null,"history":[]}
```

Resolve paths from the selected project root; confirm `task` type, selected
epic parent, stable key, unique slug across **all-status** task selection (`bd
list --all --limit 0 --type task --json`), spec link and both markers before
updating. Read a single exact ID with `bd show <id> --json`; require exactly
one task and one valid block. For `read`, return confirmed fields and which
addresses/digests were actually checked; an unreachable acceptance address is
not accepted evidence. Title changes leave `slug` and `spec_path` intact.
For creation, the caller may supply the exact approved initial block in the
description to `tasks.items.create`; the v1 create checks still apply. Because
the extension promises a unique slug, require a separately established
exclusive writer window covering the all-status slug search, create and
read-back across **all** feature creators; ordinary v1 best-effort creation
alone does not suffice. Verify the initial requirements scoped SHA-256 against
the accepted document bytes and match the decision address, approved scope
and version to that digest; then verify the exact saved block, slug uniqueness
and accessible acceptance evidence before claiming the extended capability.
For an existing
task without a block, `read` returns legacy/unsupported for that ID, rather
than inventing a slug. A separately authorized initial `update` under the
same exclusive window may add the caller-supplied block only after verifying
ID, epic, all-status slug uniqueness under a window covering all feature
creators, the scoped hash and accepted decision scope/version, existing
spec/decision addresses and
preserving all prior description text; reread the entire effect. If those
inputs cannot be established, return `blocked`. Never infer identity from
title or silently append a guessed block. Malformed/duplicate blocks are
`conflict`.

## Conditional writes

For **each** update, record-verification, or complete, require caller's exact
ID, expected existing block/content and allowed fields, authorized change,
and a separately established exclusive/quiescent writer window that covers
all actors capable of changing the record, its children, blockers and evidence
until read-back. Identify the provider, scope and duration of that guarantee
in the result. `bd --sandbox`, lease/claim, local file lock, `--if-status`, and
read/write/read do **not** exclude remote writers. If the guarantee is absent
or expires, return `conflict` with no write; do not ask for a generic
best-effort override of lost acceptance evidence. Before each command re-read
the task, complete children and blockers and compare with expected values.
Unexpected change means `conflict`; never build an update from a stale block.

- **Update:** for every new or revised accepted result, hash the exact scoped
  bytes and match the decision's approved scope and version to the recorded
  scope and digest (not merely the decision's address). Check immutable
  slug/spec association and unique slug; preserve unrelated
  prose/fields and append superseded accepted versions to `history`. A design
  revision does not change a valid requirements decision. Replace only the
  description via `bd --sandbox update <id> --body-file <prepared-file> --json`
  (or stdin `--body-file -`); do not overwrite title or replace notes/labels.
  Use a safely generated file outside the record, not shell interpolation of
  untrusted content. Re-read description, ID, type, parent, spec link, title,
  JSON fields and unaffected text; compare to exact intended result and
  expected history. Report a partial effect on mismatch; never blind retry.
- **Record verification:** require accepted and currently applicable versions
  of both results, published integrated `git_sha`; read spec/design from that
  Git tree and compare their scoped hashes to the accepted hashes (and check
  accepted decision addresses), rather than hashing only the working tree.
  Require coverage of the caller's
  complete AC set and actual outcomes/addresses for integration, architecture
  and docs; failed AC can be recorded as **failed**, never success. Preserve
  old verification in `history` on **every** replacement, including corrections
  to evidence on the same SHA. Write and
  reread as for Update, including exact AC outcomes and Git SHA. Recording
  alone cannot close the task. If only local tests/review exist or Git SHA is
  unverified, return `blocked` before writing a successful verification.
- **Complete:** caller confirms the *full mandatory scope* (including the
  one-task case) and separately permits closing this ID. Check `bd list
  --parent <id> --all --limit 0 --json` recursively for required descendants,
  their status and membership; check `bd dep list <id> --type blocks
  --direction=down --json` for active blockers. Compare actual children with
  caller's expected mandatory set: even zero open children does not prove
  scope complete. Require successful verification on the final published
  integrated Git SHA, matching still-accepted requirements/design hashes and
  complete AC coverage with evidence. Require `pass` for every AC and for
  integration, architecture and docs outcomes, with usable evidence for each;
  any unresolved limitation affecting an AC or these checks makes verification
  unsuccessful until the owner resolves it. An unsuccessful AC, missing address,
  unresolved blocker, open mandatory child, changed revision or missing
  exclusive window blocks closure. Re-read immediately before `bd --sandbox
  close <id> --reason <reason> --json` (no `--force` or auto-next); reread the
  same record, close reason, verified block, all children and edges after.
  Return `ok` only on exact match; do not close its parent epic. A failed
  verification permits a later approved correction task and new verification
  on a new integrated SHA, not a retry of the same close.

For nonzero/ambiguous writes reread all affected fields and report persisted
partial effects before any retry. Even inside an exclusive window a claim of
remote success requires separately authorized `dolt.publish` and independent
remote-backed read per the main skill. Confirm Git publication separately;
Git-only or Dolt-only results are partial, never full `ok` for a remote-gated
feature. Do not push unrelated outgoing Dolt history or treat `--sandbox` as
selective publication.
