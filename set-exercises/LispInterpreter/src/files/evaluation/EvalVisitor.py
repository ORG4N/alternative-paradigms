import math 
from ..LispVisitor import LispVisitor
from ..LispParser import LispParser

class EvalVisitor(LispVisitor):

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