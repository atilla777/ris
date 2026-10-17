# One bounded field update

Read before an update, together with `concurrency.md`. The main adapter owns
workspace/typed reads and result reconciliation. Require exact ID/type, explicit
ordinary kind when using ordinary task capabilities, authority, approved target
fields and fresh expected values. A title/priority/independent metadata edit does
not require accepted source versions, composition, blockers or delivery evidence
unless the caller's actual predicate depends on them. Ordinary task source/accepted-
content updates additionally apply `standalone.md`; feature-record changes apply
`feature-record.md`, investigation replacements `investigation.md`.

Use `bd update <id> --title/--description/--acceptance/... --json`
only for explicitly supplied fields, never send a whole stale snapshot.
A request to set `status: closed` (or any configured done status) is always
**Complete** under `completion.md`, regardless of `bd update --status`;
apply its full checks. Entering `in_progress` as a claim uses `claim.md`,
not an unguarded status/assignee update. Never use `--force`.
`--if-status <expected>` and `--if-assignee <expected>` are atomic guards
ONLY on those fields (guard mismatch exits 13 when all failures are stale).
They cannot protect title, description, labels, parent or arbitrary content
against concurrent changes while status/assignee remain equal. There is no
`--if-revision` in baseline 1.3.1 help. Apply `concurrency.md`:
native merge operations for appends/key edits and applicable native conditions.
Freshly compare expected content before preparing a bounded field replacement;
verify it and preserved fields afterward. This is not universal lost-update
protection; unsupported explicitly requested stronger guarantees return a precise
limitation, not a request to pause writers. Preserve unrelated prose and fields.
Avoid multi-ID updates: they can partially succeed. `bd update --json` returns
an array; validate actual response and independently read back the exact result.
Reconcile ambiguous append/key/replacement effects before retrying.
