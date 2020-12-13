import unittest
from str_calculator import str_calculator


class TestStringCalculator(unittest.TestCase):
    def test_concat(self):
        r = str_calculator("a", "b", 'concat')
        self.assertEqual(r, 'ab')

    def test_concat(self):
        r = str_calculator("d", "rze", "wo", 'concat')
        self.assertEqual(r, 'trzewo')

    def test_concat(self):
        r = str_calculator("ka", "j", "ak", 'concat')
        self.assertEqual(r, 'kajak')
