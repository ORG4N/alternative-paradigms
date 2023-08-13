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
        4,1,14,70,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,0,4,0,10,8,0,11,0,12,
        0,11,1,0,1,0,1,0,1,0,1,0,1,0,5,0,20,8,0,10,0,12,0,23,9,0,1,0,1,0,
        1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,4,0,40,8,0,11,
        0,12,0,41,1,0,1,0,1,0,1,0,1,0,1,0,4,0,50,8,0,11,0,12,0,51,1,0,1,
        0,1,0,1,0,3,0,58,8,0,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,
        0,0,3,0,2,4,0,0,77,0,57,1,0,0,0,2,59,1,0,0,0,4,64,1,0,0,0,6,7,5,
        1,0,0,7,9,5,3,0,0,8,10,3,0,0,0,9,8,1,0,0,0,10,11,1,0,0,0,11,9,1,
        0,0,0,11,12,1,0,0,0,12,13,1,0,0,0,13,14,5,2,0,0,14,58,1,0,0,0,15,
        58,5,13,0,0,16,58,5,12,0,0,17,21,5,1,0,0,18,20,3,0,0,0,19,18,1,0,
        0,0,20,23,1,0,0,0,21,19,1,0,0,0,21,22,1,0,0,0,22,24,1,0,0,0,23,21,
        1,0,0,0,24,58,5,2,0,0,25,26,5,1,0,0,26,27,5,4,0,0,27,28,3,0,0,0,
        28,29,5,2,0,0,29,58,1,0,0,0,30,31,5,1,0,0,31,32,5,5,0,0,32,33,3,
        0,0,0,33,34,3,0,0,0,34,35,5,2,0,0,35,58,1,0,0,0,36,37,5,1,0,0,37,
        39,5,6,0,0,38,40,3,4,2,0,39,38,1,0,0,0,40,41,1,0,0,0,41,39,1,0,0,
        0,41,42,1,0,0,0,42,43,1,0,0,0,43,44,5,2,0,0,44,58,1,0,0,0,45,46,
        5,1,0,0,46,47,5,7,0,0,47,49,5,1,0,0,48,50,3,2,1,0,49,48,1,0,0,0,
        50,51,1,0,0,0,51,49,1,0,0,0,51,52,1,0,0,0,52,53,1,0,0,0,53,54,5,
        2,0,0,54,55,3,0,0,0,55,56,5,2,0,0,56,58,1,0,0,0,57,6,1,0,0,0,57,
        15,1,0,0,0,57,16,1,0,0,0,57,17,1,0,0,0,57,25,1,0,0,0,57,30,1,0,0,
        0,57,36,1,0,0,0,57,45,1,0,0,0,58,1,1,0,0,0,59,60,5,1,0,0,60,61,5,
        12,0,0,61,62,3,0,0,0,62,63,5,2,0,0,63,3,1,0,0,0,64,65,5,1,0,0,65,
        66,3,0,0,0,66,67,3,0,0,0,67,68,5,2,0,0,68,5,1,0,0,0,5,11,21,41,51,
        57
    ]

