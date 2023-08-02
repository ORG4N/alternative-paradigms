# Generated from grammar/Lisp.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .LispParser import LispParser
else:
    from LispParser import LispParser

# This class defines a complete listener for a parse tree produced by LispParser.
class LispListener(ParseTreeListener):

    # Enter a parse tree produced by LispParser#expr.
    def enterExpr(self, ctx:LispParser.ExprContext):
        pass

    # Exit a parse tree produced by LispParser#expr.
    def exitExpr(self, ctx:LispParser.ExprContext):
        pass


    # Enter a parse tree produced by LispParser#op.
    def enterOp(self, ctx:LispParser.OpContext):
        pass

    # Exit a parse tree produced by LispParser#op.
    def exitOp(self, ctx:LispParser.OpContext):
        pass



del LispParser