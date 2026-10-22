# Path bases and checks

Read before resolving/checking paths. Read `shared-primary.md` from this same
installed resource directory only when shared workspace paths are needed.

- Resolve `sources.*` against the selected `project_root` in the **current**
  working copy. These values designate directories, not specific documents.
  `product` and `rules` denote separate OKF 0.2 bundles in the default RIS
  documentation profile, with `rules/architecture/adr/` nested inside rules;
  new feature `specs/<full feature ID>/spec.md` is ordinary Markdown. Context checks path availability,
  not OKF validity or the contents/acceptance of a document. A project may
  choose different directories without changing these roles.
- Resolve relative `workspace.*` against the Git-derived ordinary source folder
  returned as `primary_root` by `shared-primary.md`. Apply that resource before
  shared-path use, also from the source copy itself. There is no saved-primary
  cascade or folder-existence fallback. The two workspace leaves retain their
  package defaults unless explicitly overridden by a valid config leaf.
  Path resolution grants no authority to mutate the source checkout.
- Config location does not move either root. Absolute path values remain
  absolute, subject to scope and access checks. Do not interpolate `~`,
  `${ENV_VAR}` or `{{variable}}`. For `..`, symlinks or paths outside the
  selected root, inspect the actual target and authorized scope; explicitly
  approved external storage may be used, silent escape may not. Resolve
  Markdown links from the document's directory, not the path's config base.
- If a required **input** directory is missing or inaccessible, diagnose the
  current-copy path gap; block only work that requires that local path. This is
  not proof that linked published inputs are absent. The calling owner applies
  common's conditional `published-inputs.md` to retrieve pinned content/decisions
  and distinguish source availability, target applicability and copy preparation.
  Context does not select/read those documents or update the checkout. A prospective **output** directory need not yet exist
  if creation is permitted; do not switch defaults/overrides because it is absent.
  The result owner creates the missing output during its authorized operation;
  check authorization and conflicts when the
  result owner actually writes. If writing is not authorized, return a
  proposal without claiming creation. Directory presence does not validate
  a document's content, acceptance, or OKF format.
- `workspace.tasks` and `workspace.worktrees` are base directories only.
  Without a confirmed tracker task ID, do not invent an `<id>` folder,
  project slug or branch name. Never create directories or worktrees here.
  Re-resolve paths in each recipient's environment after project/worktree or
  container changes; do not cache local absolute paths in `ris.yaml`.
