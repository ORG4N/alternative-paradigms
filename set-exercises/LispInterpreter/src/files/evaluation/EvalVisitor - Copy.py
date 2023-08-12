import math 
from ..LispVisitor import LispVisitor
from ..LispParser import LispParser

class EvalVisitor(LispVisitor):

    def __init__(self):
        self.variables = {}

    def visitInt(self, ctx):
        return int(ctx.INT().getText())

    def visitParens(self, ctx):
        return self.visit(ctx.expr())

    def visitMulDiv(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.type == LispParser.MUL:
            return left * right
        else:
            return left / right

    def visitAddSub(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.type == LispParser.ADD:
            return left + right
        else:
            return left - right

    def visitFuncCall(self, ctx):
        func = ctx.FUNC().getText()         # Either sin, cos, square, or sqrt
        value = self.visit(ctx.expr())

        if func == 'sin':
            return math.sin(value)

        elif func == 'cos':
            return math.cos(value)

        elif func == 'square':
            return value * value

        elif func == 'sqrt':
            return math.sqrt(value)

        elif func == 'quote':
            return value


    def visitLet(self, ctx):
        var_name = ctx.ID().getText()
        var_value = self.visit(ctx.expr(0))
        self.variables[var_name] = var_value
        return self.visit(ctx.expr(1))

    def visitID(self, ctx):
        var_name = ctx.getText()
        if var_name in self.variables:
            return self.variables[var_name]
        else:
            raise ValueError(f"Variable '{var_name}' is not defined.")
