import unittest
# Assuming the function is in a file named solution.py
from p1 import convert_case 

class TestConvertCase(unittest.TestCase):

    # 1. Upper to Lower
    def test_upper_to_lower(self):
        pass


    # 2. Lower to Upper
    def test_lower_to_upper(self):
        pass

    # 3. Upper to Upper (Should not change)
    def test_upper_to_upper(self):
        pass
    
    # 4. Lower to Lower (Should not change)
    def test_lower_to_lower(self):
        pass

    # 5. Non-Letter Character (Should not change)
    def test_non_letter(self):
        pass

    # Bonus: Error Handling (Input is not a string)
    def test_invalid_input_type(self):
        with self.assertRaises(ValueError):
            convert_case(123, "upper")

if __name__ == '__main__':
    unittest.main()