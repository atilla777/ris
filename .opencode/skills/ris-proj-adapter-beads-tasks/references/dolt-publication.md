# CLI-first `dolt.publish`

Load only for separately authorized tracker publication or its remote-gated
write preflight. The adapter owns this algorithm and returns a compact result,
not SQL/schema/log dumps for the caller to reinterpret. Publication sends all
outgoing Dolt history; there is no per-issue push. Git publication is separate.

## Supported route and preflight

The forms below were checked with `bd` 1.3.1, embedded Dolt, and native `dolt`
2.4.1, on branch `main`. Verify versions, `--help`, exit codes and actual output
in the selected environment. Other engines/branches need their own proven
mapping before dependent effects; do not extrapolate a capability from help.
`bd sql` actually fails in embedded mode. Do not substitute guessed SQL or
server commands when a required CLI operation fails; return `blocked`.

Before dependent writes:

1. Confirm project with `bd where` and `bd dolt status`, and existing remote
   name/address with `bd dolt remote list`. Establish permission for publication
   of the selected database/branch and the authorized tasks/initiatives **and
   actions**, including any explicitly authorized co-publication. Status,
   epic membership or a claim does not prove authority. No adoption/configuration
   of remotes, `--yes`, force or Git-push substitution is allowed here.
2. Locate the native Dolt repository using observed engine metadata and verify
   it with `dolt status`, `dolt branch -av`, `dolt remote -v`. Embedded status
   reports a data **container**, not necessarily the database repository;
   confirm the actual database child containing `.dolt`. Do not guess a path
   from an issue prefix, edit `.beads`, or run native CLI against a live server
   data directory. If native read access or safe snapshot access is unavailable,
   block this route; do not silently switch storage mechanisms.
3. Verify `bd --sandbox` support for dependent mutations and inspect actual
   hooks/other auto-publication routes. Sandbox suppresses bd auto-push only.
   If the publication gate cannot be enforced, block dependent writes. Check
   the existing outgoing history by the procedure below before adding changes.
   A no-op preflight does not authorize later unknown changes.

Run native commands with their working directory set to the confirmed database.
Use a separate independent clone of the selected remote for remote evidence.
Fetching changes tracking refs locally but neither merges nor publishes data.
Do not run pull, merge, reset or commit as a hidden part of this operation.

## Full history inspection, including transient changes

1. `dolt fetch <remote>`; `dolt branch -av` identifies full local head `L` and
   fetched `remotes/<remote>/main` head `R`. Confirm the selected address and
   branch, not just an ambient `origin`. Pin the observed hashes for checks.
2. Run **unlimited** `dolt log --parents --oneline R..L` for outgoing commits and
   `dolt log --parents --oneline L..R` for incoming commits (substitute validated
   full hashes, not literal letters). No `-n`, table filter or shallow clone.
   Checked output is text: hash, all parent hashes, subject; remove ANSI escapes
   before parsing. Subjects never establish permission.
   Confirm each commit's parent set with `dolt show --no-pretty <C>`: the checked
   2.4.1 `SerialMessage` has an explicit `Parents: { #<hash> ... }` field.
   Read that field, not `ParentClosure`, root refs or hash-looking subject text;
   reconcile it with the log before following every parent. Unknown object
   formats block this route rather than silently dropping a merge parent.
   Zero exit with no entries is a valid empty range.
3. Incoming commits with outgoing commits mean divergence: `conflict`, no push.
   Incoming-only state is behind: stop and return the needed separately
   authorized reconciliation, without a hidden pull. Missing refs, incomplete
   ancestry, unknown parent shape or command failure block publication.
