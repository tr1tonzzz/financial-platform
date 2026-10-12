"""Unit variants, unsafe fallbacks and monetary conversion through the parser."""
import pytest
from financial_pipeline.extraction.normalization import monetary_unit, UNIT_MULTIPLIERS
from financial_pipeline.extraction.parser import unit, parse_report
from test_parser import entry, page


@pytest.mark.parametrize('label,canonical,factor', [
    ('Đơn vị tính: tỷ đồng', 'tỷ đồng', 1000000000),
    ('ĐVT: tỉ đồng', 'tỷ đồng', 1000000000),
    ('Đơn vị: TỶ VNĐ', 'tỷ đồng', 1000000000),
    ('nghìn VND', 'nghìn đồng', 1000),
    ('Đơn vị tính: ngàn đồng Việt Nam', 'nghìn đồng', 1000),
    ('Đơn vị tính: 1.000 VND', 'nghìn đồng', 1000),
    ('triệu VND', 'triệu đồng', 1000000),
    ('Đơn vị tính: triệu VNĐ', 'triệu đồng', 1000000),
    ('Đơn vị tiền tệ: VND', 'VND', 1),
    ('Đơn vị tính: đồng', 'VND', 1),
    ('Unit: VND million', 'triệu đồng', 1000000),
    ('Units: billion VND', 'tỷ đồng', 1000000000),
])
def test_variants_are_converted_with_exact_scale(label, canonical, factor):
    assert monetary_unit(label) == canonical
    p = page()
    p['entries'][3]['text'] = label
    assert unit(p)[0] == canonical and UNIT_MULTIPLIERS[canonical] == factor
    cover = {'entries': [entry(99, 'Công ty kiểm thử hợp nhất Báo cáo kiểm toán độc lập cho năm kết thúc ngày 31 tháng 12 năm 2025. Năm tài chính bắt đầu ngày 01 tháng 01 và kết thúc ngày 31 tháng 12.', [0, 0, 900, 50])], 'image_height': 1400, 'image_width': 1100}
    p.update(pdf_page_index=1, recognizer_model_sha256='fixture', config_sha256='fixture')
    rows, _ = parse_report([cover, p], {'ticker': 'FIX', 'fiscal_year': 2025, 'expected_legal_name': 'Công ty kiểm thử'})
    cash = next(row for row in rows if row['metric_code'] == 'cash_equivalents')
    assert cash['value_vnd'] == str(1000000*factor)
    assert cash['evidence']['unit_multiplier'] == factor


@pytest.mark.parametrize('label', ['Đơn vị tính: trăm đồng', 'Đơn vị: nghìn USD', 'Đơn vị: tỷ EUR',
                                   'Đơn vị tính: nghìn triệu VND', 'Đơn vị: đồng/cổ phiếu', 'Đơn vị: VND và USD'])
def test_unknown_declared_units_never_fall_back_to_vnd(label):
    with pytest.raises(ValueError):
        monetary_unit(label)
    p = page()
    p['entries'][3]['text'] = label
    p['entries'].append(entry(15, 'VND', [800, 180, 900, 200]))
    assert unit(p) == (None, [])


def test_conflicting_or_split_scales_are_not_unscaled_vnd():
    p = page()
    p['entries'].append(entry(20, 'triệu VND', [100, 60, 300, 80]))
    assert unit(p) == (None, [])
    p['entries'][-1]['text'] = 'nghìn'
    assert unit(p) == (None, [])
