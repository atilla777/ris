# Complete one exact record

Read before a completion branch, together with `concurrency.md` and main
typed reads. Require caller's exact ID/type, chosen branch and authority.
Administrative status-only close supports explicitly identified epic, ordinary
task-container or feature task with actual container-kind evidence and expected
status; it is a Beads-specific bounded status operation, not substantive verification. Never
infer ordinary kind from absent/failed feature parsing. No kind assessment
resource or feature-record write validation is needed for status alone.
Preserve description, feature block/refs/verification and unrelated fields;
administrative closed is not independent acceptance and never promotes null,
failed, historical or malformed verification to success.

- **Complete — ordinary child-based container close:** require exact project/ID/type,
  confirmed feature/epic/ordinary container kind and explicit closing authority.
  Freshly read exact status, complete all-status direct children and the parent's
  directed blockers. Already closed returns unchanged. Otherwise require at least
  one direct child, all children exactly `closed`, and no active parent blockers.
  Empty/unknown/incomplete membership does not pass this gate; zero-child feature
  own-result completion uses the verified-work branch. No descendant traversal,
  child evidence/blocker audit, decomposition reconstruction, specs/design/Git
  evidence, new acceptance, result persistence or verification write is required.
  Trust closed children without calling their status a fresh whole-result acceptance.
  Use `bd --sandbox -C <selected-workspace> close <exact-ID> --reason <reason> --json`
  without force/continue/claim-next or a multi-ID call. Retain native direct-child/
  blocker refusal, preserve content/evidence and independently reread status/reason,
  direct children and parent blockers. Reconcile ambiguous effects before retry;
  never repeat confirmed closure for pending publication. Native guards cover only
  their predicates, not a distributed graph CAS. Do not close children/ancestors.
- **Complete — administrative container status:** require exact project/ID/type,
  confirmed container kind and explicit administrative authority/reason. Freshly
  read status, complete direct children and directed blockers. Already closed is
  unchanged, without another close or acceptance reconstruction. Use
  `bd --sandbox -C <selected-workspace> close <exact-ID> --reason <reason> --json`
  with no force, continue, claim-next, implicit last-touched fallback or multi-ID
  call. Preserve native refusal for open direct children/live direct blockers;
  never remove links, close children/parents or reopen as a workaround. Independently
  read exact status/reason, preserved description/feature block and relevant direct
  children/blockers. No recursive delivery reconstruction, Git evidence, new
  acceptance, result persistence or verification write is required. This status
  mutation does not establish fulfillment, descendant completeness or acceptance.
  On ambiguous/nonzero output reconcile exact effects before retrying only a
  proved-missing authorized close; pending publication never repeats confirmed close.
  Apply native predicate limits in `concurrency.md`, with no manual
  writer window, global lock or invented content/graph CAS.
- **Complete — verified work:** require a specific ID, explicit permission and verified caller
  completion criteria (including mandatory members, cancelled vs completed,
  and any required publication evidence). Read status, blockers and **all**
  direct/descendant mandatory children; refuse open children or active blockers.
  Use `bd --sandbox close <id> --reason <reason> --json` with no `--force`, `--continue`,
  `--claim-next` or automatic epic closing. Re-read `status: closed`, reason,
  children and edges. If already closed, report that state; do not close again.
  `bd`'s refusal is a backstop, not proof that all required children exist.
  Apply `concurrency.md`: native transactional child/blocker guards
  suffice for their own predicates. Freshly verify exact expected mandatory
  composition, descendants and applicable evidence before close and read them
  back afterward; no graph/external-evidence freeze is required. Native closure
  is not full feature verification or a distributed transaction. An unsupported
  explicitly required stronger guarantee returns its exact limitation.

  Consume only **applicable** channel/review obligations, never invent Git or
  approval evidence. A verified eligible Fast local-only subject uses passed own
  criteria and actual authorized target/useful-effect evidence without Git SHA,
  commit or push; review is conditional under that flow's actual request/policy/
  risk grounds. This is ordinary verified completion, not administrative close.
  Mixed Fast work needs both own required Git and local parts verified; partial
  own-channel success cannot close it. No-change verifies the required existing
  result without dummy commit/push. Known adverse findings and required unavailable
  review still block dependent completion. Preserve mandatory full/feature/bug
  review/publication obligations outside this narrow Fast scope. Separately owed
  policy-required source maintenance retains its existing close/Dolt exception
  after confirmed remote Git, while remaining explicit combined-result debt.
  Result persistence, exact native close/read-back and authorized Dolt publication
  remain separate effects; Dolt does not publish local target files.

Feature **verified-work** completion uses the caller's current whole-feature criterion,
accepted-document and integrated-revision assessment, with no mandatory saved
verification/readiness record or duplicate refs. Leave historical payloads untouched.
Ordinary verified completion applies its specifics in `standalone.md`, bug fix-completion in
`bug-execution.md`. Investigation disposition has its separate unchanged owner
`investigation.md`. None of these branches implicitly publishes Dolt.
