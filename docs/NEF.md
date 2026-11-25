# Optional NAVI Engineering Framework (NEF)

CSR defines domain-specific game engineering requirements. NEF supplies provider-independent engineering assistance. Neither requires a specific AI provider.

The repository itself uses Python validator verification and a documentation architecture reference. A downstream game can use the game-recomp architecture reference independently of its own executable test profile.

Once a reviewed NEF release is available locally, inspect without changing files:

    navi standard --profile game-recomp
    navi audit --root . --profile documentation --mapping docs/NEF_REFERENCES.json
    navi migrate --root . --profile documentation --mapping docs/NEF_REFERENCES.json

Use the existing root ROADMAP.md, docs/STANDARD.md and adapter documents rather than duplicating or moving them. Optional references missing from the audit are recommendations, not failed tests. The original CSR gate remains authoritative.

For any compatible agent, export public reference instructions with:

    navi assist --profile game-recomp --format markdown

For implementation tasks, clarify material ambiguities, record acceptance and maintain the handoff. Learn only from explicitly approved sanitized lessons outside Git. Never publish private prompts, source, game inputs, credentials or logs. NEF is optional; the CSR validator runs without it.

Framework: https://github.com/Neguchads/navi-core
