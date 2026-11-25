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
