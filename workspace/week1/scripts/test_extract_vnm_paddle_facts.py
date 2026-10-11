"""Synthetic parser fixtures; these values are not company financial data."""
import unittest
from extract_vnm_paddle_facts import money, row


def entry(i,text,box):
    return {'id':i,'text':text,'bbox':box,'confidence':0.9}


class ParserFixtures(unittest.TestCase):
    def test_negative_vnd_and_grouping(self):
        self.assertEqual(money('(1.234,567)'),-1234567)
        self.assertEqual(money('-1.234.567'),-1234567)

    def test_blank_dash_ambiguity_and_real_zero(self):
        self.assertIsNone(money('-'))
        self.assertIsNone(money(''))
        self.assertIsNone(money('1.23.456'))
        self.assertEqual(money('0'),0)

    def test_current_column_on_right(self):
        entries=[entry(0,'20',[700,200,730,230]),entry(1,'1.234.567',[900,200,1080,230]),entry(2,'7.654.321',[1150,200,1320,230])]
        _,value,_,_=row(entries,'20',1250,1000)
        self.assertEqual(value['text'],'7.654.321')

    def test_merged_row_discloses_geometry(self):
        entries=[entry(0,'20',[700,200,730,230]),entry(1,'1.234.567 7.654.321',[900,200,1320,230])]
        _,value,_,_=row(entries,'20',1000,1250)
        self.assertEqual(value['text'],'1.234.567')
        self.assertEqual(value['bbox'],[900,200,1320,230])
        self.assertEqual(value['bbox_precision'],'whole_merged_row')
        self.assertEqual(value['parent_ocr_text'],'1.234.567 7.654.321')

    def test_one_numeric_column_is_ambiguous(self):
        entries=[entry(0,'20',[700,200,730,230]),entry(1,'1.234.567',[900,200,1080,230])]
        with self.assertRaises(ValueError):
            row(entries,'20',1000,1250)


if __name__=='__main__':
    unittest.main()
