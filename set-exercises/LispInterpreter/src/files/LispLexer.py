# Generated from grammar/Lisp.g4 by ANTLR 4.13.0
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,16,126,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,1,0,1,0,1,1,1,1,1,2,1,2,1,2,1,2,3,2,
        42,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,3,3,75,8,3,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,7,
        1,7,1,7,1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,1,11,1,11,1,12,4,12,103,
        8,12,11,12,12,12,104,1,13,3,13,108,8,13,1,13,4,13,111,8,13,11,13,
        12,13,112,1,14,4,14,116,8,14,11,14,12,14,117,1,15,4,15,121,8,15,
        11,15,12,15,122,1,15,1,15,0,0,16,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,
        8,17,9,19,10,21,11,23,12,25,13,27,14,29,15,31,16,1,0,5,2,0,65,90,
        97,122,2,0,43,43,45,45,1,0,48,57,3,0,46,46,65,90,97,122,3,0,9,10,
        13,13,32,32,140,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,
        0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,
        0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,
        0,29,1,0,0,0,0,31,1,0,0,0,1,33,1,0,0,0,3,35,1,0,0,0,5,41,1,0,0,0,
        7,74,1,0,0,0,9,76,1,0,0,0,11,79,1,0,0,0,13,84,1,0,0,0,15,88,1,0,
        0,0,17,93,1,0,0,0,19,95,1,0,0,0,21,97,1,0,0,0,23,99,1,0,0,0,25,102,
        1,0,0,0,27,107,1,0,0,0,29,115,1,0,0,0,31,120,1,0,0,0,33,34,5,40,
        0,0,34,2,1,0,0,0,35,36,5,41,0,0,36,4,1,0,0,0,37,42,3,17,8,0,38,42,
        3,19,9,0,39,42,3,21,10,0,40,42,3,23,11,0,41,37,1,0,0,0,41,38,1,0,
        0,0,41,39,1,0,0,0,41,40,1,0,0,0,42,6,1,0,0,0,43,44,5,115,0,0,44,
        45,5,105,0,0,45,75,5,110,0,0,46,47,5,99,0,0,47,48,5,111,0,0,48,75,
        5,115,0,0,49,50,5,115,0,0,50,51,5,113,0,0,51,52,5,117,0,0,52,53,
        5,97,0,0,53,54,5,114,0,0,54,75,5,101,0,0,55,56,5,115,0,0,56,57,5,
        113,0,0,57,58,5,114,0,0,58,75,5,116,0,0,59,60,5,99,0,0,60,61,5,97,
        0,0,61,75,5,114,0,0,62,63,5,99,0,0,63,64,5,100,0,0,64,75,5,114,0,
        0,65,66,5,113,0,0,66,67,5,117,0,0,67,68,5,111,0,0,68,69,5,116,0,
        0,69,75,5,101,0,0,70,71,5,97,0,0,71,72,5,116,0,0,72,73,5,111,0,0,
        73,75,5,109,0,0,74,43,1,0,0,0,74,46,1,0,0,0,74,49,1,0,0,0,74,55,
        1,0,0,0,74,59,1,0,0,0,74,62,1,0,0,0,74,65,1,0,0,0,74,70,1,0,0,0,
        75,8,1,0,0,0,76,77,5,101,0,0,77,78,5,113,0,0,78,10,1,0,0,0,79,80,
        5,99,0,0,80,81,5,111,0,0,81,82,5,110,0,0,82,83,5,100,0,0,83,12,1,
        0,0,0,84,85,5,108,0,0,85,86,5,101,0,0,86,87,5,116,0,0,87,14,1,0,
        0,0,88,89,5,108,0,0,89,90,5,111,0,0,90,91,5,97,0,0,91,92,5,100,0,
        0,92,16,1,0,0,0,93,94,5,43,0,0,94,18,1,0,0,0,95,96,5,45,0,0,96,20,
        1,0,0,0,97,98,5,42,0,0,98,22,1,0,0,0,99,100,5,47,0,0,100,24,1,0,
        0,0,101,103,7,0,0,0,102,101,1,0,0,0,103,104,1,0,0,0,104,102,1,0,
        0,0,104,105,1,0,0,0,105,26,1,0,0,0,106,108,7,1,0,0,107,106,1,0,0,
        0,107,108,1,0,0,0,108,110,1,0,0,0,109,111,7,2,0,0,110,109,1,0,0,
        0,111,112,1,0,0,0,112,110,1,0,0,0,112,113,1,0,0,0,113,28,1,0,0,0,
        114,116,7,3,0,0,115,114,1,0,0,0,116,117,1,0,0,0,117,115,1,0,0,0,
        117,118,1,0,0,0,118,30,1,0,0,0,119,121,7,4,0,0,120,119,1,0,0,0,121,
        122,1,0,0,0,122,120,1,0,0,0,122,123,1,0,0,0,123,124,1,0,0,0,124,
        125,6,15,0,0,125,32,1,0,0,0,8,0,41,74,104,107,112,117,122,1,6,0,
        0
    ]

class LispLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    OP = 3
    FUNC = 4
    EQ_FUNC = 5
    COND_FUNC = 6
    LET = 7
    LOAD = 8
    ADD = 9
    SUB = 10
    MUL = 11
    DIV = 12
    ID = 13
    INT = 14
    STRING = 15
    WS = 16

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'eq'", "'cond'", "'let'", "'load'", "'+'", "'-'", 
            "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>",
            "OP", "FUNC", "EQ_FUNC", "COND_FUNC", "LET", "LOAD", "ADD", 
            "SUB", "MUL", "DIV", "ID", "INT", "STRING", "WS" ]

    ruleNames = [ "T__0", "T__1", "OP", "FUNC", "EQ_FUNC", "COND_FUNC", 
                  "LET", "LOAD", "ADD", "SUB", "MUL", "DIV", "ID", "INT", 
                  "STRING", "WS" ]

    grammarFileName = "Lisp.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


