# Rails web architecture profile

Read only for Rails web scope. Add these specializations to the shared foundation;
they are recommendations to instantiate, not already accepted project rules.
No mandatory Service Layer, Rails Engine, database or job backend is implied.

## Recommended minimum and choices

- Name necessary domain responsibilities and their public operations. Framework
  folders are not by themselves domain boundaries. Specify who may query or
  mutate another domain's records and which interface preserves its invariants;
  do not categorically prohibit Active Record associations or shared tables.
- For components actually used, distinguish request/response orchestration in
  controllers, data/domain invariants in their chosen owner, and job execution
  from the same business rules. Choose where multi-record/use-case operations
  live from actual complexity; service objects are an option, not a required
  extra layer. Jobs/controllers must not independently redefine shared rules.
- Assign authorization responsibility and required identity/context at every
  relevant entry point, including background/external entry points when used.
  Do not prescribe a particular authorization gem or silently assume trusted jobs.
- For persistent invariants state the atomic boundary and concurrency obligations.
  Specify what happens to external effects on rollback/commit, and which failures
  can be retried safely. An Active Record transaction is scoped to a database
  connection; it does not make an external API or independent connection atomic.
- For used external APIs/jobs define the public error and compatibility policy,
  committed-data visibility and duplicate/retry semantics. `after_commit` timing
  alone is not a durable delivery or exactly-once guarantee; choose reliable
  delivery mechanisms only when the requirement justifies them.

Verification expectations include a cross-domain caller through its allowed
interface, unauthorized input at applicable entry points, rollback of a material
multi-write operation and repeated/failed external delivery when relevant.
Specify expected outcomes, not a prescribed test suite or CI implementation.
Exceptions use the common authority/scope/reason policy.

## Conditional extensions

Multi-tenancy, multiple databases, caches, asynchronous workflows, public API
versioning and engines activate only for real needs. Record the owner of cached
truth/invalidations or asynchronous state before suggesting mechanisms.
Existing Rails conventions and working contracts are evidence to preserve unless
the requested change conflicts with them. Exact Ruby/Rails versions, linters,
test framework and dependency management belong to development rules.

## Technical basis and limitations

Checked 2026-10-12 against official
[Active Record Transactions API (Rails 8.1.4)](https://api.rubyonrails.org/v8.1.4/classes/ActiveRecord/Transactions/ClassMethods.html):
transactions are per connection, Ruby instance state is not restored by database
rollback, nested transactions normally join the parent (`requires_new` commonly
uses savepoints), `after_commit` occurs after commit. These facts motivate the
boundary/failure questions, not a mandate to upgrade to this Rails version.
Check the actual project's Rails/database/job adapter documentation before
depending on version-specific behavior. No runtime execution or backend
compatibility beyond the cited facts is claimed by this resource.
