# Odin game architecture profile

Read only for Odin game scope. Apply the shared principles to packages and
explicit resource lifetimes; no graphics library, ECS or scene model is implied.

## Recommended minimum and choices

- Define the necessary package responsibilities, allowed import direction and
  public API. A directory-based package is a physical unit, not evidence that
  every declaration is a intended public contract: declarations are public by
  default; use a declared internal/private policy to protect implementation
  details. Do not impose a separate package for every tiny function.
- Separate simulation responsibility from platform/window/input and rendering
  responsibility at the contracts needed now. State who mutates gameplay data
  and who owns GPU/platform handles. Choose an actual dependency direction from
  known interfaces, without banning a practical combined adapter in a small game.
- For data and resources crossing boundaries define owner, borrowed/owned result,
  allocator choice, valid lifetime and who frees it. Passing a slice/map/pointer
  is not proof of deep copying or transfer of ownership. Avoid retained views
  into memory reset before consumers finish.
- Account for implicit `context.allocator` and `context.temp_allocator` as well
  as explicit allocator arguments. Specify who resets temporary storage and at
  which lifecycle boundary; persistent state must not outlive its backing arena.
  Choose per-frame/scene/general allocators only when justified by actual lifetime.
- Specify init/shutdown order, partial-initialization failure cleanup, and public
  error/result conventions for relevant resources. `defer` helps scope cleanup,
  but does not define ownership or automatically solve lifetime across scopes.

Verification expectations include import/API boundary inspection, a consumer
using a published procedure without internal coupling, repeated init/shutdown,
failed initialization with cleanup, and a borrowed-result lifetime example.
These are prospective checks, not executed memory diagnostics or tooling setup.
Exceptions follow the common authority/scope/reason policy.

## Conditional extensions and reuse

Only actual concurrency requirements activate thread ownership, synchronization
and allocator/resource access across workers. FFI/platform/render requirements
activate handle and foreign-call lifetime/calling-convention questions. Do not
infer thread safety or portability of a selected graphics API from Odin itself.

Under the shared game reuse norm, evaluate a stable independently useful package
with actual consumers. A reusable module/library exposes its allocation policy,
borrow/transfer semantics, error contract and cleanup obligations alongside
dependencies and applicability. A renderer-dependent library can be useful;
an engine-neutral universal core or separate repository is not required.
Do not extract packages or design an unrequested feature here.

## Technical basis and limitations

Checked 2026-10-12 against the official
[Odin overview](https://odin-lang.org/docs/overview/):

- [Packages/exported names](https://odin-lang.org/docs/overview/#packages):
  packages are directories, declarations are public by default, `@(private)`
  and file-private declarations restrict visibility.
- [Implicit context/allocators](https://odin-lang.org/docs/overview/#implicit-context-system):
  Odin uses manual memory management, an implicit procedure context, and general
  and temporary allocators; temporary storage must be explicitly cleared at its
  chosen lifecycle boundary.
- [Procedure parameters](https://odin-lang.org/docs/overview/#parameters):
  pointer-bearing values such as slices are passed without copying their backing
  elements. [Defer](https://odin-lang.org/docs/overview/#defer-statement) runs at
  scope exit, in reverse declaration order.

The overview is unversioned and compiler-specific defaults may change. Confirm
details against the target compiler/library and actual resource API before
depending on them. Compiler version, diagnostics and test/build tools belong to
engineering rules; no runtime or graphics compatibility matrix is claimed here.
