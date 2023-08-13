import math 
from ..LispVisitor import LispVisitor
from ..LispParser import LispParser

class EvalVisitor(LispVisitor):

    def __init__(self):
        self.variables = {}

    # Basic Arithmetic: Addition, Subtraction, Multiplication, Division
    def visitArithmetic(self, ctx):
        op = ctx.OP().getText()                             # Get the operator string ('+' or '-' or '*' or '/')
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


    def visitList(self, ctx):
        return [self.visit(expr) for expr in ctx.expr()]


    def visitFuncCall(self, ctx):
        func = ctx.FUNC().getText()         # String name of function (FUNC: 'sin' | 'cos' | 'square' | 'sqrt' | 'car' | 'cdr' | 'quote' | 'atom';)
        value = self.visit(ctx.expr())

        if func == 'sin':
            return math.sin(value)

        elif func == 'cos':
            return math.cos(value)

        elif func == 'square':
            return value * value

        elif func == 'sqrt':
            return math.sqrt(value)

        elif func == 'car':
            list_ = self.visit(ctx.expr())
            if isinstance(list_, list):
                return list_[0]
            else:
                raise Exception("Argument to 'car' must be a list.")

        elif func == 'cdr':
            list_ = self.visit(ctx.expr())
            if isinstance(list_, list):
                if len(list_) == 1:
                    return 'nil'
                else:
                    return list_[1:]
            else:
                raise Exception("Argument to 'cdr' must be a list.")

        elif func == 'quote':
            return ctx.expr().getText()

        elif func == 'atom':
            expr = self.visit(ctx.expr())
            if isinstance(expr, list):
                return 'f'
            else:
                return 't'


    def visitFuncEq(self, ctx):                 # (eq arg1 arg2) where arg1 and arg2 can be any expression
        arg1 = self.visit(ctx.expr(0))
        arg2 = self.visit(ctx.expr(1))
        if arg1 == arg2:                        # If both expressions are the same, return T aka True
            return 't'
        else:                                   # Else expressions are not the same, return F aka False
            return 'f'


    def visitFuncCond(self, ctx):                 
        clauses = ctx.cond_clause()
        for clause in clauses:
            condition = self.visit(clause.expr(0))
            action = self.visit(clause.expr(1))
            if condition != 'nil':
                return action
        return 'nil'


    def visitLet(self, ctx):
        bindings = ctx.var()
        for var in bindings:
            name = var.ID().getText()
            value =  self.visit(var.expr())
            self.variables[name] = value

        return self.visit(ctx.expr())

    def visitVar(self, ctx):
        var = ctx.ID().getText()
        value = self.visit(ctx.expr())
        return (var, value)

    def visitID(self, ctx):
        var = ctx.ID().getText()
        if var in self.variables:
            return self.variables[var]
        else:
            raise Exception(f"Variable '{var}' is not defined.")