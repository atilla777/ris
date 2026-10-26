# Independent design acceptance and persistence

Read before presenting a candidate, selecting accepted design content, accepting
or saving a draft or accepted result. The
wrapper owns design/applicability decisions; the adapter owns tracker encoding
and protected writes. No second feature registry or per-step skill is needed.

Apply common's `published-inputs.md` **Sufficient requirements/design basis**
before selecting or saving content. Throughout this resource, accepted candidate,
separate acceptance and decision matching mean independently sufficient direct,
inherited or mixed basis for requirements and design. A wholly inherited design
needs no new human approval/acceptor; preserve original accepted sources and explain
derivation in its substantive scope. In mixed content obtain an actual decision
only for new material in the context of the complete exact candidate. All decision
recording instructions below apply to actual direct/new decisions, not synthetic
approval for inherited content. Drafts with unresolved material stay drafts.

## Candidate and decision inputs

Use project-relative `path`, full published Git `revision` and `section: null`
for a whole file or an unambiguous semantic section. Requirements/design may
be separate sections or files, but cannot overlap ambiguously. Prefer a sufficient
short design in its own distinct spec.md section; use separate
design.md when adding design to whole-file accepted requirements; retain safe
existing sections instead of moving them mechanically. No mandatory scoped
hash, exact heading syntax, byte range or EOF boundary is required.

For bounded noninteractive save, the caller supplies either the full exact design
text with a distinguishable version and scope, or a recipient-accessible file at
an exact address/version (published Git version or explicitly agreed local
address/version). Both forms require destination path/section, separately accepted
requirements and their sufficient basis, the independently sufficient design basis
(source locators/derivation and any actual decision/provenance) and permitted writes.
Read the complete candidate, sources and applicable decisions
yourself; validate version/scope and that the design basis covers this
content, without assuming foreign-chat access. Return incomplete, inaccessible,
ambiguous or changed candidates and missing decisions to the caller before
dependent writes; do not ask the user, invent acceptance or reformulate accepted
meaning. Optional local fingerprints detect changes but are not tracker refs or
a mandatory hashing scheme. No intermediate file, registry or intermediate
publication is required; optional candidate storage needs its own authorized destination and
portable authors remain read-only.

### Optional pre-approval draft

A short full candidate may be shown inline. For a long design, an authorized
project writer may save the full candidate as an optional Markdown draft before
acceptance, only after the exact destination and write scope are explicitly agreed
and authorized. Inspect current files/rights, preserve unrelated and accepted
content, then read back and check the full draft's version/scope and accessibility.
If permission or an agreed path is missing, do not write: return the full unsaved
candidate in the dialogue/caller channel and the precise gap for optional storage.
The portable designer remains read-only; in a flow the lead applies the authorized
project writer directly or delegates the bounded write with the full exact candidate.

Label this result proposed/draft, not accepted, saved-as-accepted or published.
Draft storage requires no design acceptance and cannot replace it. It is separate
from the accepted-content save protocol below; do not enter that protocol with
an unaccepted draft. No mandatory draft directory, registry, file or intermediate
publication is introduced. Before later acceptance, verify the actual full draft
still matches the presented candidate; a changed candidate needs its own basis assessment.

For an ordinary native bug, accepted requirements may be the full current report,
aligned fix criteria and sufficient accepted constraints/decisions, with exact
project/tracker/bug/report identity and version (or published Git report locator)
and the authority for expected behavior. Do not demand a synthetic requirements
file/reference object or feature record. Inspect full substantive inputs and actual
decisions independently of research readiness. Design still gets its own exact
content selector, actual separate acceptance and the save/review/Git/record/tracker
gates below. A material report/criteria change needs targeted applicability review;
preserve unchanged authority/refs. No execution snapshot is required before design.

Before asking for acceptance of new material not demonstrably inherited in
the leading dialogue, give a plain-language explanation of its essence, main flow,
reused/new technologies and why, tradeoffs, material risks and irreversible or
hard-to-reverse choices. Roughly one screen is a readability guideline, not a
measured limit or permission to hide material decisions. A short full inline
design can itself provide that explanation without a duplicate summary. Identify
the exact COMPLETE candidate version/scope to be approved, make its full text
accessible inline or at a checked exact address/version, and show material impact.
The summary does not replace the full candidate or accept unseen/changed content.
For bounded supplied content, verify its sufficient basis instead of requesting
approval again; actual decisions cover only their direct/new material scope.
For that new material record its real decision in a permitted Git document/section, without imposing
a mandatory decision file. It names content path, section (including null),
revision, `decision: accepted` and attributable acceptor. Requirements approval
does not approve design; each result has its own identifiable accepted scope even
in one file/commit. One attributable act/decision section may accept both complete
requirements and design candidates when it explicitly lists each selector/version;
the two refs may share its address. Check the design entry and accepted requirements
entry independently, without another human answer just for a bounded save.
This permission does not accept an unseen design or merge overlapping selectors.
Unchanged content retains its checked acceptance on retry.

