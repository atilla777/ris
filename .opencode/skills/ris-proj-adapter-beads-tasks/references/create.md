# Create and reconcile

Read before epic/task creation, with `concurrency.md` and main typed reads.
Require approved type (`epic` or `task`, ordinary native `bug` only under
`standalone.md`), supplied title/content and stable retry identity/expected absence.
Creation needs caller authority, not merely a record in a list. `bd create --json`
returns an object with `id` in the checked version; validate the actual response.

Search all relevant records (including closed) for the caller's
stable identity and compare content/parent; for a feature also search slug
and spec association across all project tasks, using `feature-record.md`
when supplied. An exact confirmed prior creation
returns the existing ID, ambiguous matches are a `conflict`. An authorized
creation defaults to best-effort without a separate concurrency-risk question:
`bd` does not enforce unique external references, so concurrent creators can
still make duplicates. Do not claim a no-duplicate guarantee from the search
and read-back. If the caller explicitly requires that guarantee, require a
proven native uniqueness mechanism covering all relevant creators;
without it report the exact limitation and stop `conflict`, without a pause request. Run `bd create
--type epic|task --title ... --description ... --acceptance ... --json`
with only supplied fields (optional `--external-ref` or `--spec-id` for
identity; neither is a uniqueness constraint). Prefer `--parent <id>` for
a child only after checking the parent. Extract the returned ID, `show` it
and verify content and parent, then repeat the full all-state identity search
(including feature key/slug/spec) to detect concurrent collisions. Return
`conflict` with persisted IDs for a duplicate; never silently pick one.
On uncertain creation, re-list all records
and reconcile the stable identity before another attempt. With no reliable
identity evidence, do not retry an ambiguous create: `conflict`.

For common `tasks.items.create`, require a confirmed open epic as parent of a feature
task, or a confirmed open feature task as parent of a direct child. Require
caller-approved task content, a stable retry key and expected absence; for
the feature also require the exact accepted-spec link and a verifiable
address of the acceptance decision (do not infer acceptance from a file or
`--spec-id`). Persist that address in the approved description, or verify it
is accessible in the linked specification, and reread it on return/retry.
If the evidence cannot be retrieved or does not match the accepted version,
report `blocked` rather than declaring acceptance. Use
`--type task --parent <id>` with supplied content and `--external-ref` for
the stable key; use `--spec-id` only when the caller supplied it and retain
the exact link in the approved description or other readable field. Scope
child keys to their feature parent and feature keys to their epic/goal; a
globally reused raw key is insufficient. On retry, compare key, type,
parent, content, spec link and acceptance evidence address for a feature,
including all-status records. Reuse only an
exact match; changed content, moved parent, closed parent or multiple matches
are `conflict`, not permission to update. Verify the new child's `parent`,
typed `parent-child` edge (child → parent), parent direct-child selection,
and the reread content. For a feature verify the epic and the same membership.
A feature with no children needs no artificial child. If strict no-duplicate
creation is requested, require proven native support or report the unsupported
guarantee before creation: `--external-ref` is not
unique in Beads. If a multi-child request partially succeeds, reread every
affected ID, return the persisted IDs and stop further writes on the first
failure; on retry reconcile all existing children before creating missing ones.
