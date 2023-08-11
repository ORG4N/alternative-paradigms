# Generated from grammar/Lisp.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .LispParser import LispParser
else:
    from LispParser import LispParser

# This class defines a complete listener for a parse tree produced by LispParser.
class LispListener(ParseTreeListener):

    # Enter a parse tree produced by LispParser#FuncCall.
    def enterFuncCall(self, ctx:LispParser.FuncCallContext):
        pass

    # Exit a parse tree produced by LispParser#FuncCall.
    def exitFuncCall(self, ctx:LispParser.FuncCallContext):
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


    # Enter a parse tree produced by LispParser#Parens.
    def enterParens(self, ctx:LispParser.ParensContext):
        pass

    # Exit a parse tree produced by LispParser#Parens.
    def exitParens(self, ctx:LispParser.ParensContext):
        pass


    # Enter a parse tree produced by LispParser#Let.
    def enterLet(self, ctx:LispParser.LetContext):
        pass

    # Exit a parse tree produced by LispParser#Let.
    def exitLet(self, ctx:LispParser.LetContext):
        pass


    # Enter a parse tree produced by LispParser#ID.
    def enterID(self, ctx:LispParser.IDContext):
        pass

    # Exit a parse tree produced by LispParser#ID.
    def exitID(self, ctx:LispParser.IDContext):
        pass


    # Enter a parse tree produced by LispParser#Int.
    def enterInt(self, ctx:LispParser.IntContext):
        pass

    # Exit a parse tree produced by LispParser#Int.
    def exitInt(self, ctx:LispParser.IntContext):
        pass



del LispParser