import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

        def test_addition(self):
            self.assertEqual(self.calc.add(1, 2), 3)
            self.assertEqual(self.calc.add(-1, 1), 0)
            self.assertEqual(self.calc.add(-1, -1), -2)
            self.assertEqual(self.calc.add(1.5, 2.5), 4.0)

        def test_subtraction(self):
            self.assertEqual(self.calc.subtract(2, 1), 1)
            self.assertEqual(self.calc.subtract(-1, 1), -2)
            self.assertEqual(self.calc.subtract(-1, -1), 0)
            self.assertEqual(self.calc.subtract(2.5, 1.5), 1.0)

        def test_multiplication(self):
            self.assertEqual(self.calc.multiply(2, 3), 6)
            self.assertEqual(self.calc.multiply(-1, 1), -1)
            self.assertEqual(self.calc.multiply(-1, -1), 1)
            self.assertEqual(self.calc.multiply(1.5, 2), 3.0)

        def test_division(self):
            self.assertEqual(self.calc.divide(6, 2), 3)
            self.assertEqual(self.calc.divide(-6, 2), -3)
            self.assertEqual(self.calc.divide(-6, -2), 3)
            self.assertEqual(self.calc.divide(3.0, 1.5), 2.0)

            with self.assertRaises(ValueError):
                self.calc.divide(1, 0)

    if __name__ == '__main__':
        unittest.main()