import unittest

class TestMathOperationsFailed(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(2 + 3, 4)

    def test_subtraction(self):
        self.assertEqual(7 - 4, 2)

if __name__ == "__main__":
    unittest.main()

