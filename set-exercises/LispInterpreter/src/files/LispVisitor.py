# Generated from grammar/Lisp.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .LispParser import LispParser
else:
    from LispParser import LispParser

# This class defines a complete generic visitor for a parse tree produced by LispParser.

class LispVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LispParser#parens.
    def visitParens(self, ctx:LispParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LispParser#MulDiv.
    def visitMulDiv(self, ctx:LispParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LispParser#AddSub.
    def visitAddSub(self, ctx:LispParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LispParser#int.
    def visitInt(self, ctx:LispParser.IntContext):
        return self.visitChildren(ctx)



del LispParser