class LispParser ( Parser ):

    grammarFileName = "Lisp.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "<INVALID>", "<INVALID>", 
                     "'eq'", "'cond'", "'let'", "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "OP", "FUNC", 
                      "EQ_FUNC", "COND_FUNC", "LET", "ADD", "SUB", "MUL", 
                      "DIV", "ID", "INT", "WS" ]

    RULE_expr = 0
    RULE_var = 1
    RULE_cond_clause = 2

    ruleNames =  [ "expr", "var", "cond_clause" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    OP=3
    FUNC=4
    EQ_FUNC=5
    COND_FUNC=6
    LET=7
    ADD=8
    SUB=9
    MUL=10
    DIV=11
    ID=12
    INT=13
    WS=14

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


    class FuncCondContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LispParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def COND_FUNC(self):
            return self.getToken(LispParser.COND_FUNC, 0)
        def cond_clause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LispParser.Cond_clauseContext)
            else:
                return self.getTypedRuleContext(LispParser.Cond_clauseContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncCond" ):
                listener.enterFuncCond(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncCond" ):
                listener.exitFuncCond(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncCond" ):
                return visitor.visitFuncCond(self)
            else:
                return visitor.visitChildren(self)


    class FuncEqContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LispParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def EQ_FUNC(self):
            return self.getToken(LispParser.EQ_FUNC, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LispParser.ExprContext)
            else:
                return self.getTypedRuleContext(LispParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncEq" ):
                listener.enterFuncEq(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncEq" ):
                listener.exitFuncEq(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncEq" ):
                return visitor.visitFuncEq(self)
            else:
                return visitor.visitChildren(self)


    class ListContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LispParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LispParser.ExprContext)
            else:
                return self.getTypedRuleContext(LispParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList" ):
                listener.enterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList" ):
                listener.exitList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList" ):
                return visitor.visitList(self)
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
            self.state = 57
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = LispParser.ArithmeticContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 6
                self.match(LispParser.T__0)
                self.state = 7
                self.match(LispParser.OP)
                self.state = 9 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 8
                    self.expr()
                    self.state = 11 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 12290) != 0)):
                        break

                self.state = 13
                self.match(LispParser.T__1)
                pass

            elif la_ == 2:
                localctx = LispParser.IntContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 15
                self.match(LispParser.INT)
                pass

            elif la_ == 3:
                localctx = LispParser.IDContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 16
                self.match(LispParser.ID)
                pass

            elif la_ == 4:
                localctx = LispParser.ListContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 17
                self.match(LispParser.T__0)
                self.state = 21
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 12290) != 0):
                    self.state = 18
                    self.expr()
                    self.state = 23
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 24
                self.match(LispParser.T__1)
                pass

            elif la_ == 5:
                localctx = LispParser.FuncCallContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 25
                self.match(LispParser.T__0)
                self.state = 26
                self.match(LispParser.FUNC)
                self.state = 27
                self.expr()
                self.state = 28
                self.match(LispParser.T__1)
                pass

            elif la_ == 6:
                localctx = LispParser.FuncEqContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 30
                self.match(LispParser.T__0)
                self.state = 31
                self.match(LispParser.EQ_FUNC)
                self.state = 32
                self.expr()
                self.state = 33
                self.expr()
                self.state = 34
                self.match(LispParser.T__1)
                pass

            elif la_ == 7:
                localctx = LispParser.FuncCondContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 36
                self.match(LispParser.T__0)
                self.state = 37
                self.match(LispParser.COND_FUNC)
                self.state = 39 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 38
                    self.cond_clause()
                    self.state = 41 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==1):
                        break

                self.state = 43
                self.match(LispParser.T__1)
                pass

            elif la_ == 8:
                localctx = LispParser.LetContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 45
                self.match(LispParser.T__0)
                self.state = 46
                self.match(LispParser.LET)
                self.state = 47
                self.match(LispParser.T__0)
                self.state = 49 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 48
                    self.var()
                    self.state = 51 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==1):
                        break

                self.state = 53
                self.match(LispParser.T__1)
                self.state = 54
                self.expr()
                self.state = 55
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
            self.state = 59
            self.match(LispParser.T__0)
            self.state = 60
            self.match(LispParser.ID)
            self.state = 61
            self.expr()
            self.state = 62
            self.match(LispParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cond_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LispParser.ExprContext)
            else:
                return self.getTypedRuleContext(LispParser.ExprContext,i)


        def getRuleIndex(self):
            return LispParser.RULE_cond_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCond_clause" ):
                listener.enterCond_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCond_clause" ):
                listener.exitCond_clause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCond_clause" ):
                return visitor.visitCond_clause(self)
            else:
                return visitor.visitChildren(self)




    def cond_clause(self):

        localctx = LispParser.Cond_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_cond_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(LispParser.T__0)
            self.state = 65
            self.expr()
            self.state = 66
            self.expr()
            self.state = 67
            self.match(LispParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





