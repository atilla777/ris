# DragonRuby game engineering profile

Read for DragonRuby games only. Recommendations, not accepted project policy.
Official technical sources inspected **2026-10-12**. DragonRuby is a distinct
runtime; the FAQ describes Ruby 2.x-compatible syntax, a subset of MRI APIs and
no gem support. Live docs use both current `DR` and older `$gtk` examples: match
the actual SDK's docs/API, never rename working APIs merely to match a template.

## Justified minimum

| Practice/tool candidate | Why and proposed rule | Applicability/customization and limit |
|---|---|---|
| SDK version/license/target record and preserved toolkit layout | Reproduce runtime and packaged targets; native tools/filesystem depend on SDK layout | Identify SDK archive/revision and acquisition policy plus source/assets/metadata revisions. Runtime docs expose `version`; retain supported per-game layout. Do not publish licensed binaries unless project/license permits it |
| Runtime load/syntax diagnostics plus consistent reviewed Ruby style | The shipped interpreter is the language authority | Adopt existing style; no MRI `ruby -c`, RuboCop, Standard, Bundler or gems as a claimed DragonRuby runtime check. External host tools are conditional, version-pinned and must not emit unsupported syntax |
| Built-in DragonRuby unit-test facility | Test logic with the actual runtime without depending on an MRI test framework | FAQ documents `./dragonruby mygame --test tests/some_ruby_file.rb`; choose actual paths/platform invocation from SDK docs. Define assertions, reset/state isolation and reproducible seeds; do not promise a headless/display-free runner or exit semantics without SDK evidence |
| Package + target smoke-check policy | A dev tick loop does not establish distributed-game behavior | Deployment guide documents `./dragonruby-publish --package mygame` as packaging; the invocation without `--package` can publish. Proposed checks must use package-only where intended and target input/render/audio/save behavior; do not run either during rule authoring |

Consider independently testable simulation/logic with explicit inputs and
time/random controls, without mandatory rendering for each logical assertion.
This does not imply the runtime itself launches without a display. Where a
runner is unavailable, propose a truthful manual/runtime check and show the
automation gap. CI policy must state SDK acquisition/license, OS/display and
artifact access requirements instead of claiming CI is already configured.

Security/dependency policy can require provenance/licenses of vendored code,
assets and native libraries, no secrets in distributables and validation tests
for untrusted saves/network data. Bundler advisory scans do not cover the
DragonRuby SDK just because game sources use Ruby syntax.

## Conditional extensions

- Record/replay and reset seeds: runtime docs describe reproducible RNG and
  replay; choose for stateful regressions, preserve the tested code/SDK/replay
  revision. Hot reload is useful feedback, not proof of a clean boot.
- MRI-hosted formatting/linting: research actual parser support for the selected
  tool/SDK syntax and review autocorrection risk before proposing it. Passing
  host lint never replaces target-runtime checks. No default named host formatter
  is certified by this profile.
- Native extensions: confirm license tier, SDK compiler/ABI and each shipped
  target. Runtime docs describe Standard-tier packaging limitations; development
  loading alone does not prove production support.
- Frame-time/performance checks: only for a supplied budget, representative
  assets/hardware and a controlled scenario; avoid universal 60-fps assertions
  based merely on the tick API.

Review supports architectural ownership, lifecycle and considered reuse; an
engine-specific module may be useful without a separate repository or MRI gem.
Preserve existing task/publication norms even where upstream guides illustrate
direct upload. The author neither packages nor deploys nor installs tooling.

## Technical evidence

- [FAQ](https://docs.dragonruby.org/misc/faq.md): runtime versus MRI, no gems,
  replay and CLI unit-test example.
- [Runtime](https://docs.dragonruby.org/api/runtime.md): version, reset/RNG,
  replay, filesystem layout and native-extension license limits.
- [Updating SDK](https://docs.dragonruby.org/guides/updating-dragonruby.md):
  preserve game content when updating toolkit files; not an automatic upgrade.
- [Distribution](https://docs.dragonruby.org/guides/deploying-to-itch.md):
  layout, game metadata, package-only versus package-and-publish, web constraints.
