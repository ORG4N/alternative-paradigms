# Generated from grammar/Lisp.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .LispParser import LispParser
else:
    from LispParser import LispParser

# This class defines a complete listener for a parse tree produced by LispParser.
class LispListener(ParseTreeListener):

    # Enter a parse tree produced by LispParser#Arithmetic.
    def enterArithmetic(self, ctx:LispParser.ArithmeticContext):
        pass

    # Exit a parse tree produced by LispParser#Arithmetic.
    def exitArithmetic(self, ctx:LispParser.ArithmeticContext):
        pass


    # Enter a parse tree produced by LispParser#Int.
    def enterInt(self, ctx:LispParser.IntContext):
        pass

    # Exit a parse tree produced by LispParser#Int.
    def exitInt(self, ctx:LispParser.IntContext):
        pass


    # Enter a parse tree produced by LispParser#Parens.
    def enterParens(self, ctx:LispParser.ParensContext):
        pass

    # Exit a parse tree produced by LispParser#Parens.
    def exitParens(self, ctx:LispParser.ParensContext):
        pass


    # Enter a parse tree produced by LispParser#op.
    def enterOp(self, ctx:LispParser.OpContext):
        pass

    # Exit a parse tree produced by LispParser#op.
    def exitOp(self, ctx:LispParser.OpContext):
        pass



del LispParser