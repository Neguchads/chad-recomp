# CSR handoff

## Current objective

Maintain the universal game engineering standard and its manifest validator. NEF is an optional engineering assistant reference, not a runtime or build dependency.

## Baseline and evidence

Baseline before this documentation-only change: `63183d6fd2ce7f671e7208c4a34c91e5a6227257`.
The repository contains the normative draft, platform registry, adapter design, schema, example, validator and regression suite. Real console adapters and game certification remain unimplemented; consult the actual CI runs for test evidence. This handoff does not claim tests executed for the new revision before CI runs.

## Next steps

1. Review the existing [roadmap](../ROADMAP.md) and outstanding platform requirements.
2. For a new adapter, identify authorized inputs, precise tool revisions and independently verified capabilities.
3. Update contracts and tests together; execute the original validator gate.
4. Record real outcomes, limitations and next steps at the next session boundary.

## Constraints and rollback

Do not move existing folders to match a reference layout. Do not add proprietary inputs, game binaries or claims without verification. Revert only the reviewed documentation integration if needed; original CI and source layout remain intact.

NEF follow-up: the complementary gate now proposes a pinned Core upgrade and reference audit with no file changes. Check the corresponding pull request CI before reporting success.

## AutoVerify release-only integration

PR #4 documents the optional final stable delivery policy. Previous documentation
revision 2edcd0dab03eb24c8985e0f3888ee701bdbf064f passed CI runs 45926147839
and 45926148102. Core PR #36 passed run 45926014379 for pin
c6037185830f24770f856d4cd69791c686095bc5. Consumers: CDOS #59, CSOTN #19,
CCOD #16. Keep external lookups disabled until independent review, owner
authorization and live acceptance. No private material, file uploads or automatic
publication. New final revisions require their own CI results.
