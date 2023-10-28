import unittest

class TestMathOperations(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(1 + 1, 2)

    def test_subtraction(self):
        self.assertEqual(3 - 1, 2)

    def test_multiplication(self):
        self.assertEqual(2 * 3, 6)

    def test_division(self):
        self.assertEqual(8 / 4, 2)

class TestStringOperations(unittest.TestCase):
    def test_string_concatenation(self):
        result = "Hello, " + "world!"
        self.assertEqual(result, "Hello, world!")

class TestListOperations(unittest.TestCase):
    def test_list_append(self):
        my_list = [1, 2, 3]
        my_list.append(4)
        self.assertEqual(len(my_list), 4)
        self.assertEqual(my_list[1], 2)

class TestDictOperations(unittest.TestCase):
    def test_dict_update(self):
        my_dict = {"key1": "value1", "key2": "value2"}
        my_dict["key3"] = "value3"
        self.assertEqual(len(my_dict), 3)
        self.assertEqual(my_dict["key2"], "value2")

if __name__ == "__main__":
    unittest.main()

