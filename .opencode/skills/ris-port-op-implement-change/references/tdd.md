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

- On resumption inspect current tests/code and available observations; continue
  missing changes with test-first cycles and run applicable current checks. Do not
  reset or overwrite work to recreate RED. Missing historical chronology does not
  block final-result review or reuse, and passing tests do not prove past TDD.
  Never claim test-last as TDD or conceal a known violation.
- Behavior-preserving refactors use existing tests/characterization where needed
  and maintain GREEN; they do not require an artificial RED. Associated documents
  use their own checks. TDD does not waive project-mandated static/integration checks.
- Observe the actual expected RED and GREEN for each new behavioral slice; no
  saved cycle chronology or historical audit by reviewer/recovery/publication is
  required. Bind applicable final checks to the handed-off snapshot. Do not create
  a substitute implementation journal or copy cycle history into other artifacts.
