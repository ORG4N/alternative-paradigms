import unittest
from main import main

class TestMain(unittest.TestCase):

    # Tests for: 1. Basic arithmetic: add, sub, mul, div for integer numbers.
    
    def test_add(self):                     # Addition
        result = main("10 + 10")
        self.assertEqual(result, 20)    

    def test_sub(self):                     # Subtraction
        result = main("5 - 3")
        self.assertEqual(result, 2)

    def test_mul(self):                     # Multiplication
        result = main("10 * 5")
        self.assertEqual(result, 50)

    def test_div(self):                     # Division
        result = main("48 / 12")
        self.assertEqual(result, 4)

# In command line run: python src/test_main.py
if __name__ == '__main__':
    unittest.main()