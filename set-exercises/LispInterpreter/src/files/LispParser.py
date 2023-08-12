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
        4,1,8,23,2,0,7,0,2,1,7,1,1,0,1,0,1,0,4,0,8,8,0,11,0,12,0,9,1,0,1,
        0,1,0,1,0,1,0,1,0,1,0,3,0,19,8,0,1,1,1,1,1,1,0,0,2,0,2,0,1,1,0,3,
        6,23,0,18,1,0,0,0,2,20,1,0,0,0,4,5,5,1,0,0,5,7,3,2,1,0,6,8,3,0,0,
        0,7,6,1,0,0,0,8,9,1,0,0,0,9,7,1,0,0,0,9,10,1,0,0,0,10,11,1,0,0,0,
        11,12,5,2,0,0,12,19,1,0,0,0,13,19,5,7,0,0,14,15,5,1,0,0,15,16,3,
        0,0,0,16,17,5,2,0,0,17,19,1,0,0,0,18,4,1,0,0,0,18,13,1,0,0,0,18,
        14,1,0,0,0,19,1,1,0,0,0,20,21,7,0,0,0,21,3,1,0,0,0,2,9,18
    ]

class LispParser ( Parser ):

    grammarFileName = "Lisp.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "ADD", "SUB", 
                      "MUL", "DIV", "INT", "WS" ]

    RULE_expr = 0
    RULE_op = 1

    ruleNames =  [ "expr", "op" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    ADD=3
    SUB=4
    MUL=5
    DIV=6
    INT=7
    WS=8

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

        def op(self):
            return self.getTypedRuleContext(LispParser.OpContext,0)

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
            self.state = 18
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = LispParser.ArithmeticContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 4
                self.match(LispParser.T__0)
                self.state = 5
                self.op()
                self.state = 7 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 6
                    self.expr()
                    self.state = 9 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==1 or _la==7):
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
                localctx = LispParser.ParensContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 14
                self.match(LispParser.T__0)
                self.state = 15
                self.expr()
                self.state = 16
                self.match(LispParser.T__1)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(LispParser.ADD, 0)

        def SUB(self):
            return self.getToken(LispParser.SUB, 0)

        def MUL(self):
            return self.getToken(LispParser.MUL, 0)

        def DIV(self):
            return self.getToken(LispParser.DIV, 0)

        def getRuleIndex(self):
            return LispParser.RULE_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp" ):
                listener.enterOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp" ):
                listener.exitOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp" ):
                return visitor.visitOp(self)
            else:
                return visitor.visitChildren(self)




    def op(self):

        localctx = LispParser.OpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 120) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





