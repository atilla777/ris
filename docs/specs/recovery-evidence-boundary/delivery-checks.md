# Recovery evidence boundary — static audit (`ris-7e7`)

## Inspected result and limits

Inspected contract revision: `c6409a1d13ac320204eb077ddfe74e08804e19c5`.
Paths and line ranges below refer to that revision, not future file positions.
This ordinary Markdown delivery record is a bounded audit conclusion, **not a
new normative policy, evidence registry or general readiness certificate**.
It is prepared on the task branch; independent review and publication of this
record are separate gates, not outcomes established by this text.

**Conclusion:** the inspected producers and consumers already agree on conditional
recovery. A new session can reuse accessible, attributable evidence applicable to
its actual inputs and complete candidate. It cannot recover proof that survives
nowhere accessible. That case blocks dependent reuse/approval, not read-only
reconciliation or preservation of confirmed effects. No concrete contract gap
requiring a skill edit was found in the boundaries below; no skill, storage duty,
default fast report or transition ledger is added.

Four facts remain distinct: **effect exists**, **evidence is accessible**,
**evidence applies now**, and **proof is missing/unknown**. A published commit or
closed record can establish an effect without establishing historical TDD,
reviewer independence or current acceptance. A file/locator can be accessible
without proving its content or continued applicability.

## Producer → consumer trace

All paths in this table are under `skills/`. Read the referenced content, not
merely its filename, status or hash.