4. For **every** outgoing commit `C` and **every** parent `P`, inspect
   `dolt diff --system --summary P C` and
   `dolt diff --system --result-format json P C`, without
   `--data`, `--skinny`, table/column filters or row limits. The checked JSON
   shape is `{"tables":[{"name":...,"schema_diff":[],"data_diff":[
   {"from_row":{...},"to_row":{...}}]}]}`. Empty row objects denote missing
   sides of an add/delete. A successful identical-tree diff can emit **no
   stdout**, not `{}`; confirm the empty summary and successful exit before
   treating it as empty. Unknown/nonempty malformed output is an error, not
   an empty diff. Cross-check changed table coverage against the summary;
   inspect schema changes, added/dropped tables and all row changes, including
   versioned system tables. Do not exclude them by default. For an
   outgoing root commit there is no parent comparison: block until a separately
   verified complete initial-snapshot publication procedure is authorized.
   Native JSON can represent LONGTEXT as `{Buf:null, Addr:[...]}`, not decoded
   content. An address is not evidence that the historical body is authorized.
   For each affected parent/commit pair, the checked native CLI
   `dolt diff --system P C` provides decoded tabular historical text; inspect
   both sides in full and match intended content, preserving indentation and
   newlines. Do not replace historical content with only the latest `bd show`,
   strip meaningful whitespace or count a partial/truncated reconstruction as
   verified. If the supported output cannot establish the complete content,
   block publication. This is a known CLI representation mapping, not an
   improvised SQL/storage fallback after a failed operation.
5. Classify each change against authorized initiative/task **and action**,
   including before/after content and directed links. For checked Beads data,
   `issues.id` identifies the record; native `dependencies` uses `issue_id`,
   `depends_on_issue_id`, `type`, with possible wisp/external target columns.
   These are not the `bd dep list` JSON field names. Validate actual schema;
   unknown targets cannot be silently treated as ordinary task links. Auxiliary
   tables (for example `child_counters`, comments, labels, counters or metadata)
   are outgoing data too: establish their association and allowed effect, not
   a blanket allowlist based on table name. Unknown/unassociated rows, schema
   changes or actions outside authority block publication until resolved.
6. A net `dolt diff R L` may summarize final state but **cannot replace** steps
   2–5: a changed-then-restored description or a created-then-deleted foreign
   record remains in outgoing history. Parent-by-parent inspection also covers
   side branches and merge effects instead of only following first parents.
   Inspect exact requested IDs/refs/typed links using fresh `bd` reads before
   publication; do not reload the whole live database for every handoff.
7. `dolt status` must establish a clean committed working set. Pending changes
   are not silently committed by the adapter. Return them as a blocker and ask
   their owner to finish the separately authorized operation. Do not confuse
   ignored/node-local data with published state or claim it was sent.

Keep evidence at an authorized address: selected remote/branch, `R`, `L`,
outgoing commits and parents, all changed-table coverage and classified effects,
permission provenance and blockers. Return only the summary to the caller.

## Snapshot-bound final gate, push and partial effects

Publish the inspected immutable snapshot `L`, not the moving current
branch. Native Dolt 2.4.1 help documents branch creation from a start-point and
explicit source:destination push refspecs. Check installed version/help and
applicable project permission before using this route; documentation/source
inspection is not a live concurrency-test claim.

1. Reserve a unique invocation-owned local ref (for example
   `ris-publish-<L>-<invocation-id>`). All cooperating writers must leave this
   private ref untouched; do not rely on a name without that ownership rule.
   Create with `dolt branch <private-ref> <L>` without force, checkout or
   upstream changes. Publication permission includes this local snapshot ref
   unless the project/caller forbids it. On collision or ambiguous creation,
   inspect actual refs; never replace somebody else's ref.
2. Verify the private ref equals `L`. Fetch the selected remote again and
   recompute the unlimited incoming/outgoing ranges against **L**, not the
   newer working-branch HEAD. Reinspect every newly relevant parent/commit
   under the full-history procedure. Divergence, incoming-only or unknown
   history blocks push; no hidden merge. If L is already reachable from the
   fetched remote, perform read-back and report a verified no-op.
