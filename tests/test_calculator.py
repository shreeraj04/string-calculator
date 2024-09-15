import unittest
from calculator import StringCalculator

class TestStringCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = StringCalculator()
    
    def test_add_empty_string_returns_zero(self):
        result = self.calculator.add("")
        self.assertEqual(result, 0)

    def test_add_single_number_returns_the_number(self):
        result = self.calculator.add("5")
        self.assertEqual(result, 5)

    def test_add_two_numbers_returns_their_sum(self):
        result = self.calculator.add("1,2")
        self.assertEqual(result, 3)

    def test_sum_of_multiple_numbers(self):
        result = self.calculator.add("1,2,3,4,5")
        self.assertEqual(result, 15)

    def test_sum_of_large_number_of_values(self):
        result = self.calculator.add("10,20,30,40,50,60,70,80,90,100")
        self.assertEqual(result, 550)
    
    def test_sum_with_newlines(self):
        result = self.calculator.add("1\n2,3")
        self.assertEqual(result, 6)
        
    def test_sum_with_multiple_newlines(self):
        result = self.calculator.add("1\n2\n3,4")
        self.assertEqual(result, 10) 

    def test_custom_delimiter(self):
        result = self.calculator.add("//;\n1;2")
        self.assertEqual(result, 3)
    
    def test_custom_delimiter_with_multiple_numbers(self):
        result = self.calculator.add("//:\n1:2:3")
        self.assertEqual(result, 6)

    def test_negative_numbers_throw_exception(self):
        with self.assertRaises(ValueError) as context:
            self.calculator.add("1,-2,3")
        self.assertEqual(str(context.exception), "Negative numbers not allowed: -2")
    
    def test_multiple_negative_numbers_throw_exception(self):
        with self.assertRaises(ValueError) as context:
            self.calculator.add("1,-2,3,-5")
        self.assertEqual(str(context.exception), "Negative numbers not allowed: -2, -5")
        
if __name__ == "__main__":
    unittest.main()
