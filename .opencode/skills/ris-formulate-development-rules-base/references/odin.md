# Odin game engineering profile

Read for Odin games only. Recommendations, not accepted project policy.
Technical sources inspected **2026-10-12**; compiler CLI evidence is the live
upstream source, not a support guarantee for older/nightly binaries. Record
the actual compiler revision and consult its command help before selecting flags.

## Justified minimum

| Practice/tool candidate | Why and proposed rule | Applicability/customization and limit |
|---|---|---|
| Pinned Odin compiler/revision, targets and external library/asset inputs | Reproduce build assumptions while language/compiler evolves | Record `odin version` identity, package collections, link libraries, build flags, OS/architecture and acquisition revisions. No assumed built-in Cargo-like package manager/lockfile |
| Compiler `odin check <package>` plus selected `-vet` diagnostics | Parse/type-check code with native diagnostics before expensive integration work | Upstream supports check and vet flags; customize exact supported diagnostics, scope and treatment of old findings from pinned-version help. A type-check does not link or execute tests |
| `odin test <package>` and `core:testing` | Built-in behavior checks and memory-use reporting | `@(test)` procedures accept `^testing.T`; default tests are in the selected package. Use an explicit package list/import harness and supported `-all-packages` if wider coverage is needed. Do not claim a single invocation recursively discovers all packages |
| `odin build <package>` and target artifact smoke checks | Verify linking, assets and runtime beyond check/test | Use actual target/link configuration and supported build options; native/GPU/foreign-library availability can limit CI. Pure simulation tests need no mandatory renderer; rendering tests still need the relevant environment |
| One existing style/format authority or reviewed style | Consistency without fictitious tooling | Compiler usage lists `strip-semicolon`, which removes unnecessary semicolons and is not a general formatter. No built-in `odin fmt` is evidenced. Select an external formatter only after researching exact version/behavior; retain existing usable tooling |

Memory checks should support accepted allocator/ownership/lifetime obligations.
Official testing docs describe memory tracking, bad-free/leak reports and
per-run seeds; define treatment of those reports rather than assuming warnings
always yield a failing exit code. Tracking does not prove correctness for every
foreign/custom allocator or GPU resource. Default parallel tests must not share
mutable fixtures unsafely; customize threads/seed only where supported/needed.

Security/dependency practices: track foreign library versions/provenance and
licenses, test untrusted input parsing and packaging without secrets. No generic
Odin security scanner is certified here. Reference architecture's invariants,
do not redefine memory or renderer architecture through a tooling recommendation.

## Conditional extensions

- Compiler `-vet` subsets, stricter style or warnings-as-errors: available in
  current upstream CLI but select only pinned-version supported flags and an
  agreed transition policy; never silence all diagnostics to make a gate green.
- Memory/seed/thread settings: testing docs describe `ODIN_TEST_TRACK_MEMORY`,
  `ODIN_TEST_RANDOM_SEED` and `ODIN_TEST_THREADS` compile-time definitions; use
  actual supported settings and record a failed seed for reproduction.
- External formatting, sanitizers, cross-target CI and performance budgets:
  research platform/compiler/library compatibility before a binding choice;
  not universal tools or guarantees supplied by this profile.

Review/DoD includes relevant initialization/cleanup/error paths, API/dependency
contracts and considered reuse. It does not demand ECS, a particular graphics
library, library extraction or another repository. Keep current delivery rules.

## Technical evidence

- [Odin overview](https://odin-lang.org/docs/overview/): package-based build/run,
  foreign interfaces, explicit memory and context.
- [Testing](https://odin-lang.org/docs/testing/): test procedures, package
  selection, memory reports, seeds and compile-time runner options.
- [Compiler CLI source](https://github.com/odin-lang/Odin/blob/master/src/main.cpp):
  check/build/test/version commands, vet flags and strip-semicolon; match the
  actual binary's help before using version-sensitive options.
