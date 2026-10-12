"""Synthetic layout tests: no company values or report-specific page coordinates."""
import unittest
from financial_pipeline.extraction.parser import amount, classify, columns, extract_row, unit, document_context


def entry(i, text, bbox):
    return {'id': str(i), 'text': text, 'bbox': bbox, 'confidence': .9, 'crop_sha256': 'synthetic-fixture'}


def page(code_first=False, scale=1, current_right=False):
    entries = [entry(0, 'Bảng cân đối kế toán hợp nhất', [50, 20, 600, 50]),
               entry(1, 'Số cuối năm', [680 if not current_right else 910, 100, 790 if not current_right else 990, 130]),
               entry(2, 'Số đầu năm', [910 if not current_right else 680, 100, 990 if not current_right else 790, 130]),
               entry(3, 'Đơn vị tính: VND', [600, 150, 850, 180]),
               entry(4, 'Tiền và các khoản tương đương tiền', [140 if code_first else 50, 250, 540, 280]),
               entry(5, '110', [50, 250, 100, 280] if code_first else [560, 250, 600, 280]),
               entry(6, '1.000.000', [670, 250, 810, 280]), entry(7, '2.000.000', [900, 250, 1020, 280])]
    for e in entries:
        e['bbox'] = [v*scale for v in e['bbox']]
    return {'entries': entries, 'image_width': 1100*scale, 'image_height': 1400*scale}


class ContentParserTests(unittest.TestCase):
    def test_merged_row_code_and_wrapped_business_label(self):
        p = page()
        p['entries'] = [e for e in p['entries'] if e['id'] != '5']
        p['entries'][4]['text'] += ' 110'
        selected, _, _ = extract_row(p, '110', ['Tiền và các khoản tương đương tiền'], columns(p, 'balance_sheet', 2025))
        self.assertEqual(selected['text'], '1.000.000')
        p = page()
        p['entries'][4]['text'] = 'Lưu chuyển tiền thuần từ hoạt động kinh'
        p['entries'][5]['text'] = '20'
        p['entries'].append(entry(11, 'doanh', [50, 282, 130, 308]))
        selected, _, _ = extract_row(p, '20', ['Lưu chuyển tiền thuần từ hoạt động kinh doanh'], columns(p, 'balance_sheet', 2025))
        self.assertEqual(selected['text'], '1.000.000')

    def test_document_year_requires_annual_phrase_not_any_year(self):
        source = {'expected_legal_name': 'Công ty kiểm thử', 'fiscal_year': 2025}
        def context(year):
            text = f'Công ty kiểm thử hợp nhất Báo cáo kiểm toán độc lập cho năm kết thúc ngày 31 tháng 12 năm {year}. Năm tài chính bắt đầu ngày 01 tháng 01 và kết thúc ngày 31 tháng 12. So sánh 2025.'
            return document_context([{'entries': [entry(0, text, [0, 0, 100, 20])]}], source)
        self.assertTrue(context(2025)['verified'])
        self.assertFalse(context(2024)['checks']['annual'])

    def test_row_code_on_either_side_and_different_image_sizes(self):
        for first in [False, True]:
            for scale in [.7, 1, 2.2]:
                p = page(first, scale)
                self.assertEqual(classify(p), 'balance_sheet')
                self.assertEqual(unit(p)[0], 'VND')
                c = columns(p, classify(p), 2025)
                selected, _, _ = extract_row(p, '110', ['Tiền và tương đương tiền', 'Tiền và các khoản tương đương tiền'], c)
                self.assertEqual(selected['text'], '1.000.000')

    def test_current_column_may_be_on_right(self):
        p = page(current_right=True)
        c = columns(p, 'balance_sheet', 2025)
        selected, _, _ = extract_row(p, '110', ['Tiền và các khoản tương đương tiền'], c)
        self.assertEqual(selected['text'], '2.000.000')

    def test_notes_are_not_primary_statement(self):
        p = page()
        p['entries'].insert(0, entry(10, 'Thuyết minh báo cáo tài chính hợp nhất', [30, 0, 650, 20]))
        self.assertIsNone(classify(p))
        p['entries'][0]['text'] = 'Thuyết minh báo cáo tài ch tính hợp nhất'
        self.assertIsNone(classify(p))
        p['entries'] = [entry(0, 'Thông tin bổ sung cho Báo cáo lưu chuyển tiền tệ', [20, 10, 800, 40])]
        self.assertIsNone(classify(p))

    def test_missing_unit_header_and_value_are_not_zero(self):
        p = page()
        p['entries'] = [e for e in p['entries'] if e['id'] != '3']
        self.assertIsNone(unit(p)[0])
        p['entries'] = [e for e in p['entries'] if e['id'] != '1']
        with self.assertRaises(ValueError):
            columns(p, 'balance_sheet', 2025)
        self.assertIsNone(amount('—'))
        self.assertIsNone(amount('(-250)'))
        self.assertEqual(amount('(250)'), -250)
        self.assertEqual(amount('12345'), 12345)


if __name__ == '__main__':
    unittest.main()
