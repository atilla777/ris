# Beads-specific bug investigation persistence and disposition

Read before report/acceptance persistence, duplicate relation or investigation
disposition-close. Registration does not need this resource. Apply main typed
read/reconcile, `standalone.md` native supplementation and `concurrency.md` before
writes. These are bounded ordinary capabilities, not tasks v1 or feature-record/1.
The investigator owns proof, agreed criteria, useful delta and disposition
authority; this adapter checks supplied evidence/permissions and actual effects.

## Advertise the requested predicates

Support ordinary native bug **report persistence**, **acceptance persistence**,
**duplicate relation**, **disposition exact close**, and read-only **children and
blockers inspection for disposition** under the conditions below. Report each
operation's actual support/protection before its dependent write. Bug claim,
composition and execution completion are not added by this resource. Require
selected workspace, exact bug ID/expected type, caller authority, expected current
content, allowed fields and result; for duplicates also exact original ID/type,
proof, approved useful supplement or verified no useful delta, and scoped retry
identity. Never infer substantive duplicate proof from a link or similar title.

## Current report and acceptance: protected replacements

Require one caller-approved current description section with stable project/bug
identity, version, investigator and inspected code revision. Preserve the original
message and every foreign section byte-for-byte; ambiguous section boundaries or
changed content return conflict. For file-backed reports require a summary and
retrievable exact published Git revision/path instead, with no competing full
current copy. Preserve history and unrelated acceptance/decision pins. The adapter
does not accept new behavior or author diagnosis.

Inspect installed command/backend support for **real protection of changed and
preserved content**, including description and acceptance, before replacement.
This investigation contract explicitly requires that protection: ordinary bounded
fresh compare/write/read alone is insufficient. Prefer a supported safe native
operation or already established applicable coordination whose coverage is proven.
Status/assignee guards, claim/lease, worktree, sandbox, a returned revision or
multiple fresh reads are not content CAS. Baseline 1.3.1 exposes no general CLI
revision CAS. If no applicable provider exists, return `conflict` with the exact
unsupported predicate before its write; retain research and settled effects. Do
not invent flags/locks, install a coordinator, upgrade Beads, pause writers or use
raw storage writes. Do not substitute append-only notes for the current report.

With actual protection, fresh-read and compare expected content, prepare only
authorized description/acceptance fields and apply `update.md` with that provider's
supported conditions and sandbox. Do not replay the whole issue. Treat report and
acceptance as separate effects even if passed together; do not assume cross-field
atomicity. Independently read both after success, failure or ambiguous output;
verify exact desired content and preserved sections/pins. Return each as saved,
unchanged, missing, conflicting or unknown. A saved report with old/missing criteria
is a partial result, not fully saved fix inputs. Before retry reconcile both,
reuse exact settled fields and protect only remaining authorized changes. Same
identity/version with different content is conflict. Never roll back by replaying
an old snapshot or overwrite a newer/foreign report to complete a partial pair.

## Proven duplicate: original, readable meaning and typed relation

Exact-read distinct duplicate `bug` and original (native `bug` or explicitly
authorized legacy ordinary `task`), including status/content/typed edges. Other
types are unsupported. Preserve any task feature payload; this branch grants no
feature operations. A closed original is not reopened. Recheck that supplied proof
and useful delta apply to the inspected records; do not choose an original.

1. Preserve useful new information in the original via standalone's native
   `bd --sandbox update <original-id> --append-notes <supplement> --json`.
   Use a stable identity scoped to project/duplicate/original/report and approved
   exact content. Verify marker AND content/occurrences before and after append;
   exact existing effect is unchanged, same marker/different content is conflict.
   No useful delta requires an explicit checked explanation, not a token append.
   Native append preserves foreign notes but is not concurrent append-once.
2. Verify stored rationale in the duplicate's current report/summary explicitly
   says **proved duplicate of <original-id>**, with evidence; a generic relation
   does not express this meaning alone. If that report write is blocked, do not
   proceed to relation/close. Read any prior relation before attempting another.
3. Inspect installed `bd dep add --help`: baseline supports `related`, not a
   `duplicate` type. Use `bd --sandbox dep add <duplicate-id> <original-id>
   --type related --json` with normal cycle checks, never default `blocks` or an
   invented `--type duplicate`. This is a nonblocking related edge whose duplicate
   meaning is supplied by the readable proof. Independently inspect typed directed
   edges (using main normalization): exact source duplicate, target original,
   type `related`. Existing exact edge returns unchanged; reverse/unknown edge
   shape is not proof of the requested direction and must be reconciled. Do not
   remove/replace foreign edges or turn similarity into a duplicate relation.

On any failure stop remaining writes and exact-read both records and edges.
Return original supplementation/no-delta, stored rationale and typed relation
individually. An ambiguous append/add is reconciled before retry, not repeated
blindly; already verified effects are reused. No multi-record transaction or
exactly-once claim is made. Closure cannot run until all prerequisites are checked.

## Separate exact disposition-close

This branch resolves only one message as **proved correct/not a bug** or **proved
duplicate**. Require caller's evidence and authority plus persisted matching
rationale/current report (or its exact published file); for duplicate require
verified original useful-information preservation/no-delta and typed relation.
Insufficient confirmation, failed reproduction, an unknown cause or a pending
fix cannot enter this branch. It does not assert fix AC completion or require
publication of a fictitious fix. Main task/feature completion retains its own
scope, acceptance and real publication evidence requirements.

Freshly inspect `bd list --parent <bug-id> --all --limit 0 --brief --json` and relevant
descendants, plus `bd dep list <bug-id> --type blocks --direction=down --json`.
Validate IDs/types/parent and normalize blocked → blocker. Failed/truncated reads
are not empty sets. Reconcile caller's complete expected composition, evidence
and status immediately before close; refuse unfinished children or active blockers.
Use `bd --sandbox close <bug-id> --reason <proved-disposition-and-evidence> --json`
with one exact ID, no force, status-update shortcut, auto-next or ancestor closure.
Native transactional direct-child/blocker checks cover those predicates, not
external-evidence freshness or a graph-wide freeze. Native refusal remains blocked.

Independently read closed status/reason, matching rationale, complete relevant
children/blockers and, for duplicate, original content and typed relation. An
already closed exact disposition is verified unchanged; unexpected closure is
conflict, never reopen. After ambiguous response inspect actual status/reason
before retry. Report saved-report, acceptance, original, relation and exact-close
effects separately with provider/covered predicates/limits and main status envelope.
Local closure is not tracker publication. Stop on partial failure with actual
effects and exact remainder; never repeat successful effects merely to rerun the
chain or silently proceed after a conflict.
