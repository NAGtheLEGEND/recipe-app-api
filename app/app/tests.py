from django.test import SimpleTestCase
from app import calc
class CalcTests(SimpleTestCase):
    def test_add_numbers(self):
        res = calc.add(5,6)
        self.assertEqual(res,11)

    def test_sub_nums(self):
        res = calc.subs(19,10)
        self.assertEqual(res,9)