import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from imo_validation_claim_audit.audit import audit, claims, evidence
from imo_validation_claim_audit.phrases import IMOVALIDATION, NOIMOVALIDATION, GENERIC_NAMES

ROOT = Path(__file__).resolve().parents[1]


class AuditTests(unittest.TestCase):
    def test_claims(self):
        for phrase in IMOVALIDATION:
            with self.subTest(phrase=phrase):
                self.assertEqual(claims(phrase), (True, False))
        for phrase in NOIMOVALIDATION:
            with self.subTest(phrase=phrase):
                self.assertEqual(claims(phrase), (False, True))
        for text, result in [('documented imo validation claim false', (True, False)), ('imo validation claim audit', (True, False)), ('documented no imo validation claim false', (False, True)), ('doesn’t validate-imo', (False, True)), ('```\nvalidate imo\n```', (False, False)), ('`validate imo`', (True, False)), ('invalidates imogen', (False, False))]:
            with self.subTest(text=text):
                self.assertEqual(claims(text), result)

    def test_routes(self):
        routes = []
        for method in ('validate', 'is_valid'):
            routes.extend(['import stdnum.imo\nstdnum.imo.'+method+'(x)', 'import stdnum.imo as fg\nfg.'+method+'(x)', 'import stdnum\nstdnum.imo.'+method+'(x)', 'from stdnum import imo\nimo.'+method+'(x)', 'from stdnum.imo import '+method+'\n'+method+'(x)', 'from stdnum.imo import '+method+' as v\nv(x)'])
        for name in GENERIC_NAMES:
            routes.extend(['obj.'+name+'(x)', 'obj = object()\nobj.'+name+'(x)', 'from library import '+name+'\n'+name+'(x)', 'from library import '+name+' as f\nf(x)'])
        for route in routes:
            with self.subTest(route=route):
                self.assertTrue(evidence(route))

    def test_not_evidence(self):
        cases = ['import stdnum.imo', 'imo', 'validate(x)', 'is_valid(x)', 'compact(x)', 'calc_check_digit(x)', 'format(x)', 'validate_imo(x)', 'obj.validate(x)', 'obj.is_valid(x)', 'obj.imo(x)', 'obj.compact(x)', 'obj.calc_check_digit(x)', 'obj.format(x)', 'import stdnum.imo\nstdnum.imo.compact(x)', 'import stdnum.imo\nstdnum.imo.format(x)', 'import stdnum.imo\nstdnum.imo.calc_check_digit(x)', 'from stdnum import ean\nean.validate(x)', 'from stdnum import ean\nean.calc_check_digit(x)', 'from stdnum import luhn\nluhn.validate(x)', 'from stdnum import luhn\nluhn.calc_check_digit(x)', 'import re\nre.match("IMO", x)', 'import re\nre.search("IMO", x)', 'import re\nre.fullmatch("IMO", x)', 'len(x)==7', 'x.isdigit()', 'x.removeprefix("IMO")', 'x.startswith("IMO")', 'imei.validate(x)', 'imsi.validate(x)', 'mmsi.validate(x)', 'hin.validate(x)', 'eni.validate(x)', 'registry.lookup(x)', 'ais.track(x)', 'validators.imo(x)', 'idutils.is_imo(x)', '"validate imo"', '# obj.validate_imo(x)', 'obj.validate_imo', 'def broken(:', 'import stdnum.imo as m\nm = None\nm.validate(x)', 'from stdnum.imo import validate\ndef validate(x): pass\nvalidate(x)', 'from lib import validate_imo as f\nwith open(x) as f: pass\nf(x)', 'import lib as x\nwith open(y) as x: pass\nx.validate_imo(z)', 'def validate_imo(x): pass\nobj.validate_imo(x)', 'import subprocess\nsubprocess.run(["checker", x])']
        for case in cases:
            with self.subTest(case=case):
                self.assertFalse(evidence(case))

    def test_audit(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp)
            (p/'README.md').write_text('validate imo')
            self.assertEqual(audit(p)[0]['severity'], 'HIGH')
            (p/'tests').mkdir()
            (p/'tests/test_x.py').write_text('import stdnum.imo\nstdnum.imo.validate(x)')
            self.assertEqual(audit(p)[0]['severity'], 'MEDIUM')
            (p/'a.py').write_text('import stdnum.imo')
            (p/'b.py').write_text('stdnum.imo.validate(x)')
            self.assertEqual(audit(p)[0]['severity'], 'MEDIUM')
            (p/'a.py').write_text('import stdnum.imo\nstdnum.imo.validate(x)')
            self.assertEqual(audit(p), [])
            (p/'README.md').write_text('no imo validation')
            self.assertEqual(audit(p)[0]['id'], 'documented-no-imo-validation-claim-false')
            self.assertEqual(audit(p, ['a.py']), [])
            (p/'a.py').unlink()
            self.assertEqual(audit(p), [])

    def test_cli(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp)
            (p/'README.md').write_text('validate imo')
            (p/'test_x.py').write_text('import stdnum.imo\nstdnum.imo.validate(x)')
            cmd = [sys.executable, '-m', 'imo_validation_claim_audit', 'audit', tmp]
            result = subprocess.run(cmd+['--json'], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0)
            self.assertEqual(json.loads(result.stdout)['findings'][0]['id'], 'documented-imo-validation-claim-false')
            self.assertEqual(subprocess.run(cmd+['--fail-on', 'medium'], capture_output=True).returncode, 2)
            self.assertEqual(subprocess.run(cmd+['--ignore', 'test_x.py'], capture_output=True).returncode, 2)
            self.assertEqual(subprocess.run(cmd+['--fail-on', 'HIGH'], capture_output=True).returncode, 1)
            self.assertEqual(subprocess.run([sys.executable, '-m', 'imo_validation_claim_audit', 'audit', tmp+'/missing'], capture_output=True).returncode, 1)

    def test_readme(self):
        text = (ROOT/'README.md').read_text()
        self.assertEqual(claims(text), (False, False))
        self.assertEqual(audit(ROOT), [])
        self.assertNotIn('the phrase', text)
        self.assertNotIn('a tool that', text)
        self.assertEqual(len(IMOVALIDATION), 50)
        self.assertEqual(len(NOIMOVALIDATION), 24)
        self.assertEqual(len(GENERIC_NAMES), 24)
        for value in ('imo-validation-claim-audit', 'documented-imo-validation-claim-false', 'documented-no-imo-validation-claim-false'):
            self.assertNotIn(value, text.split('```')[0])


if __name__ == '__main__':
    unittest.main()
