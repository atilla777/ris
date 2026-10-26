# CLI-first `dolt.publish`

Load only for separately authorized tracker publication or its remote-gated
write preflight. The adapter owns this route, outside `tasks` v1. Publication
sends shared project `main` history under its standing policy or explicit
shared-history authority, including neighboring records; there is no per-issue push. Git publication,
local record writes and exact completion are separate effects.
“Separately authorized” means independently established authority for this effect,
not necessarily a separate user message. A full parent operation may authorize
publication of its tracker result; pass its attributable scope through this gate.
It does not by itself authorize neighboring history. Use the accepted shared-history
policy or explicit coverage below, preserving any project requirement for additional
approval. Missing coverage returns the exact decision to the lead, or a specific
question on direct invocation, not an invented local-only endpoint.

## Establish project, destination and authority

The CLI forms were inspected with `bd` 1.3.1, embedded Dolt and native `dolt`
2.4.1 on `main`. Reuse checked versions/help in an unchanged tool/engine context;
verify missing capabilities and actual output. Another
engine/branch needs a proven mapping before dependent effects. Failed commands
are not empty results. Do not invent SQL or parse storage objects as a fallback.

1. Confirm the selected project with `bd where` and `bd dolt status`, and the
   existing remote name/address with `bd dolt remote list`. Locate the native
   database repository from observed engine metadata; embedded status names a
   container, not necessarily its database child. Verify actual `.dolt` location,
   `dolt status`, `dolt branch -av` and `dolt remote -v`. Do not guess from an
   issue prefix or run native CLI against a live server data directory. Missing
   safe access blocks dependent work. Run native commands in the verified database.
2. For a new push or dependent record mutation only, establish authority for
   shared project `main` history in that destination:
    use the selected project's accepted standing shared-history policy when
    available, otherwise explicit authority for agreed tasks/initiatives and
    permitted actions. A standing policy may authorize the whole accumulated
    shared history, including neighboring tasks, without approval per ID/commit.
    Record its source; do not automatically install RIS repository policy in
    another project. Respect narrower permissions and explicit exclusions.
    Status, epic membership or claim alone is not authority. Uncovered scope,
    conflicting policy or actions outside permission block dependent publication;
    ask only the necessary substantive scope question, not a technical reapproval.
   Co-publication gives no right to edit, accept or close another agent's records.
3. At entry to remote-gated record work, establish sandbox/hooks, destination,
   shared scope and publication feasibility once, or consume sufficient checked
   results. Recheck affected facts on tool/workspace/target/policy/hook changes;
   do not fetch/recheck remote history for each local record write. Actual push
   retains fresh confirmation/direction/authority gates below. Sandbox suppresses
   bd auto-push, not concurrent writers; preflight expands no policy.

Do not configure/adopt remotes, use `--yes`, force, deletion/`--all` push, or
silently pull, merge, reset, commit, checkout or change upstream. Fetch changes
tracking refs only. No private snapshot ref, new clone, full-row semantic
comparison, SQL AS OF, per-commit/parent audit or substitute mandatory all-row
net-diff audit is required. Ordinary scope checks use the supplied agreement and
fresh relevant task facts, not reconstruction of every historical action.
Confirmation-only needs project/destination/safe-read checks, not renewed
authority for later local/remote work; apply write-only gates only after S is
proven absent below.

Use native `dolt fetch --silent` and `dolt push --silent` to suppress routine
progress only. Preserve stderr, exit status and the final verified revision/result
receipt; silence is not success. Do not discard errors, mask failures with a
pipeline or require a new log file. Quiet progress does not replace the scope,
direction and fresh remote revision checks below.

## Confirm first

Distinguish required/recovered revision `S`, observed local `main` head `L`, and
fresh fetched selected-remote `main` head `R`. Recover exact S from inspectable
receipts/history; do not replace a known S with newer L. Unknown prior S blocks
confirmation/replay. For genuinely fresh publication, observe L as candidate S.
Keep expected IDs, local result/closure evidence and scope alongside S; remote
revision assurance does not independently verify their field contents.

