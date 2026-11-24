"""CSR v0.1 manifest validator; standard library only. No project execution."""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = json.loads((ROOT / "schemas/csr.project.schema.json").read_text(encoding="utf-8"))

def validate(d):
    errors = []
    def check(value, spec, path):
        if "const" in spec and value != spec["const"]:
            errors.append(f"{path}: expected {spec['const']!r}")
        if "enum" in spec and value not in spec["enum"]:
            errors.append(f"{path}: unsupported value")
        t = spec.get("type")
        if t == "object":
            if not isinstance(value, dict):
                errors.append(f"{path}: expected object"); return
            props = spec.get("properties", {})
            for k in spec.get("required", []):
                if k not in value: errors.append(f"{path}.{k}: required")
            for k, v in value.items():
                if k in props: check(v, props[k], f"{path}.{k}")
                elif spec.get("additionalProperties") is False: errors.append(f"{path}.{k}: unexpected field")
        elif t == "string":
            if not isinstance(value, str): errors.append(f"{path}: expected string"); return
            if len(value) < spec.get("minLength", 0): errors.append(f"{path}: too short")
            if "pattern" in spec and re.fullmatch(spec["pattern"], value) is None: errors.append(f"{path}: invalid format")
        elif t == "array":
            if not isinstance(value, list): errors.append(f"{path}: expected array"); return
            if len(value) < spec.get("minItems", 0): errors.append(f"{path}: too few items")
            if spec.get("uniqueItems") and len({json.dumps(v, sort_keys=True) for v in value}) != len(value): errors.append(f"{path}: duplicate items")
            for i, v in enumerate(value): check(v, spec["items"], f"{path}[{i}]")
    check(d, SCHEMA, "project")
    if isinstance(d, dict):
        if d.get("mode") == "static-aot" and d.get("fallback") != "none": errors.append("static-aot cannot declare guest JIT/interpreter fallback; use hybrid")
        if d.get("mode") == "original" and (d.get("platform") != "original" or d.get("fallback") != "not-applicable"): errors.append("original requires original platform and not-applicable fallback")
        if d.get("platform") == "original" and d.get("mode") != "original": errors.append("original platform requires original mode")
    return errors

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("manifest", type=Path)
    args = p.parse_args()
    try: errors = validate(json.loads(args.manifest.read_text(encoding="utf-8")))
    except (OSError, UnicodeError, ValueError) as e: errors = [str(e)]
    if errors:
        print("INVALID: " + "\n".join(errors)); return 1
    print("VALID manifest (structure only; not a compatibility certification)")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
