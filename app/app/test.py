"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    def test_add_numbers(self):
        """
        test adding numbers together
        """
        results = calc.add(5, 6)

        self.assertEqual(results, 11)

    def test_subtract_numbers(self):
        """
        Test subtracting numbers
        """
        results = calc.subtract(10, 15)

        self.assertEqual(results, 5)
