"""Independent research calculation probe, not the production application.

No network calls or third-party project imports. Values must already have been
mapped and reviewed; this module deliberately does not parse PDFs or notices.
"""
from decimal import Decimal, ROUND_FLOOR
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'docs/research-dividend-functions/evidence'

def decimal(value):
    value = Decimal(str(value))
    if not value.is_finite():
        raise ValueError('non_finite')
    return value

def blocked(reason):
    return {'status': 'not_computable', 'reason': reason, 'value': None}

def coverage(facts, as_of):
    """CFO and two magnitudes, matching issuer/period/scope/unit and source."""
    names = ('cfo', 'capex', 'distribution')
    if any(facts.get(name) is None for name in names):
        return blocked('missing_operand')
    rows = [facts[name] for name in names]
    required = ('issuer', 'period', 'scope', 'unit', 'available_at', 'source', 'reviewed')
    if any(any(key not in row or row[key] is None for key in required) for row in rows):
        return blocked('metadata_missing')
    if any(not row['reviewed'] or not row['source'] for row in rows):
        return blocked('unreviewed_or_no_source')
    if any(row['available_at'] > as_of for row in rows):
        return blocked('future_information')
    for key in ('issuer', 'period', 'scope', 'unit'):
        if len({row[key] for row in rows}) != 1:
            return blocked('incompatible_' + key)
    if rows[0]['unit'] != 'VND':
        return blocked('unit_not_normalized')
    if facts['distribution'].get('kind') not in ('cash_dividends_paid', 'owner_distribution_grouped'):
        return blocked('distribution_definition_unresolved')
    try:
        cfo, capex, dist = (decimal(row['value']) for row in rows)
    except (KeyError, ValueError, ArithmeticError):
        return blocked('invalid_number')
    if capex < 0 or dist < 0:
        return blocked('outflow_magnitude_negative')
    total = capex + dist
    return {'status': 'computed', 'formula_version': 'probe-1', 'distribution_kind': facts['distribution']['kind'],
            'cash_after_capex': str(cfo-capex), 'cash_after_distribution': str(cfo-total),
            'coverage': {'status': 'computed', 'value': str(cfo/total)} if total > 0 else
                        {'status': 'not_applicable', 'value': None, 'reason': 'zero_denominator'},
            'sources': [row['source'] for row in rows]}

def reference_dps(raw_dps, events, source_basis, target_basis, as_of, complete=True):
    """Events are the reviewed interval between the specified bases.

    Interval membership is supplied, not inferred from record dates here.
    Only forward conversion of raw pre-event DPS to a later basis is probed.
    """
    if not complete:
        return blocked('partial_annual_coverage')
    if source_basis != 'raw' or target_basis != 'later_reference':
        return blocked('unsupported_or_already_adjusted_basis')
    factor = Decimal(1)
    for event in events:
        if event.get('published_at', '9999') > as_of:
            return blocked('future_information')
        if event.get('status') == 'canceled':
            continue
        if event.get('status') != 'effective' or not event.get('basis_confirmed') or not event.get('source'):
            return blocked('unresolved_event')
        if event.get('kind') not in ('free_share_issue', 'split', 'reverse_split'):
            return blocked('unsupported_event')
        try:
            f = decimal(event['factor'])
        except (KeyError, ValueError, ArithmeticError):
            return blocked('invalid_factor')
        if f <= 0:
            return blocked('invalid_factor')
        factor *= f
    try:
        raw = decimal(raw_dps)
    except (ValueError, ArithmeticError):
        return blocked('invalid_dps')
    if raw < 0:
        return blocked('negative_dps')
    return {'status': 'computed', 'raw_dps': str(raw), 'factor': str(factor),
            'reference_dps': str(raw/factor), 'sources': [e['source'] for e in events if e.get('status') != 'canceled'],
            'assumption': 'confirmed interval; theoretical shares; no account rounding'}

def free_share_entitlement(shares, numerator, denominator):
    shares, numerator, denominator = map(decimal, (shares, numerator, denominator))
    if shares < 0 or shares != shares.to_integral_value() or numerator < 0 or denominator <= 0:
        raise ValueError('invalid_entitlement_inputs')
    return int((shares*numerator/denominator).to_integral_value(rounding=ROUND_FLOOR))

OPS = {'>=': lambda a,b:a>=b, '<=':lambda a,b:a<=b, '>':lambda a,b:a>b,
       '<':lambda a,b:a<b, '==':lambda a,b:a==b}

def screen(metrics, conditions):
    if not conditions:
        raise ValueError('empty_conditions')
    results = []
    for condition in conditions:
        operator = condition['operator']
        if operator not in OPS:
            raise ValueError('unsupported_operator')
        threshold = decimal(condition['threshold'])
        metric = metrics.get(condition['metric'])
        row = {'metric': condition['metric'], 'operator': operator, 'threshold': str(threshold)}
        if metric is None or metric.get('status') != 'computed' or not metric.get('sources'):
            row.update(status='unknown', reason='missing_or_ineligible_metric')
        elif metric.get('unit') != condition['unit']:
            row.update(status='unknown', reason='incompatible_unit')
        else:
            try:
                value = decimal(metric['value'])
                row.update(status='pass' if OPS[operator](value, threshold) else 'fail',
                           value=str(value), sources=metric['sources'])
            except (ValueError, ArithmeticError):
                row.update(status='unknown', reason='invalid_metric_value')
        results.append(row)
    states = {row['status'] for row in results}
    result = 'fail' if 'fail' in states else 'unknown' if 'unknown' in states else 'pass'
    return {'status': result, 'conditions': results, 'contains_unknown': 'unknown' in states}

def run():
    cases = json.loads((OUT/'real-cases.json').read_text(encoding='utf-8'))
    result = {'method': 'independent arithmetic/rule probe; no production integration or user acceptance',
              'dhg': {year: coverage(facts, '2026-10-11') for year, facts in cases['dhg']['facts'].items()},
              'fpt_rounding': {'eligible_shares': 21, 'additional_shares': free_share_entitlement(21,3,20),
                              'source': 'https://vsdc.vn/vi/ad1/184974',
                              'assumption': 'eligibility at free-share event only; no later cash entitlement inferred'}}
    metric = {'residual': {'status': 'computed', 'value': result['dhg']['2025']['cash_after_distribution'],
                          'unit': 'VND', 'sources': result['dhg']['2025']['sources']}}
    conditions = [{'metric':'residual','operator':'>=','threshold':0,'unit':'VND'},
                  {'metric':'annual_dps_growth','operator':'>=','threshold':0,'unit':'ratio'}]
    result['dhg_screen_example'] = screen(metric, conditions)
    (OUT/'probe-results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(result,ensure_ascii=True,indent=2))

if __name__ == '__main__':
    run()
