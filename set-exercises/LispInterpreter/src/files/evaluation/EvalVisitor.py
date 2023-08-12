import math 
from ..LispVisitor import LispVisitor
from ..LispParser import LispParser

class EvalVisitor(LispVisitor):


    # Basic Arithmetic: Addition, Subtraction, Multiplication, Division
    def visitArithmetic(self, ctx):
        op = ctx.op().getText()                             # Get the operator string ('+' or '-' or '*' or '/')
        args = [self.visit(expr) for expr in ctx.expr()]    # Get the values within the expression

        if op == '+':                                       # Addition:
            return sum(args)                                # Sum all values within expression.

        elif op == '-':                                     # Subtraction:
            return args[0] - sum(args[1:])                  # Subtract all values within expression from eachother by subtracting first value in list from the sum of all other values.
                                                            # (- a b c d e) == (- a (+ b c d e))

        elif op == '*':                                     # Multiplication:
            result = args[0]                                # Multiplicate all values with eachother by storing first value in a temp variable and multiplying the contents of this variable by
            for arg in args[1:]:                            # each other value within the expression, one at a time.
                result *= arg
            return result                                   

        elif op == '/':                                     # Division
            result = args[0]                                # Similar to multiplication. Store first value of expression in result variable and divide the contents of this variable
            for arg in args[1:]:                            # by all other values within the expression. Final result is achieved when all values have been divided by eachother.
                result /= arg                               # (/ a b c d e) == (/ a (* b c d e))
            return result


    def visitInt(self, ctx):
        return int(ctx.INT().getText())


    def visitParens(self, ctx):
        return self.visit(ctx.expr())