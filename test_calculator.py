import unittest
import calculator

class TestClass(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(2, 4), 6)

    def test_sub(self):
        self.assertEqual(calculator.sub(2, 4), -2)

    def test_mul(self):
        self.assertEqual(calculator.mul(2, 4), 8)

    def test_div(self):
        self.assertEqual(calculator.div(2, 4), 0.5)

if __name__ == "__main__":
    unittest.main()
