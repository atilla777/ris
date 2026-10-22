# Native-bug review basis

Read only for a supplied exact native bug, before selecting the review basis.
Use ordinary typed bug reads and retrieve the full current report (including
the exact published file when linked), aligned criteria and accepted constraints/
decisions with their authority. A sufficient report replaces formal spec/design,
not authority or separate acceptance of material design. Select by the **actual
subject**, not the existence of a bug ID:

- **Pre-execution design/document review:** bind the exact document candidate and
  separate acceptance decision where applicable to the full current report/criteria/
  accepted constraints and source versions. No future historical execution-input
  snapshot, fix implementation, implementation checks or execution plan/omission
  decision is required for this subject. Compare current inputs with that bound
  basis; material drift returns affected design/document evidence for reassessment.
  This exception does not accept the design or approve a future fix. Keep independent
  review, applicable document checks and complete candidate-tree binding.
- **Fix implementation review, including its publication gate:** additionally read
   the full used historical inputs through the adapter at project/tracker + bug ID +
   exact record version and used immutable Git source/decision locators; name that
   basis in the report. A number/hash or inaccessible link alone is insufficient;
   missing used fields block approval. No full notes snapshot/text handoff is required;
   preserve legacy snapshots as actual historical inputs without migration. Compare
  current report/criteria/decisions with that basis and bind exact candidate/check
  versions to original divergence and affected regressions. Material drift requires
  targeted change/review/evidence applicability assessment before approval,
  preserving compatible evidence with reasons. Never approve a changed expectation
  just because the implementation passes it. Assess sufficient accepted technical
  inputs and current code/tests, not the author's plan or TDD-history persistence.
  A mixed implementation/document subject retains these implementation guards;
  it cannot select the pre-execution exception.
