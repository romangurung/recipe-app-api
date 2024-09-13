"""
Sample tests
"""

from django.test import SimpleTestCase # type: ignore

from app import calc

class CalcTests(SimpleTestCase):
    def test_add_numbers(self):
        result = calc.add(5, 6)
        self.assertEqual(result, 11)

    def test_subtract_numbers(self):
        result = calc.subtract(9, 6)
        self.assertEqual(result, 3)

