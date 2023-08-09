# Generated from grammar/Lisp.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .LispParser import LispParser
else:
    from LispParser import LispParser

# This class defines a complete listener for a parse tree produced by LispParser.
class LispListener(ParseTreeListener):

    # Enter a parse tree produced by LispParser#parens.
    def enterParens(self, ctx:LispParser.ParensContext):
        pass

    # Exit a parse tree produced by LispParser#parens.
    def exitParens(self, ctx:LispParser.ParensContext):
        pass


    # Enter a parse tree produced by LispParser#MulDiv.
    def enterMulDiv(self, ctx:LispParser.MulDivContext):
        pass

    # Exit a parse tree produced by LispParser#MulDiv.
    def exitMulDiv(self, ctx:LispParser.MulDivContext):
        pass


    # Enter a parse tree produced by LispParser#AddSub.
    def enterAddSub(self, ctx:LispParser.AddSubContext):
        pass

    # Exit a parse tree produced by LispParser#AddSub.
    def exitAddSub(self, ctx:LispParser.AddSubContext):
        pass


    # Enter a parse tree produced by LispParser#int.
    def enterInt(self, ctx:LispParser.IntContext):
        pass

    # Exit a parse tree produced by LispParser#int.
    def exitInt(self, ctx:LispParser.IntContext):
        pass



del LispParser