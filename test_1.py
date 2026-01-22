import unittest
# Assuming the function is in a file named solution.py
from p1 import convert_case 

class TestConvertCase(unittest.TestCase):

    # 1. Upper to Lower
    def test_upper_to_lower(self):
        self.assertEqual(convert_case("A", "lower"), "a")
        self.assertEqual(convert_case("B", "Lower"), "b")
        self.assertEqual(convert_case("C", "LOWER"), "c")


    # 2. Lower to Upper
    def test_lower_to_upper(self):
        self.assertEqual(convert_case("a", "upper"), "A")
        self.assertEqual(convert_case("b", "Upper"), "B")
        self.assertEqual(convert_case("c", "UPPER"), "C")

    # 3. Upper to Upper (Should not change)
    def test_upper_to_upper(self):
        self.assertEqual(convert_case("A", "upper"), "A")
        self.assertEqual(convert_case("B", "Upper"), "B")
        self.assertEqual(convert_case("C", "UPPER"), "C")
    
    # 4. Lower to Lower (Should not change)
    def test_lower_to_lower(self):
        self.assertEqual(convert_case("a", "lower"), "a")
        self.assertEqual(convert_case("b", "Lower"), "b")
        self.assertEqual(convert_case("c", "LOWER"), "c")

    # 5. Non-Letter Character (Should not change)
    def test_non_letter(self):
        self.assertEqual(convert_case("!", "LOWER"), "!")

    # Bonus: Error Handling (Input is not a string)
    def test_invalid_input_type(self):
        with self.assertRaises(ValueError):
            self.assertEqual( convert_case(123, "upper"), "Input must be a string")

if __name__ == '__main__':
    unittest.main()