Identify published content by path, full revision and semantic section, with its
sufficient basis. The decision-address protocol below applies to direct/new
decisions and original decisions for inherited sources. No tracker reference object is required.
The immutable decision address pins repository, full
decision commit, path and any unique decision section. Read actual content and
decision at those revisions, check semantic selection, match path/section and
resolved revision, and consume the Git owner's checked publication of both
commits. Branch URLs, local notes and file/commit presence do
not establish published acceptance. A decision may name content revision
`containing-commit` only for content in that same commit; resolve it from the
immutable decision address. Never invent a future commit/address or copy accepted
refs/readiness into a tracker registry.
Pin the commit recording that actual decision, not a later unchanged copy.
Copying `containing-commit` into another commit does not renew acceptance;
retain the original reference or name/link its original full revision.
For unpublished revisions, keep the current accepted design and its separate
actual decision accessible to the next stage. For a material replacement,
briefly identify the superseded version/decision, what changed and the new actual
acceptance. A full archive of intermediate accepted snapshots, draft log,
intermediate publication or commit per acceptance is not required; voluntary
local drafts/commits are allowed. Preserve already published versions, decisions
and their pinned references in Git history.

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
need their separate decision and a design applicability check by the design
owner. Compatible unchanged design retains its original acceptance; materially
changed design needs its own separate acceptance. Uncertain applicability blocks
the dependent action, not independently authorized work.

## Preflight, save, update, verify

For full mode preflight the existing Git publisher and applicable adapter
publication before dependent writes, with exact subject/destination, authority,
whole outgoing scope and actual guarantees. Missing prerequisites block full
success; independently authorized local saving preserves useful effects. Full
mode returns `blocked|conflict|error` from the stopping cause with exact remaining
channels; an expressly limited successful local save may be `ok` only for its boundary.

Before proposing limited publication, explain which parts of the requested whole
it excludes and what remains. A restriction on primary-copy synchronization does
not by itself exclude or authorize local record reconciliation or publication
through the selected adapter; check their existing permissions separately. An
agreed Git-only result stays Git-only, with the excluded remainder explicit.

An explicitly limited record-only call discovers published accepted content/decisions
and applicable independent review/publication evidence from saved associations
(or a supplied checked result within an unfinished flow), skips formulation, renewed
acceptance and file saving, then enters step 5. It performs no second push. No
particular receipt file or previous chat is required; missing actual evidence
remains a precise dependent gap, never invented.

1. Check exact file/evidence paths, rights, format and current state under the
   project writer protocol. Apply an installed appropriate OKF operation only
   for an actual selected OKF bundle, not ordinary Markdown. Preserve unrelated
   content, requirements and decisions. An unexpected file change or missing
   required file protection means conflict before the dependent write.
2. In combined mode preflight exact task/kind/identity and expected prior state:
    feature uses native task/optional epic/block reads and bounded update; explicit ordinary
    standalone uses supported tool-specific source updates without feature JSON.
    Native bug source links use explicitly advertised ordinary bug updates; a
    native notes append may record the pinned design/decision refs without replacing
    the current report. Ask the adapter to reconcile existing source links before
    append/retry; do not reproduce its native procedure. Any
    necessary investigation report/acceptance replacement applies its owner's
    bounded single-investigator persistence conditions; source-link append alone
    cannot establish a saved aligned report/criteria pair.
    Existing-record writes
    use the adapter's fresh expected-content/composition/blocker checks, targeted
    native operations and independent read-back. State native predicates and
    limits; a row/status guard is not arbitrary structure/evidence CAS. Do not
    require a manual window or atomic freeze of record, graph and external
    evidence. Unsupported explicitly required stronger guarantees block only
    dependent record writes; authorized independent file saving may proceed.
3. Reread expected files immediately before saving sufficiently grounded content.
   Save only that content, source derivation and any actual decision evidence, no unresolved intermediate draft
   in this accepted-save branch. The optional pre-approval draft branch above is
   separate and grants no acceptance or publication. Read back,
   compare selected content with the exact accepted candidate and separate design
   decision for either supplied form, check substantive
    coverage, format/links and preserved requirements. An explicitly limited
    local save is now complete without tracker ID, epic or adapter; return
   checked addresses/revisions/decision and pending immutable refs. Do not infer
   workspace.tasks/<ID> before confirmation or require a draft directory.