| Boundary | Producer, actual channel and sufficient address | Consumer and limit |
| --- | --- | --- |
| Shared artifact/response transfer | [Common artifacts](../../../skills/ris-proj-lib-common/references/artifacts.md), lines 60–81, 88–109: full distinguishable response content or exact accessible result/evidence address, versions, actual separate decisions and channel effects. Response-only content must be explicitly forwarded. | Same resource, lines 93–102: recipient reads complete content and rechecks version/provenance, paths and live gates. A lost response or inaccessible ignored note is a discovery gap, not implied durable storage. |
| Copy preparation → plan/change | [Preparation](../../../skills/ris-proj-op-prepare-task-worktree/SKILL.md), lines 97–124: checked project/task/actor/copy/branch/base and primary-selection facts returned directly or at an authorized exact address; no default receipt file. | [Primary resolution](../../../skills/ris-proj-op-resolve-context/references/shared-primary.md), lines 5–33, and [full recovery](../../../skills/ris-proj-flow-execute-task/references/recovery.md), lines 12–28: explicit primary or already available verified witness with current-copy association. Git common-dir/registration corroborates, never selects. Missing association blocks dependent use, not authorization to recreate/reset. |
| Plan/change/checks → review | [Plan](../../../skills/ris-proj-op-plan-task/SKILL.md), lines 71–85; [implementation](../../../skills/ris-proj-op-implement-task-tdd/SKILL.md), lines 67–87; [text route](../../../skills/ris-proj-flow-execute-task/references/text-work.md), lines 48–59: authorized primary-local plan/implementation notes and exact check/snapshot evidence. These ignored files are not remotely synchronized. | [Review](../../../skills/ris-proj-op-review-task/SKILL.md), lines 18–39, 74–104, reads actual bytes, baseline, check applicability and provenance. [Full recovery](../../../skills/ris-proj-flow-execute-task/references/recovery.md), lines 63–89, reconstructs only supported facts; missing historical proof stays unverified. RIS full flow still requires its local plan/report; fast's file exception does not waive TDD. |
| Independent review → Git publication | [Full flow](../../../skills/ris-proj-flow-execute-task/SKILL.md), lines 38–43, 240–260, actually launches a fresh reviewer independent of every author/repairer. [Review owner](../../../skills/ris-proj-op-review-task/SKILL.md), lines 74–104, returns provenance, versioned findings and required saved report (response-only where permitted). | [Publication](../../../skills/ris-proj-op-publish-task/SKILL.md), lines 78–85, 123–146, requires the complete approved subject and independent provenance. Base plus overlays/additions/deletions/modes, unchanged base files and predeclared exclusions are bound; HEAD or dirty hash alone is insufficient. Changed integration needs independent reassessment before push. |
| Fast implementation/review → publication/result | [Fast flow](../../../skills/ris-proj-flow-execute-simple-task/SKILL.md), lines 42–51, 94–140: main agent applies stage owners; sufficient evidence stays in session, review actually runs separately. No mandatory report file. | [Fast recovery](../../../skills/ris-proj-flow-execute-simple-task/references/recovery.md), lines 16–27, assumes no new-session history; missing/inapplicable review needs a fresh independent invocation. [Fast tracker](../../../skills/ris-proj-flow-execute-simple-task/references/tracker.md), lines 51–73, requires remotely sufficient outcome/check/review/limits and Git SHA, not ignored reports as remote prerequisites. No retroactive session-proof inference from a summary. |
| Ordinary task inputs/result → another session | [Beads ordinary work](../../../skills/ris-proj-adapter-beads-tasks/references/standalone.md), lines 95–108, 147–156: sufficient attributable request/criteria/constraints in readable record content; authorized result append or independent metadata keys with checks/review provenance, revision, evidence addresses and limits. Address: selected project/tracker + exact ID and actual field/content or pinned external locator. | Exact full record read under the [adapter](../../../skills/ris-proj-adapter-beads-tasks/SKILL.md), lines 86–145; [full recovery](../../../skills/ris-proj-flow-execute-task/references/recovery.md), lines 21–38, 75–92. Remotely readable content suffices only for the facts it actually contains and evidence it makes accessible; not an automatic archive of every earlier invocation or RED/GREEN event. Local persistence is not remote publication. |
| Native bug basis → execution/review | [Fix flow](../../../skills/ris-proj-flow-fix-bug/SKILL.md), lines 98–127, and [Beads bug execution](../../../skills/ris-proj-adapter-beads-tasks/references/bug-execution.md), lines 51–101: full historical report/criteria/decisions in notes, addressed by project/tracker + exact bug ID + unique begin/end marker. Marker and complete content/occurrences are checked; a hash/link alone is insufficient. | [Full recovery](../../../skills/ris-proj-flow-execute-task/references/recovery.md), lines 47–53, and [fix review](../../../skills/ris-proj-op-review-task/SKILL.md), lines 58–68, retrieve complete text and compare current basis. Drift requires targeted assessment, not snapshot rewrite/reappend. Pre-execution document review (same skill, lines 50–57) needs its actual document basis, not a future execution snapshot; it never approves the future fix. |
| Git/result/close → pending tracker publication | [Git owner](../../../skills/ris-proj-op-publish-task/SKILL.md), lines 159–180; [ordinary result](../../../skills/ris-proj-adapter-beads-tasks/references/standalone.md), lines 147–178; [bug result](../../../skills/ris-proj-adapter-beads-tasks/references/bug-execution.md), lines 103–130: separate exact Git commit/tree/remote evidence, record result and verified exact closure. | [Full recovery](../../../skills/ris-proj-flow-execute-task/references/recovery.md), lines 90–110, and [Dolt publication](../../../skills/ris-proj-adapter-beads-tasks/references/dolt-publication.md), lines 51–75, 104–129: recover exact required revision S from inspectable receipts/history and freshly test reachability from selected remote R before new-write gates. Unknown S or failed reads remain unverified. Already closed stays closed; no replay/reclose. Reachability is not field-by-field snapshot equivalence. |

## Static scenario/criterion matrix

These are **read-through cases, not executed agent/scenario tests**. Addresses
refer to the producer/consumer trace above; each conclusion is conditional on
actual accessible evidence and fresh applicable gates.

