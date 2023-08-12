import unittest
from main import main

class TestMain(unittest.TestCase):

    # Basic tests.

    def test_int(self):                     # Test if an integer will evaluate to itself.
        result = main("(55)")
        self.assertEqual(result, 55)

    def test_signed_int(self):              # Test if a negative integer will be returned as a negative integer.
        result = main("(-200)")
        self.assertEqual(result, -200)


    # Tests for: 1. Basic arithmetic: add, sub, mul, div for integer numbers.
    
    def test_add_1(self):                     # Addition.
        result = main("(+ 10 10)")
        self.assertEqual(result, 20)
        
    def test_add_2(self):                     # Addition with multiple values.
        result = main("(+ 10 10 10 10)")
        self.assertEqual(result, 40)    

    def test_sub_1(self):                     # Subtraction.
        result = main("(- 5 3)")
        self.assertEqual(result, 2)

    def test_sub_2(self):                     # Subtraction with multiple values.
        result = main("(- 10 2 1)")
        self.assertEqual(result, 7)

    def test_mul_1(self):                     # Multiplication.
        result = main("(* 10 5)")
        self.assertEqual(result, 50)

    def test_mul_2(self):                     # Multiplication with multiple values.
        result = main("(* 5 5 10 )")
        self.assertEqual(result, 250)

    def test_div_1(self):                     # Division.
        result = main("(/ 48  12)")
        self.assertEqual(result, 4)

    def test_div_2(self):                     # Division with multiple values.
        result = main("(/ 100  10 5)")
        self.assertEqual(result, 2)

    # Tests for: 2. Maths functions: sin, cos, square, sqrt.
    # Sin and Cos test cases are rounded to 3 decimal places to make equation checks.
     
    def test_sin(self):                     # Sin
        result = main("(sin 30)")
        result = round(result, 3)           
        self.assertEqual(result, -0.988)   

    def test_cos(self):                     # Cos
        result = main("(cos 30)")
        result = round(result, 3) 
        self.assertEqual(result, 0.154)   

    def test_square(self):                  # Square
        result = main("(square 3)")
        self.assertEqual(result, 9)   

    def test_sqrt(self):                    # Sqrt
        result = main("(sqrt 16)")
        self.assertEqual(result, 4)   

    # Tests for: 3. Let function to assign expressions to variables.

    def test_let_1(self):                   # Test for assigning a variable
        result = main("(let((x 3)) (x))")         
        self.assertEqual(result, 3)  

    def test_let_2(self):                   # Test for addition with assigned variable
        result = main("(let((x 4)) (+ x 10))")         
        self.assertEqual(result, 14)   

    def test_let_3(self):                   # Test for multiplicatiton with assigned variable
        result = main("(let((xyz 5)) (* 20 xyz))")         
        self.assertEqual(result, 100)   

    def test_let_4(self):                   # Test for signed integer assignment
        result = main("(let((number -10)) (number))")         
        self.assertEqual(result, -10)

    def test_let_5(self):                   # Test for Func within assigned variable
        result = main("(let((y (square 5))) (y))")         
        self.assertEqual(result, 25)

    def test_let_6(self):                   # Test for assinging multiple variables
        result = main("(let((x 10) (y 20)) (+ x y))")         
        self.assertEqual(result, 30)

    def test_let_7(self):                   # Assign the result of a calculation using two variables to its own variable and use that in a calculation
        result = main("(let((x 10) (y 20)) (let((result (+ x y))) (+ result 5)))")         
        self.assertEqual(result, 35)

# In command line run: python src/test_main.py
if __name__ == '__main__':
    unittest.main()