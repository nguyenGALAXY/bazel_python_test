import unittest

class TestMoreOperations(unittest.TestCase):
    def test_square(self):
        self.assertEqual(3 ** 2, 9)

    def test_string_length(self):
        self.assertEqual(len("Hello, world!"), 13)

if __name__ == "__main__":
    unittest.main()

