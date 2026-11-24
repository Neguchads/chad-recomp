import copy
import json
import unittest
from pathlib import Path
from tools.validate import validate, SCHEMA

ROOT = Path(__file__).resolve().parents[1]
class Tests(unittest.TestCase):
    def setUp(self): self.d = json.loads((ROOT / "examples/project.json").read_text())
    def test_example(self): self.assertEqual(validate(self.d), [])
    def test_missing(self): del self.d['toolchain']; self.assertTrue(validate(self.d))
    def test_unknown_platform(self): self.d['platform']='invalid'; self.assertTrue(validate(self.d))
    def test_aot_fallback(self): self.d['fallback']='jit'; self.assertTrue(validate(self.d))
    def test_hybrid(self): self.d.update(mode='hybrid',fallback='jit'); self.assertEqual(validate(self.d),[])
    def test_duplicate_hosts(self): self.d['hosts']*=2; self.assertTrue(validate(self.d))
    def test_unknown_field(self): self.d['run']='anything'; self.assertTrue(validate(self.d))
    def test_bad_root(self): self.assertTrue(validate([]))
    def test_original(self): self.d.update(platform='original',mode='original',fallback='not-applicable'); self.assertEqual(validate(self.d),[])
    def test_original_wrong_mode(self): self.d['platform']='original'; self.assertTrue(validate(self.d))
    def test_registry_consistency(self):
        items=json.loads((ROOT/'registry/platforms.json').read_text())
        ids=[i['id'] for i in items]; self.assertEqual(len(ids),len(set(ids)))
        self.assertEqual(set(ids)|{'original'},set(SCHEMA['properties']['platform']['enum']))
