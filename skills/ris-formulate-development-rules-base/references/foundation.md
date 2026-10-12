# Engineering foundation

Use for create and scoped update. This is a decision aid, not the target
project's accepted policy. Do not publish unused alternatives or empty sections.

## Minimum substantive coverage

- **Environment/reproducibility:** identify supported runtime/compiler/framework
  versions, OS/architecture targets, dependency source and pinned revision/lock
  policy, build inputs/options, generated artifacts and asset provenance. Record
  how a clean environment reproduces the build; reproducible inputs do not imply
  bit-identical binaries. Upgrades need a purpose, compatibility evidence and
  applicable regression checks, not "always latest".
- **Style/static checks:** one coherent style and formatting authority per file
  kind; lint/diagnostic scope, excluded generated/vendor files and handling of
  existing findings. Name only tools actually supported by the stack. A manual
  review rule is legitimate where an automation tool is unavailable; do not
  describe manual review as a passing automated gate.
- **Testing:** meaningful behavior/regression assertions for changed risk, tests
  at public seams and necessary integration paths. Distinguish pure logic,
  runtime integration and UI/platform smoke checks. Record fixtures/environment,
  time/random controls, commands and evidence sufficient to reproduce failure.
  A clean compiler run is not a test suite; a green unit suite does not establish
  rendering, packaging, transaction or external-service behavior. No mandatory
  tests mirroring implementation or arbitrary universal coverage target.
- **Security/dependencies:** select checks for actual risks: known-vulnerable
  dependencies, untrusted network/save input, secrets and distributable assets,
  native library provenance/licensing. State database freshness/offline limits
  and exception authority; scanner output is not proof of absence of flaws.
- **Docs/review:** keep affected public usage, contracts, setup and rule references
  current; review correctness, tests, applicable architecture obligations and
  justified exceptions. For games include consideration of reuse and, when
  extraction is already justified, checks of interfaces, runtime/memory/lifecycle
  obligations. Review does not itself extract a library or redefine architecture.
- **CI/DoD:** define required versus conditional checks, trigger/scope, local/CI
  environment, pass/fail treatment and evidence tied to the checked revision.
  Missing infrastructure is an explicit limitation or separately proposed setup,
  not an invented running CI job. Material skips/exceptions identify reason,
  authority, affected scope and revisit condition; actual owner is supplied or
  visibly proposed. DoD includes applicable tests, reviewed changes, affected
  docs and unresolved-risk disposition while retaining existing delivery rules.

## Customization and transition

Start from observed tooling plus accepted norms. Select a profile recommendation
only where it fills a real gap. Document why a tool/practice is retained, chosen,
deferred or excluded; keep optional alternatives out of binding text. A useful
selection record is: goal → current equivalent → supported candidate/evidence →
project customization → expected check/result → limitation/exception.

An existing project may enforce rules for new/touched code with an agreed,
bounded baseline exception. Do not silently whitelist all warnings, reformat
the repository, replace a working test framework, or claim debt is remediated.
Preserve the actual task, permission, approval and publication procedure, even
if the profile's illustrative workflow differs. A conflict is an open decision,
not permission to rewrite that process.

## Failure signals and corrective reactions

- Proposed command is absent from version-matched docs/help: investigate or mark
  unsupported and leave the dependent gate unselected; never fabricate success.
- Formatter emits syntax unavailable in runtime: exclude it as a default pending
  compatibility evidence; target-runtime validation remains necessary.
- CI cannot access licensed SDK/display/native dependencies: record that gap and
  a feasible scoped/manual check proposal; do not promise headless execution.
- Tests are green but use a different runtime/target than the shipped artifact:
  narrow the claim and require the relevant runtime/platform evidence in policy.
- Gate contradicts publication/approval rules, or a version change alters an
  architecture contract: expose the conflict and required adjacent decision.
- Update unexpectedly needs whole-project migration: return the bounded proposal
  and unresolved dependency rather than expand scope or create a backlog.