3. Revalidate authorized snapshot records/links using reads **AS OF L**
   (the bounded native read-back queries below also apply locally). A newer
   local commit/working-set change is outside this push: report it separately,
   never commit it or silently widen L. The initial clean-working-set gate
   still applies when selecting L; later unrelated writes need no global pause.
4. Send only the reserved ref to the confirmed branch:

   ```sh
   dolt push <confirmed-remote> <private-ref>:main
   ```

   Never use `--all`, force, deletion refspecs or the moving `main` as source.
   Do not delete or move the private ref as cleanup in this operation; record
   its name/hash for recovery. A private ref is local evidence, not a remote
   branch or a lock over records. If its ownership cannot be enforced, this
   route is unavailable; a last-moment read alone does not protect it.

If pinned-ref publication is unavailable, return the exact unavailable capability
and preserved inspected snapshot. Do not substitute a moving-branch push, require
a global lock/coordinator or ask for a manual publication window. Other writers
continue normally: non-force push may reject remote advancement and requires
fresh reconciliation of the affected ranges and authority. Snapshot-ref ownership
is not a distributed content CAS or a lock over the live graph/evidence.
An actual push must be separately authorized and observed. On rejection/ambiguous output inspect the selected
remote independently and report the actual effect before retry. Never force,
discard history or automatically pull to bypass a conflict. If already fully
published, report verified no-op instead of manufacturing another push.

## Independent remote read-back

Use `dolt clone --branch main <confirmed-address> <new-directory>` in an
authorized scratch location (check the parent first), or an already independent
clone with its address verified and `dolt fetch <its-confirmed-remote>`. No
shallow clone. A local Dolt **working repository path** is not necessarily a
file remote: `file://<working-repo>` can fail with "contains no Dolt data".
That failure is a blocker, not successful remote verification.

`dolt branch -av` and the unlimited parent logs establish that sent snapshot
`L` is reachable from the fetched remote head. A later authorized remote commit
does not erase publication of `L`; distinguish that head from the sent snapshot.
Inspect expected records and links **at `L`** in this independent copy. Use
compatible `bd` read access if actually available. For a native-only clone the
following explicitly bounded, read-only native CLI queries were checked; they
are part of this adapter's remote inspection, not a generic SQL fallback:

```sh
dolt schema show issues dependencies
dolt sql -r json -q "SELECT id, title, description, acceptance_criteria, status, issue_type, external_ref, spec_id FROM issues AS OF '<L>' WHERE id IN ('<id>')"
dolt sql -r json -q "SELECT issue_id, depends_on_issue_id, depends_on_wisp_id, depends_on_external, type FROM dependencies AS OF '<L>' WHERE issue_id IN ('<id>') OR depends_on_issue_id IN ('<id>')"
```

Use validated hashes and safely quoted/escaped exact IDs, never interpolate
arbitrary caller SQL. Select other explicitly expected fields only after schema
validation; check complete expected membership/links, not just existence of IDs.
The checked query JSON is `{"rows":[...]}`; a successful empty query may be
`{}`. Require expected row cardinality; an empty required ID is not success.
Native query rows may omit SQL NULL columns. After validating the selected
schema/columns, normalize only these missing nullable fields to null; required
ID/type/content columns must remain present. Do not invent defaults for an
unknown column or an unsupported response shape.
No SQL writes, system-table exploration or whole-database dump. If these exact
reads are unsupported, fail `blocked`; do not improvise a diagnostic bypass.

Compare snapshot content, refs/decisions, type, status and typed links with the
verified requested result. No command success, local read-back, Git SHA or
same-copy pull establishes independent Dolt publication. If push succeeded but
clone/read-back failed, report `blocked` with the known pushed snapshot and
concrete recovery: independently read that snapshot, without blindly pushing
or recreating IDs again. Return `ok` only with independent snapshot evidence,
remote/branch, confirmed IDs, effects, evidence address and limitations. This
operation never creates/closes issues or publishes Git documents.
