# Rails web engineering profile

Read for Rails web only. Recommendations, not automatically accepted norms.
Technical sources inspected **2026-10-12**; live upstream docs do not certify
every Ruby/Rails/gem combination. Consult the project's version-matched docs,
Gemfile/lockfile, binstubs and CI settings before selecting exact versions.

## Justified minimum

| Practice/tool candidate | Why and proposed rule | Applicability/customization and limit |
|---|---|---|
| Ruby/Rails/Bundler version record; Gemfile + Gemfile.lock | Reproduce the application's dependency resolution; use bundle-scoped executables/binstubs | Pin the project's supported combination and target/native platforms; dependency updates are deliberate, not blanket `bundle update`. Lock inputs alone do not prove native build or DB reproducibility |
| Existing RuboCop/style authority; `rubocop-rails-omakase` for an uncommitted style | A coherent, Rails-maintained starting style without designing a new dialect | Omakase is included by new Rails 7.2+ applications according to its README, not guaranteed in every app. Retain existing RuboCop/Standard/custom policy; check gem compatibility, scope/exclusions and whether `bin/rubocop` exists. Autocorrection is a separate write operation |
| Rails/Minitest test runner for a new default app | Framework-supported models, requests, jobs and integration assertions | Candidate `bin/rails test`; Rails documents that this excludes system tests. Retain an established RSpec suite rather than migrating it. Use actual bundle commands and isolated test DB/schema |
| Targeted UI/system checks if browser/JS behavior matters | Request tests cannot establish browser behavior | Candidate `bin/rails test:system` only with applicable runner/browser support; API-only apps need not add browser tests |
| Brakeman and bundler-audit for applicable Rails/gem security checks | Brakeman analyzes Rails security patterns; bundler-audit checks lockfile advisories/insecure sources | Confirm supported parser/runtime versions and invocation. Candidate bundle-scoped `brakeman`, `bundle-audit check --update`; record advisory DB revision/freshness and offline limits. Neither is a general proof of security |

Use the common foundation for documentation/review/CI/DoD. For Rails make
integration requirements concrete where relevant: authorization failures,
transactions/rollback, DB constraints, job retry/idempotency and external API
failure paths support the project's architectural contracts. Do not define
those contracts here or require Service Layer/extra testing gems by default.

## Conditional extensions

- Existing RSpec, frontend formatter/linter/test runner: retain with its own
  supported versions and lockfile when present; inspect its docs if recommending
  new behavior. Rails alone does not require a JavaScript package-manager stack.
- Eager-load check, system-browser matrix and migration checks: select only for
  applicable deployment/autoload/DB/UI risks and actual runner capabilities.
- Performance/query regressions: define a representative measured budget when
  the project's requirement justifies it, not a generic benchmark gate.

If existing accepted style/tests disagree with the default, customize around
them. If a security-tool recommendation is unsupported in the actual version,
mark the gate unresolved rather than silently upgrade Ruby/Rails or disable it.

## Technical evidence

- [RubyGems dependency management](https://guides.rubygems.org/dependency_management/):
  application lockfiles, bundle-scoped executables and selective updates.
- [Rails testing](https://guides.rubyonrails.org/testing.html): test runner,
  test database, Minitest, integration/system separation and CI.
- [Rails Omakase README](https://github.com/rails/rubocop-rails-omakase):
  intended starting point, existing house-style preservation and Rails 7.2+.
- [Brakeman documentation](https://brakemanscanner.org/docs/):
  Rails-specific static security checks and false-positive disposition.
- [bundler-audit README](https://github.com/rubysec/bundler-audit):
  lockfile advisories, insecure sources, update/no-update and ignored advisories.
