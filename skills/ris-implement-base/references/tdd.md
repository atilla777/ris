# Required test-first implementation

Read in `tdd` mode before changing behavior. The base owns this method; a caller
owns project/task integration. Use the established criteria and stable observable
test boundary; do not reopen accepted interfaces just to simplify a test.

## One vertical slice at a time

1. Choose one small required behavior. Write a focused test before its production
   change; expected results come from the requirement or an independent example.
   For a bug, reproduce the reported defect through the appropriate interface.
2. **RED:** run the test against the pre-change implementation. Inspect its actual
   failure: the assertion must expose missing/wrong behavior. Runner, import,
   compilation or environment failure alone is not RED; establish a runnable test
   and the expected behavioral failure before dependent production changes.
3. **GREEN:** implement only enough accepted behavior to pass this slice. Run the
   test, then the affected regression/contract checks. Investigate failures before
   building dependent slices; never weaken correct expectations to get green.
4. **REFACTOR, if useful:** make local behavior-preserving improvements within
   accepted design and rerun affected tests. Do not add speculative abstractions
   or change a public contract under the guise of refactoring. Repeat for the next
   behavior, learning from each completed slice rather than bulk-writing all tests.

Do not claim TDD from tests written after implementation, an unexecuted test or an
unrelated failure. If no meaningful expected RED can be established, report why
and block that behavioral change; do not silently switch modes or manufacture a
failure by breaking correct code. Independent authorized work may continue.

## Existing work, refactors and evidence

- On resumption, read existing tests, code and cycle evidence. Reuse an already
  proven RED/GREEN sequence only when its versions and behavior remain applicable;
  perform new cycles for uncovered behavioral changes. Do not reset or overwrite
  existing work to recreate RED. Missing historical evidence leaves that portion
  unverified, even if the final tests pass.
- Behavior-preserving refactors use existing tests/characterization where needed
  and maintain GREEN; they do not require an artificial RED. Associated documents
  use their own checks. TDD does not waive project-mandated static/integration checks.
- Preserve concise inspectable evidence for each behavioral slice: criterion/test,
  pre-change version, command and expected observed RED, resulting implementation
  version and GREEN, and any refactor checks. A complete transcript or separate
  file per cycle is unnecessary. Bind final checks to the handed-off snapshot.
