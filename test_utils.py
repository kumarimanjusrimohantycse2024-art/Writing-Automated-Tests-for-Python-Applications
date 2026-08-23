import unittest
import utils

class TestMathFunctions(unittest.TestCase):

    def test_add_basic(self):
        self.assertEqual(utils.add(2, 3), 5)
        self.assertEqual(utils.add(-1, 1), 0)

    def test_subtract_basic(self):
        self.assertEqual(utils.subtract(5, 3), 2)
        self.assertEqual(utils.subtract(0, 5), -5)

    def test_multiply_basic(self):
        self.assertEqual(utils.multiply(4, 3), 12)
        self.assertEqual(utils.multiply(-2, 3), -6)

    def test_divide_basic(self):
        self.assertEqual(utils.divide(10, 2), 5)
        self.assertAlmostEqual(utils.divide(7, 2), 3.5)

    def test_divide_by_zero_raises(self):
        with self.assertRaises(ValueError):
            utils.divide(10, 0)

class TestStringFunctions(unittest.TestCase):

    def test_reverse_string_basic(self):
        self.assertEqual(utils.reverse_string("abc"), "cba")
        self.assertEqual(utils.reverse_string(""), "")

    def test_reverse_string_type_error(self):
        with self.assertRaises(TypeError):
            utils.reverse_string(123)

    def test_count_vowels_basic(self):
        self.assertEqual(utils.count_vowels("hello"), 2)   # e, o
        self.assertEqual(utils.count_vowels("HELLO"), 2)   # E, O
        self.assertEqual(utils.count_vowels("xyz"), 0)

    def test_count_vowels_type_error(self):
        with self.assertRaises(TypeError):
            utils.count_vowels(123)

class TestParseIntList(unittest.TestCase):

    def test_parse_int_list_basic(self):
        self.assertEqual(utils.parse_int_list("1,2,3"), [1, 2, 3])

    def test_parse_int_list_spaces(self):
        self.assertEqual(utils.parse_int_list(" 1 ,  2 ,3 "), [1, 2, 3])

    def test_parse_int_list_empty_items(self):
        self.assertEqual(utils.parse_int_list("1,,2,,,3"), [1, 2, 3])

    def test_parse_int_list_invalid_value(self):
        with self.assertRaises(ValueError):
            utils.parse_int_list("1, two, 3")

    def test_parse_int_list_type_error(self):
        with self.assertRaises(TypeError):
            utils.parse_int_list(123)

if __name__ == "__main__":
    unittest.main()