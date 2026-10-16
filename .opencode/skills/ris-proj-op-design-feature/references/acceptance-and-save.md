# Independent design acceptance and persistence

Read before selecting accepted design content, accepting or saving it. The
wrapper owns design/applicability decisions; the adapter owns tracker encoding
and protected writes. No second feature registry or per-step skill is needed.

## Candidate and decision inputs

Use project-relative `path`, full published Git `revision` and `section: null`
for a whole file or an unambiguous semantic section. Requirements/design may
be separate sections or files, but cannot overlap ambiguously. Prefer separate
design.md when adding design to whole-file accepted requirements; retain safe
existing sections instead of moving them mechanically. No mandatory scoped
hash, exact heading syntax, byte range or EOF boundary is required.

For bounded noninteractive save, the caller supplies either the full exact design
text with a distinguishable version and scope, or a recipient-accessible file at
an exact address/version (published Git version or explicitly agreed local
address/version). Both forms require destination path/section, separately accepted
requirements and their decision, the actual separate design acceptance decision/
acceptor provenance and permitted writes. Read the complete candidate and decisions
yourself; validate version/scope and that the actual design decision approves this
content, without assuming foreign-chat access. Return incomplete, inaccessible,
ambiguous or changed candidates and missing decisions to the caller before
dependent writes; do not ask the user, invent acceptance or reformulate accepted
meaning. Optional local fingerprints detect changes but are not tracker refs or
a mandatory hashing scheme. No intermediate file, registry or intermediate
publication is required; optional candidate storage needs its own authorized destination and
portable authors remain read-only.

Show the specific design and material impact to the authorized acceptor in the
leading dialogue, or verify the supplied separate decision for this candidate.
Record its real decision in a permitted Git document/section, without imposing
a mandatory decision file. It names content path, section (including null),
revision, `decision: accepted` and attributable acceptor. Requirements approval
does not approve design; each result has its own identifiable decision even in
one file/commit. Unchanged content retains its checked acceptance on retry.

Published references use `{path, revision, section, acceptance: {address,
decision: "accepted"}}`. The immutable decision address pins repository, full
decision commit, path and any unique decision section. Read actual content and
decision at those revisions, check semantic selection, match path/section and
resolved revision, and establish publication of both commits from fetched
selected-remote evidence. Branch URLs, local notes and file/commit presence do
not establish published acceptance. A decision may name content revision
`containing-commit` only for content in that same commit; resolve it from the
immutable decision address. Tracker revision always stores the actual full
published commit. Never invent a future commit/address.
Pin the commit recording that actual decision, not a later unchanged copy.
Copying `containing-commit` into another commit does not renew acceptance;
retain the original reference or name/link its original full revision.
Preserve every separately accepted content/decision snapshot in Git history
when multiple versions were accepted before publication.

Local accepted content and decision evidence may be saved before publication,
with immutable refs explicitly pending and a checked local candidate identity.
Document-only can use verified local accepted requirements/decision inputs with
these limits stated; combined tracker updates cannot use unpublished refs.

## Preserve requirements and bound impact

For design-only work preserve the entire old requirements reference, including
acceptance address/revision. Compare actual applicable requirements at that
revision with the candidate/saved design tree using path diff and semantic
section review in both versions; changes elsewhere in a shared file do not
automatically invalidate requirements. Same labels or path alone prove nothing.
Record applicability evidence; material/uncertain behavioral changes return to
the requirements owner, blocking dependent design acceptance/writes. Do not
reaccept requirements, rewrite their ref to the latest commit or assert that
design acceptance approves changed behavior. Authorized requirements changes
need their separate decision and checked design applicability from their owner.

## Preflight, save, update, verify

For full mode preflight the existing Git publisher and applicable adapter
publication before dependent writes, with exact subject/destination, authority,
whole outgoing scope and actual guarantees. Missing prerequisites block full
success; independently authorized local saving may remain partial.

An explicitly limited record-only call reads published accepted content/decisions
and the applicable independent review/Git receipt, skips formulation, renewed
acceptance and file saving, then enters step 5. It performs no second push.

