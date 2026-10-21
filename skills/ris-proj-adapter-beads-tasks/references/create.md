# Create and reconcile

Read before epic/task creation, with `concurrency.md` and main typed reads.
Require approved type (`epic` or `task`, ordinary native `bug` only under
`standalone.md`), supplied title/content and stable retry identity/expected absence.
Creation needs caller authority, not merely a record in a list. `bd --sandbox create --json`
returns an object with `id` in the checked version; validate the actual response.

Search all relevant records (including closed) for the caller's
stable identity and compare content/optional parent and actual known source
associations. Disclose the fields needed for those predicates, including legacy
prose when relevant; unknown is not absent. No feature registry schema or global
slug/spec scan is required. An exact confirmed prior creation
returns the existing ID, ambiguous matches are a `conflict`. An authorized
creation defaults to best-effort without a separate concurrency-risk question:
`bd` does not enforce unique external references, so concurrent creators can
still make duplicates. Do not claim a no-duplicate guarantee from the search
and read-back. If the caller explicitly requires that guarantee, require a
proven native uniqueness mechanism covering all relevant creators;
without it report the exact limitation and stop `conflict`, without a pause request. Run `bd --sandbox create
--type epic|task --title ... --description ... --acceptance ... --json`
with only supplied fields (optional `--external-ref` or `--spec-id` for
identity; neither is a uniqueness constraint). Prefer `--parent <id>` for
a child only after checking the parent. Extract the returned ID, `show` it
and verify content and parent, then repeat the full all-state identity search
for the relevant stable identity to detect concurrent collisions. Return
`conflict` with persisted IDs for a duplicate; never silently pick one.
On uncertain creation, re-list all records
and reconcile the stable identity before another attempt. With no reliable
identity evidence, do not retry an ambiguous create: `conflict`.

For early feature registration approved title/goal and stable project-scoped key
suffice. Create native task content, without JSON, duplicate accepted refs or
ready/verification fields. Epic is optional; validate a supplied epic's type/open
status and omit --parent when absent. Omit --spec-id when no actual source link
exists; do not manufacture one. A known exact ID is read/reused, not created again.

For decomposition children require a confirmed open feature parent and caller's
sufficient accepted scope/criteria, source/decision inputs and stable parent-scoped
key; early-registration permission does not waive child-input readiness. The caller
checks actual acceptance in documents, not a registry/--spec-id flag. It also
distinguishes decomposition sufficiency from execution readiness: a sufficiently
defined accepted future prerequisite can support child creation before its
implementation, with necessary directed blocks verified through `structure.md`.
Unknown/disputed required contracts or a blocker applicable to the creation
action stop the dependent write, not independently sufficient authorized work.
The adapter does not infer execution readiness from creation or bypass native
refusal, ownership or caller-supplied scope guards. Use supplied
`--type task`, optional confirmed `--parent`, `--external-ref` and ordinary content;
existing explicit links may be retained but do not duplicate accepted-reference
objects. On retry compare key/type/parent/content/actual source association across
the relevant all-status set. Changed content, moved/closed parent or ambiguous
matches is conflict, not update permission. Verify child parent, typed parent-child
edge (child → parent), complete parent-child selection and reread content; check
an optional epic association similarly.
A feature with no children needs no artificial child. If strict no-duplicate
creation is requested, require proven native support or report the unsupported
guarantee before creation: `--external-ref` is not
unique in Beads. If a multi-child request partially succeeds, reread every
affected ID, return the persisted IDs and stop further writes on the first
failure; on retry reconcile all existing children before creating missing ones.
