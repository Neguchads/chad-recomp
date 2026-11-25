# Chad Standard Recomp
### Universal Game Engineering Framework

**CSR 0.1.0 — draft standard and working manifest validator**

An open, console-agnostic engineering standard for native ports, static recompilation, decompilation, hybrid runtimes, emulator-based projects and original games. CSR does not itself translate game binaries or implement a console emulator.

[Português](README.pt-BR.md) · [Standard](docs/STANDARD.md) · [Platform matrix](docs/PLATFORMS.md) · [Toolchains](docs/TOOLCHAINS.md) · [Adapters](docs/ADAPTERS.md) · [Roadmap](ROADMAP.md)

## Quick start

```sh
python tools/validate.py examples/project.json
python -m unittest discover -s tests -v
```

Copy `examples/project.json` to your game's root as `csr.project.json`; choose a platform and execution profile; implement the adapter stages using your own build system. Read the standard before claiming compliance.

## Scope

- Common documentation, build, CI, release, save migration, license and provenance rules.
- Independent platform and toolchain profiles; multiple execution modes are allowed and must be disclosed.
- No proprietary ROM, firmware, keys, generated proprietary game code or assets distributed by this repository.
- Open-source original infrastructure under MIT; upstream dependencies retain their licenses.

## Status

This release contains a normative draft, research registry, manifest schema, CLI validator, tests, CI and project templates. Real console adapters, automatic translation, runtime libraries and game certification are not implemented.

## Optional engineering assistance

[Architecture](docs/ARCHITECTURE.md) · [Handoff](docs/HANDOFF.md) · [NAVI Engineering Framework references](docs/NEF.md). The original CSR layout and verification remain independent of any agent.
