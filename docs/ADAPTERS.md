# Adapter contract (design, not yet implemented)

Platform profile identifies guest CPU, ABI, endian, binary/container types, coprocessors and peripheral services. Toolchain adapter identifies exact tool version, supported input variants and stages. Host profile identifies OS, architecture, compiler, graphics/audio and packaging. Keep these dimensions independent.

| Stage | Input | Output |
|---|---|---|
| probe | local authorized dump, manifest | verified identity and capability report |
| analyze | verified input, symbols, pinned tools | function map, imports, unresolved items |
| generate | analysis, config, tool revision | generated code and translation report |
| build | runtime, generated code, host profile | binary and build manifest |
| test | binary, fixtures, reference traces | evidence, failures, blocked checks |
| package | binary and redistributable files | release artifact, hashes, provenance |
| run | binary, read-only install and data directory | execution logs, exit status |

Every stage must report success/failure, input hashes, tool identity and output paths. Never execute untrusted manifest shell strings. Use explicit argument arrays, validated local paths and timeouts in future runners. Support not-applicable stages for source ports/original projects; do not pretend they ran. Keep emulator reference adapters distinct from runtime adapters. A JIT fallback is declared in capability and runtime diagnostics. External launchers get their own validated adapter, never an invented upstream schema.

## Incremental model
Cache stage outputs by canonical inputs, tool revision and transitive dependencies; invalidate dependent stages when their inputs change. Do not share private game-code caches across unrelated projects or upload them to public CI artifacts.
