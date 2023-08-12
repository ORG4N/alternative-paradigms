# Generated from grammar/Lisp.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,12,44,2,0,7,0,2,1,7,1,1,0,1,0,1,0,4,0,8,8,0,11,0,12,0,9,1,0,
        1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,
        4,0,29,8,0,11,0,12,0,30,1,0,1,0,1,0,1,0,3,0,37,8,0,1,1,1,1,1,1,1,
        1,1,1,1,1,0,0,2,0,2,0,0,48,0,36,1,0,0,0,2,38,1,0,0,0,4,5,5,1,0,0,
        5,7,5,3,0,0,6,8,3,0,0,0,7,6,1,0,0,0,8,9,1,0,0,0,9,7,1,0,0,0,9,10,
        1,0,0,0,10,11,1,0,0,0,11,12,5,2,0,0,12,37,1,0,0,0,13,37,5,11,0,0,
        14,37,5,10,0,0,15,16,5,1,0,0,16,17,3,0,0,0,17,18,5,2,0,0,18,37,1,
        0,0,0,19,20,5,1,0,0,20,21,5,4,0,0,21,22,3,0,0,0,22,23,5,2,0,0,23,
        37,1,0,0,0,24,25,5,1,0,0,25,26,5,5,0,0,26,28,5,1,0,0,27,29,3,2,1,
        0,28,27,1,0,0,0,29,30,1,0,0,0,30,28,1,0,0,0,30,31,1,0,0,0,31,32,
        1,0,0,0,32,33,5,2,0,0,33,34,3,0,0,0,34,35,5,2,0,0,35,37,1,0,0,0,
        36,4,1,0,0,0,36,13,1,0,0,0,36,14,1,0,0,0,36,15,1,0,0,0,36,19,1,0,
        0,0,36,24,1,0,0,0,37,1,1,0,0,0,38,39,5,1,0,0,39,40,5,10,0,0,40,41,
        3,0,0,0,41,42,5,2,0,0,42,3,1,0,0,0,3,9,30,36
    ]

class LispParser ( Parser ):

    grammarFileName = "Lisp.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "<INVALID>", "<INVALID>", 
                     "'let'", "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "OP", "FUNC", 
                      "LET", "ADD", "SUB", "MUL", "DIV", "ID", "INT", "WS" ]

    RULE_expr = 0
    RULE_var = 1

    ruleNames =  [ "expr", "var" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    OP=3
    FUNC=4
    LET=5
    ADD=6
    SUB=7
    MUL=8
    DIV=9
    ID=10
    INT=11
    WS=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LispParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FuncCallContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LispParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FUNC(self):
            return self.getToken(LispParser.FUNC, 0)
        def expr(self):
            return self.getTypedRuleContext(LispParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncCall" ):
                listener.enterFuncCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncCall" ):
                listener.exitFuncCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncCall" ):
                return visitor.visitFuncCall(self)
            else:
                return visitor.visitChildren(self)


    class ParensContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LispParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(LispParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class LetContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LispParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LET(self):
            return self.getToken(LispParser.LET, 0)
        def expr(self):
            return self.getTypedRuleContext(LispParser.ExprContext,0)

        def var(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LispParser.VarContext)
            else:
                return self.getTypedRuleContext(LispParser.VarContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLet" ):
                listener.enterLet(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLet" ):
                listener.exitLet(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLet" ):
                return visitor.visitLet(self)
            else:
                return visitor.visitChildren(self)


    class IDContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LispParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(LispParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterID" ):
                listener.enterID(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitID" ):
                listener.exitID(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitID" ):
                return visitor.visitID(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LispParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(LispParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)


    class ArithmeticContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LispParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OP(self):
            return self.getToken(LispParser.OP, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LispParser.ExprContext)
            else:
                return self.getTypedRuleContext(LispParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmetic" ):
                listener.enterArithmetic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmetic" ):
                listener.exitArithmetic(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithmetic" ):
                return visitor.visitArithmetic(self)
            else:
                return visitor.visitChildren(self)



    def expr(self):

        localctx = LispParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 36
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = LispParser.ArithmeticContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 4
                self.match(LispParser.T__0)
                self.state = 5
                self.match(LispParser.OP)
                self.state = 7 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 6
                    self.expr()
                    self.state = 9 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 3074) != 0)):
                        break

                self.state = 11
                self.match(LispParser.T__1)
                pass

            elif la_ == 2:
                localctx = LispParser.IntContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 13
                self.match(LispParser.INT)
                pass

            elif la_ == 3:
                localctx = LispParser.IDContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 14
                self.match(LispParser.ID)
                pass

            elif la_ == 4:
                localctx = LispParser.ParensContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 15
                self.match(LispParser.T__0)
                self.state = 16
                self.expr()
                self.state = 17
                self.match(LispParser.T__1)
                pass

            elif la_ == 5:
                localctx = LispParser.FuncCallContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 19
                self.match(LispParser.T__0)
                self.state = 20
                self.match(LispParser.FUNC)
                self.state = 21
                self.expr()
                self.state = 22
                self.match(LispParser.T__1)
                pass

            elif la_ == 6:
                localctx = LispParser.LetContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 24
                self.match(LispParser.T__0)
                self.state = 25
                self.match(LispParser.LET)
                self.state = 26
                self.match(LispParser.T__0)
                self.state = 28 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 27
                    self.var()
                    self.state = 30 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==1):
                        break

                self.state = 32
                self.match(LispParser.T__1)
                self.state = 33
                self.expr()
                self.state = 34
                self.match(LispParser.T__1)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(LispParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(LispParser.ExprContext,0)


        def getRuleIndex(self):
            return LispParser.RULE_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar" ):
                listener.enterVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar" ):
                listener.exitVar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)




    def var(self):

        localctx = LispParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(LispParser.T__0)
            self.state = 39
            self.match(LispParser.ID)
            self.state = 40
            self.expr()
            self.state = 41
            self.match(LispParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





