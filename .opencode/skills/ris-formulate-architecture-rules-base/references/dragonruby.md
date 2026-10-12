# DragonRuby game architecture profile

Read only for DragonRuby game scope. Specialize the shared foundation without
choosing ECS, scene hierarchy, a global event bus or a separate game engine.

## Recommended minimum and choices

- Assign one loop coordinator and distinguish input translation, gameplay state
  transition and presentation responsibilities. These can be functions in a
  small game, not mandatory separate packages. Define the order necessary to
  avoid presentation-dependent gameplay; do not invent a fixed-step model.
- Assign a logical writer for each gameplay state group. `args.state` is a
  runtime storage facility, not permission for every subsystem to mutate every
  field. Pass the required state/commands through agreed interfaces; decide
  between runtime state and class-owned state from the project's needs.
- State initialization, reset, scene/session transitions and durable save
  ownership when applicable. Class-owned state outside `args.state` needs an
  explicit reset policy; do not assume the runtime resets all globals/objects.
  For saves specify game data versus runtime/render objects, restore validation,
  compatibility and the invariant after a failed load when needed.
- When reproduction, replay or timing-sensitive behavior matters, define the
  owner/source of time and randomness and the intended scope of reproducibility.
  A seed alone is not a cross-platform determinism guarantee. No replay or
  network synchronization requirement follows from using DragonRuby.
- Consider independent observation of gameplay transitions without requiring
  rendering in every logical check. A test seam can supply state and input to
  gameplay logic within the actual runtime. Do not promise a headless runtime
  or ordinary Ruby tool compatibility without checking the installed edition.

Verification expectations: an input → step → presentation example, mutation
through the owned interface, reset/restart from changed state, and save/replay
failure or reproducibility cases only when their requirements are present.
Exceptions follow the common authority/scope/reason policy.

## Reuse specialization

Require consideration during design/review under the shared reuse norm. A
candidate should name real consumers, gameplay-independent responsibility,
interface/state ownership, initialization/reset and required DragonRuby API.
Passing the entire `args` object to all consumers is not itself a boundary:
document what a runtime-dependent module may access. Pure data/logic interfaces
are useful where feasible, but a library may honestly target DragonRuby.
Do not automatically split a small game's simulation into a separate repository.

## Technical basis and limitations

Checked 2026-10-12 against the official contribution repository at
`9bbfe79586a1bb1cad2fcfb0d5264f4edb113fa0`:

- [State](https://github.com/DragonRuby/dragonruby-game-toolkit-contrib/blob/9bbfe79586a1bb1cad2fcfb0d5264f4edb113fa0/docs/api/state.md):
  `args.state` persists between `tick` invocations and clears on `DR.reset`;
  class/instance state outside it requires a reset function/policy. The docs
  mention `boot` initialization as recommended with a future enforcement note;
  do not reinterpret that note as a universal current-version requirement.
- [Outputs](https://github.com/DragonRuby/dragonruby-game-toolkit-contrib/blob/9bbfe79586a1bb1cad2fcfb0d5264f4edb113fa0/docs/api/outputs.md):
  `tick args` submits primitives through `args.outputs`; rendering remains a
  runtime boundary even if gameplay checks can be isolated.

These documented API facts are not a tested version matrix. Check the target
runtime's bundled docs for API, edition and lifecycle specifics before depending
on them. MRI gems, syntax tooling, headless execution and native-extension support
are not established here; engineering recommendations need separate evidence.
