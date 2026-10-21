# Complete one exact record

Read before either completion branch, together with `concurrency.md` and main
typed reads. Require caller's exact ID/type, chosen branch and authority.
Administrative status-only close supports explicitly identified epic, ordinary
task-container or feature task with actual container-kind evidence and expected
status; it is a Beads-specific bounded status operation, not substantive verification. Never
infer ordinary kind from absent/failed feature parsing. No kind assessment
resource or feature-record write validation is needed for status alone.
Preserve description, feature block/refs/verification and unrelated fields;
administrative closed is not independent acceptance and never promotes null,
failed, historical or malformed verification to success.

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

Feature verified completion uses the caller's current whole-feature criterion,
accepted-document and integrated-revision assessment, with no mandatory saved
verification/readiness record or duplicate refs. Leave historical payloads untouched.
Ordinary verified completion applies its specifics in `standalone.md`, bug fix-completion in
`bug-execution.md`. Investigation disposition has its separate unchanged owner
`investigation.md`. None of these branches implicitly publishes Dolt.
