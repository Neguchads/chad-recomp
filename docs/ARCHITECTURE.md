# CSR repository architecture

This repository implements a documentation standard and Python manifest validator, not a game runtime or console emulator. Keep its actual structure; use CSR's game-recomp architecture recommendations in downstream games where applicable.

## Boundaries

- `docs/STANDARD.md`: normative engineering requirements.
- `docs/ADAPTERS.md`, `docs/PLATFORMS.md`, `docs/TOOLCHAINS.md`: proposed adapter contract and capability references, not implemented emulators.
- `registry/platforms.json`: platform reference registry.
- `schemas/csr.project.schema.json`: project contract.
- `tools/validate.py`: deterministic manifest validation.
- `examples/project.json`: illustrative input.
- `tests/test_validate.py`: validator regression tests.
- `.github/workflows/`: original verification and complementary NAVI pilot.

Changes to contracts, registry and validator need coordinated tests and documentation. Do not add empty runtime, generated-code or asset directories to a standard-only repository.

## Verification and limitations

Run `python tools/validate.py examples/project.json` and `python -m unittest discover -s tests -v`. The validator does not demonstrate translation correctness, native playability, runtime behavior or console conformance.

Architecture references: [CSR standard](STANDARD.md), [adapter contract](ADAPTERS.md), [roadmap](../ROADMAP.md).
