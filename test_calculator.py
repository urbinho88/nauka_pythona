import unittest


from calculator import calculate

class TestCalculator(unittest.TestCase):
    def test_dodawanie(self):
        r = calculate(1, 2, '+')
        self.assertEqual(r, 3)

class TestCalculator(unittest.TestCase):
    def test_odejmowanie(self):
        r = calculate(3, 2, '-')
        self.assertEqual(r, 1)

class TestCalculator(unittest.TestCase):
    def test_mnozenie(self):
        r = calculate(1, 2, '*')
        self.assertEqual(r, 2)

class TestCalculator(unittest.TestCase):
    def test_dzielenie(self):
        r = calculate(6, 2, '/')
        self.assertEqual(r, 3)