| Case / AC | Sufficient input or precise gap | Supported continuation |
| --- | --- | --- |
| Fresh session with accessible evidence — AC-1/4 | Exact attributable request/decisions, checked copy association, full candidate identity and accessible checks/review with actual invocation provenance. | Re-read content and live Git/Beads facts; reuse only applicable proof. A locator alone is not a pass. |
| Chat lost, local evidence accessible — AC-1/4 | Exact primary-local plan/change/review results with source versions and invocation facts, or explicitly forwarded complete content; remotely readable task/bug basis where required. | Revalidate root/association and evidence. Partial notes lacking reviewer/TDD provenance leave those gates unverified. No old chat is assumed. |
| Ignored notes lost, remote evidence accessible — AC-1/2 | Self-contained task request/result, pinned Git artifacts and actual review/check provenance accessible through existing channels; bug full marker-addressed snapshot where applicable. | Reconstruct only what those sources establish. Missing RIS-required local plan/report needs its owner's legitimate remaining assessment/save where required; never rerun implementation merely to recreate notes or make local paths remote requirements. |
| Both chat and ignored notes lost — AC-1/3 | Accessible remote proof can still cover particular facts; Git/Beads status alone cannot supply missing decisions, chronology or independence. | Preserve known commits/closure. Name each missing prerequisite and stop dependent reuse/approval; no universal automatic-recovery promise or new registry. |
| Closed, tracker publication unconfirmed — AC-1/2 | Exact ID/closure/result, Git evidence separately, exact required S recoverable from receipts/history and fresh selected-remote R. | Confirmation-first reachability read; if sent, no push/write/close. If proven unsent, only authorized missing publication under fresh gates. Unknown S/read failure blocks confirmation/replay, not preservation of closure. |
| Unknown independent-review origin — AC-1/2 | Actual independent invocation/context, all authors/repairers, exact reviewed whole subject, inputs and verdict are needed. A configured role/name/report title is insufficient. | Missing provenance blocks reuse; obtain fresh independent review for the actual current subject. It does not establish a past approval or undo a sent commit. |
| Unknown TDD chronology — AC-1/2 | Per behavioral slice: criterion/test, pre-change version, command and observed expected RED before production edit, resulting version/GREEN and final checks. | [TDD method](../../../skills/ris-port-op-implement-change/references/tdd.md), lines 9–42, forbids reconstruction after edits, artificial breakage or test-last relabeling. Missing historical RED remains unverified and blocks dependent approval pending legitimate disposition. Pure refactors/text retain their actual non-artificial-RED checks. |
| Copy association unavailable or stale — AC-1/2 | Valid explicit primary selection, or available saved indication with provenance/project/repository/current-copy association. | Re-resolve and corroborate; unresolved association blocks dependent shared-path actions. Never select primary from first/main worktree, branch name, common-dir or `.sdlc` alone. |
| Candidate/input changed — AC-2/4 | Old and actual complete subject/input identities and targeted applicability assessment. | Recheck affected checks and independent whole-snapshot review; retain compatible evidence with reasons and confirmed sent/closed effects. No automatic full restart or blanket reuse. |
| No ledger/default fast report — AC-3 | Common artifacts lines 83–102; full-flow evidence lines 9–18, 97–102; fast flow lines 42–51. | Existing authorized channels remain sufficient or produce the exact discovery gap. Making additional evidence durable would require a separate material decision, not an audit-side implementation detail. |

## Verification scope

Static inspection covered the actual stage owners, direct-invocation boundaries,
conditional resources and full/fast/native-bug transfers listed above. The
existing portable TDD/review methods remain separate from project wrappers;
flows retain transitions, context owns root resolution, and the adapter owns
bounded tracker persistence/publication. No new dependency or instruction load
is introduced. No behavioral reliability, cost, speed or repeatability claim is
made. No live/scenario session or executable logic is added or tested here.

The task's local implementation evidence records actual static/link/parity checks
and the exact candidate identity for the independent reviewer. That ignored note
is **not** a required remote input to this conclusion. Independent review,
Git publication, exact task completion and Dolt publication require their own
applicable evidence and are not certified by this record.