After project/destination/safe-read checks, run `dolt fetch --silent <confirmed-remote>`
and inspect `dolt branch -av` for full L/R hashes and exact selected refs. Use
validated complete hashes with `dolt merge-base <S> <R>`: successful equality
to S establishes reachability (S=R also suffices after the fresh fetch). A failed
fetch, missing ref/object or failed/ambiguous ancestry read stays unverified;
do not treat it as proof of absence. If this mapping is unsupported, return the
precise capability gap, without rebuilding a parent/object parser.
Only a successful, unambiguous merge-base result different from S establishes
that S is not an ancestor of R; an empty/error result does not.

**Check S reachability before incoming-only/divergence, clean-working-set or
other new-write gates.** Reachable S returns verified no-op, naming S and fresh
R separately. Newer local/remote work does not block confirmation and is outside
this receipt's acceptance. No push, result write, close, merge, branch update,
private ref, write window or repeated human confirmation is needed. Confirmation
does not require a clean later local working set.

## Publish only proven unsent work

1. If S is proven absent from R, recheck authority, selected remote/address/main
   and relevant scope. Require a clean committed candidate working set; report
   pending writes without silently committing them. Verify S is reachable from L;
   a recovered S not contained in selected local main cannot be sent by this route.
2. Check local/remote direction with `dolt merge-base <L> <R>` and full observed
   hashes. R ancestor of L permits the ordinary outgoing route. L ancestor of R
   is incoming-only; neither ancestor is divergence. Return `conflict` and the
   separately authorized reconciliation needed, without hidden merge/pull/force.
   Unknown direction blocks publication. Repeat confirmation-first after each
   refetch before applying these new-push gates.
3. Immediately before push, freshly observe selected branch/candidate and scope.
   Reassess changed observations through these gates, retaining S. Invoke only:

   ```sh
   dolt push --silent <confirmed-remote> main:main
   ```

   This sends the shared moving branch, not an immutable exact-sent snapshot.
   Other authorized writers may add history between observation and push. Do not
   promise an atomic snapshot/CAS or stop writers with a global lock/coordinator.
4. Independently of the push response, freshly fetch the selected remote again,
   observe R and check S reachability as above. Cached tracking refs, command
   success, local closure or Git SHA alone do not establish remote publication.
   A fresh remote fetch/ref observation suffices; a separate clone is not required.

## Refusal, ambiguity and receipt

For rejected/nonzero/timed-out/ambiguous push, **first** fetch and check exact S.
If reachable, record confirmed publication without retry. If proven absent,
only the missing push may proceed after fresh direction/scope checks; genuine
divergence remains conflict. If S, remote access or ancestry is unknown, stop
with uncertainty and exact missing evidence. A successful push followed by failed
verification preserves the attempted/known effect but is not verified success.
Do not repeat a confirmed result write, ID creation or closure to repair publication.

Return `ok|blocked|conflict|error` with selected project/database, remote/address/
branch, scope and authority provenance, required S, observed L and fresh R,
reachability evidence/address, actual push attempted vs confirmed/no-op facts,
expected IDs and separate local result/closure facts, limits and exact remainder.
Technical read failure is `error`, missing access/capability/identity is `blocked`,
contradictory scope/history is `conflict`. Return `ok` only with fresh remote
revision assurance; a preflight `ok` covers only its explicitly bounded checks.

Return the receipt to the caller. A persisted receipt file is not required and
is not created by default; recovery reads native local history and the selected
remote, not a saved receipt.

The accepted guarantee is reachability of S from fresh selected remote R, not
independent authorization proof for every historic action or exact field-by-field
snapshot equivalence. S is a required observed revision, not proof of exact sent
bytes; later remote R or local additions are distinguished, not accepted by this
receipt. If stronger assurance is requested, return that separate policy decision
before dependent effects rather than quietly restoring the removed audit route.
This operation never writes/closes issues or publishes Git.