1. Check exact file/evidence paths, rights, format and current state under the
   project writer protocol. Apply an installed appropriate OKF operation only
   for an actual selected OKF bundle, not ordinary Markdown. Preserve unrelated
   content, requirements and decisions. An unexpected file change or missing
   required file protection means conflict before the dependent write.
2. In combined mode preflight exact task/kind/identity and expected prior state:
    feature uses task/epic/block and `tasks.features.update`; explicit ordinary
    standalone uses supported tool-specific source updates without feature JSON.
    Existing-record writes
    use the adapter's fresh expected-content/composition/blocker checks, targeted
    native operations and independent read-back. State native predicates and
    limits; a row/status guard is not arbitrary structure/evidence CAS. Do not
    require a manual window or atomic freeze of record, graph and external
    evidence. Unsupported explicitly required stronger guarantees block only
    dependent record writes; authorized independent file saving may proceed.
3. Reread expected files immediately before saving. Save only accepted content
   and actual decision evidence, no unaccepted intermediate draft. Read back,
   compare selected content with the exact accepted candidate and separate design
   decision for either supplied form, check substantive
    coverage, format/links and preserved requirements. An explicitly limited
    local save is now complete without tracker ID, epic or adapter; return
   checked addresses/revisions/decision and pending immutable refs. Do not infer
   workspace.tasks/<ID> before confirmation or require a draft directory.
4. In full mode apply independent `ris-port-op-review-change` to the pre-ID
    document subject, or `ris-proj-op-review-task` for an applicable ID, passing
    exact whole candidate base/overlay/add/delete/modes, accepted inputs/decisions,
    rules and checks. All authors/repair authors are distinct from the reviewer.
    Resolve high/medium through their content owner, affected checks and fresh
    independent review. Invoke `ris-proj-op-publish-task` with exact subject,
    decisions, checks/review/provenance, destination evidence and allowed effects.
    Consume its commit/tree/ref/remote receipt and independent remote evidence;
    match accepted selected content and preserved requirements. Integration drift
    requires applicable independent reassessment. Reuse checked existing
    publication without empty commit/push. A limited record-only contribution
    consumes the existing applicable receipt; limited local save stops earlier.
5. Before combined update require published design and decision refs and
    applicable accepted published requirements. Git failure blocks dependent
    record writes and preserves saved effects. Reread record and relevant
    children/blockers immediately before updating; unexpected change conflicts.
   Invoke the adapter with expected prior state and exact new design reference;
   preserve feature slug/spec where applicable, complete requirements reference
   and unrelated prose/fields.
   Changed result refs invalidate verification to null, without tracker history.
   Do not record verification or complete here. Specifically authorized blocker
   changes require supported adapter scope, checked endpoints/direction/cycles
   and read-back; otherwise return proposals/limitations.
6. Check full adapter read-back: actual ID/kind/parent, feature slug/spec where applicable, exact refs and separate
   decisions, verification invalidation, preserved prose and permitted edges.
   Match actual saved/published content and unchanged applicable requirements.
   An exact repeated invocation returns unchanged after checks, without a new
   acceptance or redundant update. Historical unsupported payloads remain intact
    and block dependent operations; no migration/alternate API is introduced.
7. In full combined mode invoke the selected adapter's separate publication
    operation for exact verified record/refs, destination and authorized entire
    outgoing scope. Inspect returned snapshot/remote/independent read-back receipt
    against the promised result. No-change checks existing required availability
    or debt without empty push. Limited record-only stops at checked local update
    and names this remainder. Unknown publication is reconciled by its owner
    before retry, not repeated from a saved marker.

On ambiguous, nonzero or partial file/tracker effects, inspect actual state
before any retry and return confirmed paths/IDs/revisions, decisions, effects,
limitations and exact recovery. A saved new design with old record is partial
in combined mode. Recover by checking/publishing accepted content and decision,
resolving immutable refs, then reconciling the protected adapter update; do not
rollback, blind-retry or repeat unchanged acceptance. Git and tracker remote
publication are separate effects executed by their existing owners; local read-back
or one successful channel alone cannot establish full remote success.
