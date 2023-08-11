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

     # Tests for: 2. Maths functions: sin, cos, square, sqrt.
     # Sin and Cos test cases are rounded to 3 decimal places to make equation checks.

    def test_sin(self):                     # Sin
        result = main("sin(30)")
        result = round(result, 3)           
        self.assertEqual(result, -0.988)   

    def test_cos(self):                     # Cos
        result = main("cos(30)")
        result = round(result, 3) 
        self.assertEqual(result, 0.154)   

    def test_square(self):                  # Square
        result = main("square(3)")
        self.assertEqual(result, 9)   

    def test_sqrt(self):                    # Sqrt
        result = main("sqrt(16)")
        self.assertEqual(result, 4)   

     # Tests for: 3. Let function to assign expressions to variables.

    def test_let_1(self):                   # Test for assigning a variable
        result = main("let(x = 3) (x)")         
        self.assertEqual(result, 3)  

    def test_let_2(self):                   # Test for addition with assigned variable
        result = main("let(x = 4) (x + 4)")         
        self.assertEqual(result, 8)   

    def test_let_3(self):                   # Test for multiplicatiton with assigned variable
        result = main("let(xyz = 5) (20 * xyz)")         
        self.assertEqual(result, 100)   

    def test_let_4(self):                   # Test for signed integer assignment
        result = main("let(number = -10) (number + 15)")         
        self.assertEqual(result, 5)

    def test_let_5(self):                   # Test for Func within assigned variable
        result = main("let(y = square(5)) (y)")         
        self.assertEqual(result, 25)

# In command line run: python src/test_main.py
if __name__ == '__main__':
    unittest.main()