4. In full mode apply independent `ris-proj-op-review-task` to this project
    document subject with or without an ID. It composes portable assessment and
    saves one local YAML under its references/report-format.md. Pass publication-gate
    purpose; before ID pass an
    explicit authorized report path, not an invented task folder. Consume exact
    address/round with separate validity/applicability checks and no fallback past
    later adverse/unknown rounds, passing
    exact whole candidate base/overlay/add/delete/modes, accepted inputs/decisions,
    rules and checks. All authors/repair authors are distinct from the reviewer.
    For a native bug ID explicitly request **pre-execution design/document review**:
    pass full current report/criteria/accepted constraints with source identity and
    authority, plus exact design candidate and separate decision. Do not require or
    create a future execution-input snapshot, implementation or execution plan to
    satisfy this document gate. Bind the full candidate tree independently of that
    absent historical execution basis; compare current report/criteria/decisions
    with the supplied design basis for targeted applicability reassessment.
    Resolve high/medium through their content owner, affected checks and fresh
    independent review. Invoke `ris-proj-op-publish-task` with exact subject,
    decisions, checks/review/provenance, destination evidence and allowed effects.
    Select its **Documents** input branch for this design publication, including
    when the native bug ID is supplied for identity. It is not fix implementation
    publication; keep the same current report/criteria/design basis and document
    review scope without importing future execution prerequisites. Mixed fix changes
    are outside this design-only handoff and cannot use that exception.
    Consume its commit/tree/ref/remote receipt and independent remote evidence;
    match accepted selected content and preserved requirements. Check applicable
    accepted project policy and pass its actual source/version/acceptance and
    boundaries, or an explicit local request, to the publisher. Without either its
    default is remote-only; authorized source-copy/dependency maintenance is a
    separate safe-FF effect without branch switching: skipped/failed sync never
    invalidates confirmed remote Git or blocks record/tracker actions. A policy-required
    or explicitly requested update retains its unfinished combined-result part;
    never call the whole result complete or repeat push for it. Integration drift
    requires applicable independent reassessment. Reuse checked existing
    publication without empty commit/push. A limited record-only contribution
    consumes the existing applicable receipt; limited local save stops earlier.
5. Before combined update require published design and decision refs and
    applicable accepted published requirements. Git failure blocks dependent
    record writes and preserves saved effects. Reread record and relevant
    children/blockers immediately before updating; unexpected change conflicts.
   For features reconcile only authorized ordinary goal/scope/criteria as needed;
   documents and decisions remain discoverable through common's full-ID convention
   or checked legacy source links. Do not duplicate accepted refs, write JSON or
   reset verification. Preserve all historical payloads/links and unrelated fields.
   Ordinary standalone/bug source-link updates keep their own contracts and paths;
   preserve current report and original decisions. Assess affected evidence anew.
   Do not record verification or complete here. Specifically authorized blocker
   changes require supported adapter scope, checked endpoints/direction/cycles
   and read-back; otherwise return proposals/limitations.
6. Check full adapter read-back: actual ID/kind/parent, authorized ordinary content,
   preserved prose/historical payload and permitted edges; check document/decision discovery.
   Match actual saved/published content and unchanged applicable requirements.
   An exact repeated invocation returns unchanged after checks, without a new
   acceptance or redundant update. Historical payloads remain intact and their
   schema alone never blocks the document route; no migration/alternate API.
7. In full combined mode invoke the selected adapter's separate publication
    operation for exact verified record/refs, destination and authorized entire
    outgoing scope. Inspect required revision/fresh remote reachability receipt
    alongside the locally verified result; do not require remote field equivalence.
    No-change checks existing required availability
    or debt without empty push. Limited record-only stops at checked local update
    and names this remainder. Unknown publication is reconciled by its owner
    before retry, not repeated from a saved marker.

On ambiguous, nonzero or partial file/tracker effects, inspect actual state
before any retry and return confirmed paths/IDs/revisions, decisions, effects,
limitations, actual stopping cause and exact recovery. A saved new design with
old record requires the cause's `blocked|conflict|error` in combined mode.
Recover by checking/publishing accepted content and decision,
resolving immutable refs, then reconciling the protected adapter update; do not
rollback, blind-retry or repeat unchanged acceptance. Git and tracker remote
publication are separate effects executed by their existing owners; local read-back
or one successful channel alone cannot establish full remote success.
