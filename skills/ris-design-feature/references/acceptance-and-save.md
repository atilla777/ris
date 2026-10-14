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

For bounded noninteractive save require the verified candidate address/revision,
destination path/section, separately accepted requirements and their decision,
the actual design acceptance decision/acceptor provenance and permitted writes.
The candidate may be a published Git version or an explicitly agreed local
address/version. Read it and compare the approved selected content; optional
local fingerprints detect changes but are not tracker refs or a mandatory
hashing scheme. Missing decisions return to the caller; the executor must not
ask the user, invent acceptance or change content while saving.

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

1. Check exact file/evidence paths, rights, format and current state under the
   project writer protocol. Apply an installed appropriate OKF operation only
   for an actual selected OKF bundle, not ordinary Markdown. Preserve unrelated
   content, requirements and decisions. An unexpected file change or missing
   required file protection means conflict before the dependent write.
2. In combined mode preflight exact task/epic/identity, expected old block,
   allowed fields and `tasks.features.update` guarantees. Existing-record writes
   require adapter-provided protection over the affected record and relevant
   composition/blockers/evidence through read/write/verify. Prefer applicable
   native CAS/transactions, then existing automatic coordination; a manual
   window is fallback only. Name provider, covered predicates and limits.
   A row-only/status guard does not cover arbitrary structure/evidence.
   Obtain acceptance outside any short coordination period. Missing
   protection blocks record writes; authorized independent file saving may
   proceed, but combined completion remains blocked/partial.
3. Reread expected files immediately before saving. Save only accepted content
   and actual decision evidence, no unaccepted intermediate draft. Read back,
   compare selected content with the accepted candidate, check substantive
   coverage, format/links and preserved requirements. Document-only is now a
   complete checked local result without tracker ID, epic or adapter; return
   checked addresses/revisions/decision and pending immutable refs. Do not infer
   workspace.tasks/<ID> before confirmation or require a draft directory.
4. Before combined update require published design and decision refs and
   applicable accepted published requirements. Local-only direct calls return
   saved partial effects with exact publication/re-entry prerequisites; the
   authorized caller owns Git publication. With published inputs and rights a
   direct call completes the design+record result. Reread record and relevant
   children/blockers inside the established window; unexpected change conflicts.
   Invoke the adapter with expected prior state and exact new design reference;
   preserve slug/spec, complete requirements reference and unrelated prose/fields.
   Changed result refs invalidate verification to null, without tracker history.
   Do not record verification or complete here. Specifically authorized blocker
   changes require supported adapter scope, checked endpoints/direction/cycles
   and read-back; otherwise return proposals/limitations.
5. Check full adapter read-back: actual ID/epic/slug/spec, exact refs and separate
   decisions, verification invalidation, preserved prose and permitted edges.
   Match actual saved/published content and unchanged applicable requirements.
   An exact repeated invocation returns unchanged after checks, without a new
   acceptance or redundant update. Historical unsupported payloads remain intact
   and block dependent operations; no migration/alternate API is introduced.

On ambiguous, nonzero or partial file/tracker effects, inspect actual state
before any retry and return confirmed paths/IDs/revisions, decisions, effects,
limitations and exact recovery. A saved new design with old record is partial
in combined mode. Recover by checking/publishing accepted content and decision,
resolving immutable refs, then reconciling the protected adapter update; do not
rollback, blind-retry or repeat unchanged acceptance. Git and tracker remote
publication are separate facts owned by the authorized caller; local read-back
or one successful channel alone cannot establish full remote success.
