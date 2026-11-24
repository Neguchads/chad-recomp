# Building and validation
Requires Python 3.10+ (CI uses 3.12). No package dependencies. Run from repository root:
```sh
python tools/validate.py examples/project.json
python -m unittest discover -s tests -v
```
The sample revision is intentionally a placeholder. This validates manifest structure, not a real build or game. Configure the actual toolchain and test evidence in the consuming project.
