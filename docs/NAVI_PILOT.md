# NAVI pilot
This complementary gate uses profile python-tooling. Scope: Manifest validator unittest suite; not console recompilation certification.
Core SHA: e9fa2e4c825615ddc6f0a24b65d7139ec38fc477. Read-only workflow token, no inherited secrets, no
private export. No original workflow or application code changed. A passing
gate is not production certification. Merge only after reviewed Core and
pilot gates, actual restore-tested backup and rollout approval. Rollback:
revert the integration commit. No automatic merge or ruleset changes.


Validated release candidate: NAVI Core v0.2.0rc1. Complementary gate only; original CI and branch governance unchanged.

NEF candidate pin: c952bb80f33b3eee31de9a717298095154e1fd22. The original CSR workflow remains unchanged. The additional reference audit and migration preview are read-only; CI evidence must be checked before claiming validation. No AI provider required.
