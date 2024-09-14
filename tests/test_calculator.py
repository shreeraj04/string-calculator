import unittest

class TestStringCalculator(unittest.TestCase):

    def test_add_empty_string_returns_zero(self):
        result = self.calculator.add("")
        self.assertEqual(result, 0)

    def test_add_single_number_returns_the_number(self):
        result = self.calculator.add("5")
        self.assertEqual(result, 5)

    def test_add_two_numbers_returns_their_sum(self):
        result = self.calculator.add("1,2")
        self.assertEqual(result, 3)

if __name__ == "__main__":
    unittest.main()
