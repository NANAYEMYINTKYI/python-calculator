import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    # Test cases for add()
    def test_add_positive(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    def test_add_negative(self):
        self.assertEqual(self.calc.add(-1, -2), -3)

    # Test cases for subtract()
    def test_subtract_positive(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)  

    def test_subtract_negative(self):
        self.assertEqual(self.calc.subtract(-5, -3), -2)  

    # Test cases for multiply()
    def test_multiply_positive(self):
        self.assertEqual(self.calc.multiply(4, 3), 12)

    def test_multiply_negative(self):
        self.assertEqual(self.calc.multiply(4, -3), -12)

    # Test cases for divide()
    def test_divide_positive(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_divide_negative(self):
        self.assertEqual(self.calc.divide(-10, 2), -5)

    # Test cases for modulo()
    def test_modulo_positive(self):
        self.assertEqual(self.calc.modulo(7, 3), 1)  

    def test_modulo_exact_division(self):
        self.assertEqual(self.calc.modulo(9, 3), 0)  

if __name__ == '__main__':
    unittest.main()