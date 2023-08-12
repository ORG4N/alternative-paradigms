# Generated from grammar/Lisp.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .LispParser import LispParser
else:
    from LispParser import LispParser

# This class defines a complete generic visitor for a parse tree produced by LispParser.

class LispVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LispParser#Arithmetic.
    def visitArithmetic(self, ctx:LispParser.ArithmeticContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LispParser#Int.
    def visitInt(self, ctx:LispParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LispParser#Parens.
    def visitParens(self, ctx:LispParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LispParser#op.
    def visitOp(self, ctx:LispParser.OpContext):
        return self.visitChildren(ctx)



del LispParser