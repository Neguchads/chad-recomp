# CSR 0.1.0 — normative draft

MUST = mandatory for the applicable profile; SHOULD = recommended with documented exceptions; MAY = optional. Conformance requires evidence, not merely presence of files.

## Profiles

`static-aot`, `decomp-port`, `native-compat`, `hybrid`, `emulator`, `original`. A project MUST disclose its actual execution mode and fallback. A hybrid or emulator project MUST NOT claim pure native AOT if guest instructions execute in JIT/interpreter.

## CSR-01 Governance
MUST include README, license scope, third-party notices, contribution instructions, supported input versions, known limitations and build instructions. Use SPDX identifiers. Do not relicense upstream code. Document provenance of generated and recovered code. Do not commit private game dumps, keys, firmware or unlicensed assets.

Optional distribution branding SHOULD follow [the official press badge convention](PRESS-BADGES.md) where applicable; a developer badge is not a conformance or release certification.

## CSR-02 Input and reproducibility
MUST identify authorized inputs by revision, size and SHA-256; reject mismatched inputs before generation. Pin toolchain revisions and dependency lockfiles. Record host OS, compiler, flags and generated output hashes. Separate immutable source/install from writable data. Use synthetic or redistributable fixtures in public CI.

## CSR-03 Architecture
MUST isolate guest ISA/ABI and hardware-specific code behind an adapter boundary. Separate generated code, handwritten runtime, patches, platform services and UI. Document guest endianness, memory layout, interrupts, timing, floating-point and concurrency semantics. Never silence unsupported instructions or return successful stubs without evidence. For original projects guest-specific requirements are N/A.

## CSR-04 Pipeline
SHOULD support analyze, generate, build, test, package and run stages. Incremental cache keys include input hash, tool revision, configuration, dependencies and relevant flags. Generated files are reproducible or explicitly identified as non-reproducible. Use clean CI builds as a control. Native compiler choice is per adapter: clang/GCC/MSVC/Rust/.NET etc.

## CSR-05 Verification
MUST include smoke tests and regressions for supported capabilities. Recomp profiles SHOULD compare instruction semantics, guest memory and deterministic traces against a reference. Match firmware/game version, input, timing and seed. Unavailable reference tests are recorded as N/A or blocked, not passed. Validate multi-CPU ordering, FPU edge cases, graphics and audio independently. Never claim full playability without documented gameplay coverage.

## CSR-06 Runtime and player data
MUST store settings, saves, logs and caches separately from immutable install. Validate schema versions; use atomic save/config writes and backup before migration. Record recovery, rollback and clean installation tests. Accessibility, localization, controls and graphical profiles SHOULD use platform-appropriate services.

## CSR-07 Extensibility
Mods and patches SHOULD declare identity, target version, dependencies, conflicts, trust and load order. Unknown combinations are unverified, not automatically enabled. Native mods are executable code; no sandbox claims without evidence.

## CSR-08 Release
MUST use versioned artifacts, changelog, hashes, license notices and documented support matrix. Scan packages for prohibited content. Pin CI dependencies and minimize privileges. Publish build provenance and SBOM where feasible. Separate nightly and stable. External launcher manifests MUST validate against upstream schemas; CSR manifest is not the RecompLauncher schema. Do not include generated proprietary content unless redistribution rights are established.

## CSR-09 Agents
AGENTS.md SHOULD contain build/test commands, architecture boundaries, safety and validation rules. AI contributions require the same evidence and review as human work; respect upstream contribution policies. Record unknowns and unresolved findings.

## Conformance levels
L0: documented manifest and license/input policy. L1: reproducible build, smoke/regression evidence. L2: tested distribution, updates, saves and compatibility. L3: differential/performance evidence (as applicable), security/provenance and extension contracts. Each level requires previous levels; mark N/A with rationale. A passing manifest is not a conformance certification.
