---
name: ris-verify-feature-base
description: >-
  Verify a feature's complete integrated behavior on one identified revision,
  with criterion coverage, architecture, documentation and evidence applicability.
  Use for read-only feature acceptance, including a failed verification retry;
  not diff review, implementation, design approval or tracker closure.
---

# Verify an integrated feature

Own the portable, read-only acceptance assessment. Work from explicit inputs
and the actual project's rules without requiring RIS configuration, directories,
another skill, tracker or a particular stack. Return content for the caller;
do not save reports, edit code/docs/requirements, create repair tasks, integrate,
publish or close anything. The caller owns persistence and completion.

## Establish the subject

Require the bounded feature identity, complete current accepted criteria and
exclusions, independently accepted requirements/design versions and their decision
evidence, applicable contracts/rules, the concrete integrated revision and evidence
of its integration, related source baselines/current sources, and available checks.
Use explicit paths/addresses; do not infer acceptance from file presence or a
task's status. A minimal accepted design may simply preserve existing contracts.
No new design file or criterion numbering scheme is required by this method.

Confirm the full immutable revision (e.g. Git commit SHA), actual code tree,
branch/integration context and requirements/design bytes at that revision. Check
the accepted scopes and versions against those bytes and decisions. If using a
checkout, confirm it represents that tree and contains no material dirty overlay.
Evidence collected on another revision needs the applicability check below.
Missing integration evidence, inaccessible decisions or contradictory versions
leave dependent acceptance unverified; still report independent observations.
If the supplied revision is superseded in the intended integration target,
assess applicability before claiming acceptance of the final current result.

## Assess complete behavior

1. Enumerate the full accepted criterion set; map each criterion to an actual
   observation, command/test or usable evidence address, outcome and revision.
   Preserve stable IDs if supplied. Do not silently drop failed or subjective
   criteria, or treat closed children as criterion coverage.
2. Exercise the meaningful cross-component scenarios through accepted test seams:
   normal flow, material error/rollback/boundary paths and shared contracts.
   A headless feature need not acquire a UI. Separate local unit/review evidence
   from the integrated behavior it actually demonstrates.
3. Check applicable architecture fitness: responsibility/state ownership,
   public contracts, dependency direction and project invariants. Use existing
   static/contract/integration checks where suitable; otherwise inspect the
   actual implementation and explain the assessment. Do not invent a required
   architectural style. Unchecked constraints are unverified, not passed.
4. Inspect affected documentation and examples against this integrated tree;
   future design must not be presented as implemented architecture. Check
   applicable navigation/format constraints on selected knowledge documents,
   without imposing them on ordinary feature specifications.
5. Compare only linked product/source scopes to their decision baselines. Mark
   absent baselines as currency unconfirmed. Distinguish editorial changes from
   material behavior changes; trace material impact to criteria, contracts,
   tasks/tests and evidence. Do not rewrite author-owned sources or accepted
   decisions to make the implementation pass. Independent coverage remains useful.
6. Subjective criteria require a relevant observation/playtest or owner decision
   for this version (or justified reuse). A successful build does not demonstrate
   balance, feel or visual quality. Ask for the missing decision only if necessary.

Run permitted non-mutating checks when needed, avoiding generated files in the
subject tree. If a check would write, use an authorized disposable environment
outside it or report the check unavailable; read-only does not authorize fixtures
inside the project. Record command, environment, exit/outcome and evidence.
Do not say a proposed command was run.

## Reuse and retry

For each reused check identify its original revision, tested scope, inputs and
environment. Inspect the intervening code, contracts, requirements, sources and
configuration changes and explain why they cannot invalidate that result on the
target tree. Merely having a green earlier run or independent review is insufficient.
Rerun affected checks; retain valid costly evidence instead of repeating blindly.
Unavailable evidence or uncertain applicability leaves that criterion unverified.

On failure return exact criterion/scenario, expected/observed result, evidence
and bounded repair/decision needs. Do not change requirements or open work yourself.
After an authorized repair is integrated, assess the new revision and complete
coverage again, keeping previous failure evidence and explaining reused results.
A fixed local branch alone does not establish a repaired integrated feature.

## Return and stop

Return `status: pass|fail|unverified`, feature identity, full revision/tree and
integration evidence, accepted scopes/versions/decisions, criterion coverage,
integration/architecture/docs/source-currency outcomes, check addresses and reuse
rationale, unresolved limitations and bounded recovery needs. `fail` means an
observed criterion/required check fails; `unverified` means no observed failure
but material evidence is missing. `pass` requires complete criteria and required
checks, usable evidence and no unresolved material limitation. State genuinely
inapplicable checks with reasons instead of pretending to have run them.
Check report completeness and revision consistency before returning. Passing
this method is not tracker completion, publication or permission to close.
