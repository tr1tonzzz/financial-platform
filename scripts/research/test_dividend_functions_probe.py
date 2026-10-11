"""Domain edge cases for the independent probe, not production acceptance."""
import copy
import unittest
import json
import platform
from pathlib import Path
from decimal import Decimal
from dividend_functions_probe import coverage, reference_dps, free_share_entitlement, screen

def facts(cfo=120,capex=80,distribution=60):
    result={name: {'value':str(value),'issuer':'A','period':'2025','scope':'entity','unit':'VND',
                  'available_at':'2026-03-01','source':'source-'+name,'reviewed':True}
            for name,value in zip(('cfo','capex','distribution'),(cfo,capex,distribution))}
    result['distribution']['kind']='owner_distribution_grouped'
    return result

def event(factor='1.2', **changes):
    result={'factor':factor,'kind':'free_share_issue','published_at':'2025-07-01',
            'basis_confirmed':True,'status':'effective','source':'notice'}
    result.update(changes)
    return result

class CoverageTests(unittest.TestCase):
    def test_residual_and_fraction(self):
        r=coverage(facts(),'2026-10-11')
        self.assertEqual(r['cash_after_distribution'],'-20')
        self.assertEqual(Decimal(r['coverage']['value']),Decimal(120)/140)
    def test_missing_is_not_zero(self):
        f=facts(); f['capex']=None
        self.assertEqual(coverage(f,'2026-10-11')['reason'],'missing_operand')
    def test_scope_period_unit_issuer(self):
        for key,value in [('scope','consolidated'),('period','2024'),('unit','million_VND'),('issuer','B')]:
            with self.subTest(key=key):
                f=facts();f['capex'][key]=value
                self.assertEqual(coverage(f,'2026-10-11')['reason'],'incompatible_'+key)
    def test_zero_denominator_keeps_residual(self):
        r=coverage(facts(10,0,0),'2026-10-11')
        self.assertEqual(r['cash_after_distribution'],'10');self.assertIsNone(r['coverage']['value'])
    def test_negative_cfo_preserves_sign(self):
        self.assertEqual(coverage(facts(-10,5,5),'2026-10-11')['coverage']['value'],'-1')
    def test_outflow_sign_not_abs(self):
        self.assertEqual(coverage(facts(10,-5,5),'2026-10-11')['reason'],'outflow_magnitude_negative')
    def test_source_review_asof(self):
        for key,value,reason in [('reviewed',False,'unreviewed_or_no_source'),('source','','unreviewed_or_no_source'),
                                 ('available_at','2027-01-01','future_information')]:
            with self.subTest(key=key):
                f=facts();f['cfo'][key]=value
                self.assertEqual(coverage(f,'2026-10-11')['reason'],reason)
    def test_notice_dps_rejected(self):
        f=facts();f['distribution']['kind']='announced_dps'
        self.assertEqual(coverage(f,'2026-10-11')['reason'],'distribution_definition_unresolved')

class BasisTests(unittest.TestCase):
    def calculate(self,events,**changes):
        args={'source_basis':'raw','target_basis':'later_reference','as_of':'2026-10-11','complete':True}
        args.update(changes)
        return reference_dps(1000,events,**args)
    def test_identity_and_chain(self):
        self.assertEqual(self.calculate([])['reference_dps'],'1000')
        self.assertEqual(Decimal(self.calculate([event('1.2'),event('1.25')])['reference_dps']),Decimal(1000)/Decimal('1.50'))
    def test_reverse_split(self):
        self.assertEqual(self.calculate([event('0.5',kind='reverse_split')])['reference_dps'],'2.00E+3')
    def test_canceled_does_not_adjust(self):
        self.assertEqual(self.calculate([event(status='canceled')])['factor'],'1')
    def test_unresolved_and_unsupported(self):
        self.assertEqual(self.calculate([event(basis_confirmed=False)])['reason'],'unresolved_event')
        self.assertEqual(self.calculate([event(kind='paid_rights_issue')])['reason'],'unsupported_event')
    def test_no_double_adjustment(self):
        self.assertEqual(self.calculate([],source_basis='vendor_adjusted')['status'],'not_computable')
    def test_partial_or_future_blocked(self):
        self.assertEqual(self.calculate([],complete=False)['reason'],'partial_annual_coverage')
        self.assertEqual(self.calculate([event(published_at='2027-01-01')])['reason'],'future_information')
    def test_invalid_factor(self):
        for value in ('0','-1','NaN'):
            with self.subTest(value=value):self.assertEqual(self.calculate([event(value)])['reason'],'invalid_factor')
    def test_fpt_account_rounding(self):
        self.assertEqual(free_share_entitlement(21,3,20),3)
        self.assertEqual(free_share_entitlement(100,3,20),15)

class ScreenTests(unittest.TestCase):
    def setUp(self):
        self.condition={'metric':'x','operator':'>=','threshold':'1','unit':'ratio'}
        self.metric={'status':'computed','value':'1.2','unit':'ratio','sources':['source']}
    def test_pass_fail_unknown_truth_table(self):
        for value,status in [('1.2','pass'),('0.9','fail'),(None,'unknown')]:
            with self.subTest(value=value):
                m=copy.deepcopy(self.metric);m['value']=value
                self.assertEqual(screen({'x':m},[self.condition])['status'],status)
    def test_failed_and_unknown_kept(self):
        m=copy.deepcopy(self.metric);m['value']='0'
        other={**self.condition,'metric':'y'}
        r=screen({'x':m},[self.condition,other])
        self.assertEqual(r['status'],'fail');self.assertTrue(r['contains_unknown'])
    def test_partial_no_source_wrong_unit(self):
        for changes in ({'status':'partial'},{'sources':[]},{'unit':'VND'}):
            with self.subTest(changes=changes):
                self.assertEqual(screen({'x':{**self.metric,**changes}},[self.condition])['status'],'unknown')
    def test_invalid_operator_and_empty(self):
        with self.assertRaises(ValueError):screen({},[{**self.condition,'operator':'exec'}])
        with self.assertRaises(ValueError):screen({},[])

if __name__=='__main__':
    suite=unittest.defaultTestLoader.loadTestsFromModule(__import__(__name__))
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    report={'scope':'independent calculation/rule prototype; not application acceptance',
            'executed_on':'2026-10-11','python':platform.python_version(),'tests_run':result.testsRun,
            'failures':len(result.failures),'errors':len(result.errors),'status':'passed' if result.wasSuccessful() else 'failed'}
    path=Path(__file__).resolve().parents[2]/'docs/research-dividend-functions/evidence/probe-test-results.json'
    path.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    raise SystemExit(0 if result.wasSuccessful() else 1)
