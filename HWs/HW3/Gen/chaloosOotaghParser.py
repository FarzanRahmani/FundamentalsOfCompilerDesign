# Generated from E:/uni/7th term/fundamentals of compiler design/HWs/HW3/chaloosOotagh.g4 by ANTLR 4.13.1
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
        4,1,27,279,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,1,0,1,0,5,0,33,8,0,10,0,12,0,36,9,0,1,0,1,0,1,1,5,1,41,
        8,1,10,1,12,1,44,9,1,1,1,3,1,47,8,1,1,1,5,1,50,8,1,10,1,12,1,53,
        9,1,1,1,1,1,5,1,57,8,1,10,1,12,1,60,9,1,4,1,62,8,1,11,1,12,1,63,
        1,2,5,2,67,8,2,10,2,12,2,70,9,2,1,2,1,2,5,2,74,8,2,10,2,12,2,77,
        9,2,4,2,79,8,2,11,2,12,2,80,1,3,1,3,5,3,85,8,3,10,3,12,3,88,9,3,
        1,3,1,3,1,3,3,3,93,8,3,1,3,1,3,1,4,1,4,1,5,1,5,1,5,1,5,3,5,103,8,
        5,1,6,1,6,5,6,107,8,6,10,6,12,6,110,9,6,1,6,1,6,5,6,114,8,6,10,6,
        12,6,117,9,6,5,6,119,8,6,10,6,12,6,122,9,6,1,6,1,6,1,7,1,7,1,7,1,
        7,1,7,1,7,5,7,132,8,7,10,7,12,7,135,9,7,1,7,1,7,5,7,139,8,7,10,7,
        12,7,142,9,7,5,7,144,8,7,10,7,12,7,147,9,7,1,7,1,7,1,8,1,8,1,8,1,
        8,1,8,5,8,156,8,8,10,8,12,8,159,9,8,1,8,1,8,5,8,163,8,8,10,8,12,
        8,166,9,8,1,8,1,8,5,8,170,8,8,10,8,12,8,173,9,8,5,8,175,8,8,10,8,
        12,8,178,9,8,1,8,1,8,1,8,5,8,183,8,8,10,8,12,8,186,9,8,1,8,1,8,5,
        8,190,8,8,10,8,12,8,193,9,8,1,8,1,8,5,8,197,8,8,10,8,12,8,200,9,
        8,5,8,202,8,8,10,8,12,8,205,9,8,1,8,3,8,208,8,8,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,222,8,9,1,9,1,9,1,9,5,9,227,
        8,9,10,9,12,9,230,9,9,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,
        11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,5,11,249,8,11,10,11,12,
        11,252,9,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,5,12,263,
        8,12,10,12,12,12,266,9,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,
        275,8,13,1,14,1,14,1,14,0,3,18,22,24,15,0,2,4,6,8,10,12,14,16,18,
        20,22,24,26,28,0,1,1,0,3,4,304,0,30,1,0,0,0,2,42,1,0,0,0,4,68,1,
        0,0,0,6,82,1,0,0,0,8,96,1,0,0,0,10,102,1,0,0,0,12,104,1,0,0,0,14,
        125,1,0,0,0,16,150,1,0,0,0,18,221,1,0,0,0,20,231,1,0,0,0,22,236,
        1,0,0,0,24,253,1,0,0,0,26,274,1,0,0,0,28,276,1,0,0,0,30,34,3,2,1,
        0,31,33,5,23,0,0,32,31,1,0,0,0,33,36,1,0,0,0,34,32,1,0,0,0,34,35,
        1,0,0,0,35,37,1,0,0,0,36,34,1,0,0,0,37,38,5,0,0,1,38,1,1,0,0,0,39,
        41,5,23,0,0,40,39,1,0,0,0,41,44,1,0,0,0,42,40,1,0,0,0,42,43,1,0,
        0,0,43,46,1,0,0,0,44,42,1,0,0,0,45,47,3,4,2,0,46,45,1,0,0,0,46,47,
        1,0,0,0,47,51,1,0,0,0,48,50,5,23,0,0,49,48,1,0,0,0,50,53,1,0,0,0,
        51,49,1,0,0,0,51,52,1,0,0,0,52,61,1,0,0,0,53,51,1,0,0,0,54,58,3,
        10,5,0,55,57,5,23,0,0,56,55,1,0,0,0,57,60,1,0,0,0,58,56,1,0,0,0,
        58,59,1,0,0,0,59,62,1,0,0,0,60,58,1,0,0,0,61,54,1,0,0,0,62,63,1,
        0,0,0,63,61,1,0,0,0,63,64,1,0,0,0,64,3,1,0,0,0,65,67,5,23,0,0,66,
        65,1,0,0,0,67,70,1,0,0,0,68,66,1,0,0,0,68,69,1,0,0,0,69,78,1,0,0,
        0,70,68,1,0,0,0,71,75,3,6,3,0,72,74,5,23,0,0,73,72,1,0,0,0,74,77,
        1,0,0,0,75,73,1,0,0,0,75,76,1,0,0,0,76,79,1,0,0,0,77,75,1,0,0,0,
        78,71,1,0,0,0,79,80,1,0,0,0,80,78,1,0,0,0,80,81,1,0,0,0,81,5,1,0,
        0,0,82,86,3,8,4,0,83,85,5,23,0,0,84,83,1,0,0,0,85,88,1,0,0,0,86,
        84,1,0,0,0,86,87,1,0,0,0,87,89,1,0,0,0,88,86,1,0,0,0,89,92,5,21,
        0,0,90,91,5,1,0,0,91,93,3,22,11,0,92,90,1,0,0,0,92,93,1,0,0,0,93,
        94,1,0,0,0,94,95,5,2,0,0,95,7,1,0,0,0,96,97,7,0,0,0,97,9,1,0,0,0,
        98,103,3,16,8,0,99,103,3,20,10,0,100,103,3,12,6,0,101,103,3,14,7,
        0,102,98,1,0,0,0,102,99,1,0,0,0,102,100,1,0,0,0,102,101,1,0,0,0,
        103,11,1,0,0,0,104,108,5,5,0,0,105,107,5,23,0,0,106,105,1,0,0,0,
        107,110,1,0,0,0,108,106,1,0,0,0,108,109,1,0,0,0,109,120,1,0,0,0,
        110,108,1,0,0,0,111,115,3,10,5,0,112,114,5,23,0,0,113,112,1,0,0,
        0,114,117,1,0,0,0,115,113,1,0,0,0,115,116,1,0,0,0,116,119,1,0,0,
        0,117,115,1,0,0,0,118,111,1,0,0,0,119,122,1,0,0,0,120,118,1,0,0,
        0,120,121,1,0,0,0,121,123,1,0,0,0,122,120,1,0,0,0,123,124,5,6,0,
        0,124,13,1,0,0,0,125,126,5,7,0,0,126,127,5,8,0,0,127,128,3,18,9,
        0,128,129,5,9,0,0,129,133,5,10,0,0,130,132,5,23,0,0,131,130,1,0,
        0,0,132,135,1,0,0,0,133,131,1,0,0,0,133,134,1,0,0,0,134,145,1,0,
        0,0,135,133,1,0,0,0,136,140,3,10,5,0,137,139,5,23,0,0,138,137,1,
        0,0,0,139,142,1,0,0,0,140,138,1,0,0,0,140,141,1,0,0,0,141,144,1,
        0,0,0,142,140,1,0,0,0,143,136,1,0,0,0,144,147,1,0,0,0,145,143,1,
        0,0,0,145,146,1,0,0,0,146,148,1,0,0,0,147,145,1,0,0,0,148,149,5,
        11,0,0,149,15,1,0,0,0,150,151,5,12,0,0,151,152,5,8,0,0,152,153,3,
        18,9,0,153,157,5,9,0,0,154,156,5,23,0,0,155,154,1,0,0,0,156,159,
        1,0,0,0,157,155,1,0,0,0,157,158,1,0,0,0,158,160,1,0,0,0,159,157,
        1,0,0,0,160,164,5,10,0,0,161,163,5,23,0,0,162,161,1,0,0,0,163,166,
        1,0,0,0,164,162,1,0,0,0,164,165,1,0,0,0,165,176,1,0,0,0,166,164,
        1,0,0,0,167,171,3,10,5,0,168,170,5,23,0,0,169,168,1,0,0,0,170,173,
        1,0,0,0,171,169,1,0,0,0,171,172,1,0,0,0,172,175,1,0,0,0,173,171,
        1,0,0,0,174,167,1,0,0,0,175,178,1,0,0,0,176,174,1,0,0,0,176,177,
        1,0,0,0,177,179,1,0,0,0,178,176,1,0,0,0,179,207,5,11,0,0,180,184,
        5,13,0,0,181,183,5,23,0,0,182,181,1,0,0,0,183,186,1,0,0,0,184,182,
        1,0,0,0,184,185,1,0,0,0,185,187,1,0,0,0,186,184,1,0,0,0,187,191,
        5,10,0,0,188,190,5,23,0,0,189,188,1,0,0,0,190,193,1,0,0,0,191,189,
        1,0,0,0,191,192,1,0,0,0,192,203,1,0,0,0,193,191,1,0,0,0,194,198,
        3,10,5,0,195,197,5,23,0,0,196,195,1,0,0,0,197,200,1,0,0,0,198,196,
        1,0,0,0,198,199,1,0,0,0,199,202,1,0,0,0,200,198,1,0,0,0,201,194,
        1,0,0,0,202,205,1,0,0,0,203,201,1,0,0,0,203,204,1,0,0,0,204,206,
        1,0,0,0,205,203,1,0,0,0,206,208,5,11,0,0,207,180,1,0,0,0,207,208,
        1,0,0,0,208,17,1,0,0,0,209,210,6,9,-1,0,210,211,3,22,11,0,211,212,
        5,24,0,0,212,213,3,22,11,0,213,222,1,0,0,0,214,222,5,20,0,0,215,
        216,5,8,0,0,216,217,3,18,9,0,217,218,5,9,0,0,218,222,1,0,0,0,219,
        220,5,14,0,0,220,222,3,18,9,1,221,209,1,0,0,0,221,214,1,0,0,0,221,
        215,1,0,0,0,221,219,1,0,0,0,222,228,1,0,0,0,223,224,10,2,0,0,224,
        225,5,25,0,0,225,227,3,18,9,3,226,223,1,0,0,0,227,230,1,0,0,0,228,
        226,1,0,0,0,228,229,1,0,0,0,229,19,1,0,0,0,230,228,1,0,0,0,231,232,
        5,21,0,0,232,233,5,1,0,0,233,234,3,22,11,0,234,235,5,2,0,0,235,21,
        1,0,0,0,236,237,6,11,-1,0,237,238,3,24,12,0,238,250,1,0,0,0,239,
        240,10,4,0,0,240,241,5,15,0,0,241,249,3,24,12,0,242,243,10,3,0,0,
        243,244,5,16,0,0,244,249,3,24,12,0,245,246,10,2,0,0,246,247,5,24,
        0,0,247,249,3,24,12,0,248,239,1,0,0,0,248,242,1,0,0,0,248,245,1,
        0,0,0,249,252,1,0,0,0,250,248,1,0,0,0,250,251,1,0,0,0,251,23,1,0,
        0,0,252,250,1,0,0,0,253,254,6,12,-1,0,254,255,3,26,13,0,255,264,
        1,0,0,0,256,257,10,3,0,0,257,258,5,17,0,0,258,263,3,26,13,0,259,
        260,10,2,0,0,260,261,5,18,0,0,261,263,3,26,13,0,262,256,1,0,0,0,
        262,259,1,0,0,0,263,266,1,0,0,0,264,262,1,0,0,0,264,265,1,0,0,0,
        265,25,1,0,0,0,266,264,1,0,0,0,267,268,5,8,0,0,268,269,3,22,11,0,
        269,270,5,9,0,0,270,275,1,0,0,0,271,275,5,21,0,0,272,275,3,28,14,
        0,273,275,5,20,0,0,274,267,1,0,0,0,274,271,1,0,0,0,274,272,1,0,0,
        0,274,273,1,0,0,0,275,27,1,0,0,0,276,277,5,19,0,0,277,29,1,0,0,0,
        34,34,42,46,51,58,63,68,75,80,86,92,102,108,115,120,133,140,145,
        157,164,171,176,184,191,198,203,207,221,228,248,250,262,264,274
    ]

class chaloosOotaghParser ( Parser ):

    grammarFileName = "chaloosOotagh.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "';'", "'int'", "'boolean'", "'begin'", 
                     "'end'", "'while'", "'('", "')'", "'{'", "'}'", "'if'", 
                     "'else'", "'!'", "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "INT", "BOOLEAN", 
                      "ID", "WS", "NEWLINE", "RELOP", "LOGICOP", "ArithOp", 
                      "LINE_COMMENT" ]

    RULE_start = 0
    RULE_prog = 1
    RULE_declaration = 2
    RULE_variable_declaration = 3
    RULE_type = 4
    RULE_statement = 5
    RULE_compoundst = 6
    RULE_whilest = 7
    RULE_ifst = 8
    RULE_cond = 9
    RULE_assign = 10
    RULE_expr = 11
    RULE_term = 12
    RULE_factor = 13
    RULE_number = 14

    ruleNames =  [ "start", "prog", "declaration", "variable_declaration", 
                   "type", "statement", "compoundst", "whilest", "ifst", 
                   "cond", "assign", "expr", "term", "factor", "number" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    INT=19
    BOOLEAN=20
    ID=21
    WS=22
    NEWLINE=23
    RELOP=24
    LOGICOP=25
    ArithOp=26
    LINE_COMMENT=27

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def prog(self):
            return self.getTypedRuleContext(chaloosOotaghParser.ProgContext,0)


        def EOF(self):
            return self.getToken(chaloosOotaghParser.EOF, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(chaloosOotaghParser.NEWLINE)
            else:
                return self.getToken(chaloosOotaghParser.NEWLINE, i)

        def getRuleIndex(self):
            return chaloosOotaghParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = chaloosOotaghParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.prog()
            self.state = 34
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==23:
                self.state = 31
                self.match(chaloosOotaghParser.NEWLINE)
                self.state = 36
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 37
            self.match(chaloosOotaghParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(chaloosOotaghParser.NEWLINE)
            else:
                return self.getToken(chaloosOotaghParser.NEWLINE, i)

        def declaration(self):
            return self.getTypedRuleContext(chaloosOotaghParser.DeclarationContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(chaloosOotaghParser.StatementContext)
            else:
                return self.getTypedRuleContext(chaloosOotaghParser.StatementContext,i)


        def getRuleIndex(self):
            return chaloosOotaghParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = chaloosOotaghParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 39
                    self.match(chaloosOotaghParser.NEWLINE) 
                self.state = 44
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 46
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 45
                self.declaration()


            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==23:
                self.state = 48
                self.match(chaloosOotaghParser.NEWLINE)
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 61 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 54
                self.statement()
                self.state = 58
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 55
                        self.match(chaloosOotaghParser.NEWLINE) 
                    self.state = 60
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

                self.state = 63 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2101408) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(chaloosOotaghParser.NEWLINE)
            else:
                return self.getToken(chaloosOotaghParser.NEWLINE, i)

        def variable_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(chaloosOotaghParser.Variable_declarationContext)
            else:
                return self.getTypedRuleContext(chaloosOotaghParser.Variable_declarationContext,i)


        def getRuleIndex(self):
            return chaloosOotaghParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = chaloosOotaghParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==23:
                self.state = 65
                self.match(chaloosOotaghParser.NEWLINE)
                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 78 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 71
                self.variable_declaration()
                self.state = 75
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 72
                        self.match(chaloosOotaghParser.NEWLINE) 
                    self.state = 77
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

                self.state = 80 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==3 or _la==4):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(chaloosOotaghParser.TypeContext,0)


        def ID(self):
            return self.getToken(chaloosOotaghParser.ID, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(chaloosOotaghParser.NEWLINE)
            else:
                return self.getToken(chaloosOotaghParser.NEWLINE, i)

        def expr(self):
            return self.getTypedRuleContext(chaloosOotaghParser.ExprContext,0)


        def getRuleIndex(self):
            return chaloosOotaghParser.RULE_variable_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable_declaration" ):
                listener.enterVariable_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable_declaration" ):
                listener.exitVariable_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_declaration" ):
                return visitor.visitVariable_declaration(self)
            else:
                return visitor.visitChildren(self)




    def variable_declaration(self):

        localctx = chaloosOotaghParser.Variable_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_variable_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.type_()
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==23:
                self.state = 83
                self.match(chaloosOotaghParser.NEWLINE)
                self.state = 88
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 89
            self.match(chaloosOotaghParser.ID)
            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 90
                self.match(chaloosOotaghParser.T__0)
                self.state = 91
                self.expr(0)


            self.state = 94
            self.match(chaloosOotaghParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return chaloosOotaghParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = chaloosOotaghParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            _la = self._input.LA(1)
            if not(_la==3 or _la==4):
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


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifst(self):
            return self.getTypedRuleContext(chaloosOotaghParser.IfstContext,0)


        def assign(self):
            return self.getTypedRuleContext(chaloosOotaghParser.AssignContext,0)


        def compoundst(self):
            return self.getTypedRuleContext(chaloosOotaghParser.CompoundstContext,0)


        def whilest(self):
            return self.getTypedRuleContext(chaloosOotaghParser.WhilestContext,0)


        def getRuleIndex(self):
            return chaloosOotaghParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = chaloosOotaghParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_statement)
        try:
            self.state = 102
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 98
                self.ifst()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 99
                self.assign()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 100
                self.compoundst()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 4)
                self.state = 101
                self.whilest()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompoundstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(chaloosOotaghParser.NEWLINE)
            else:
                return self.getToken(chaloosOotaghParser.NEWLINE, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(chaloosOotaghParser.StatementContext)
            else:
                return self.getTypedRuleContext(chaloosOotaghParser.StatementContext,i)


        def getRuleIndex(self):
            return chaloosOotaghParser.RULE_compoundst

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompoundst" ):
                listener.enterCompoundst(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompoundst" ):
                listener.exitCompoundst(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompoundst" ):
                return visitor.visitCompoundst(self)
            else:
                return visitor.visitChildren(self)




    def compoundst(self):

        localctx = chaloosOotaghParser.CompoundstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_compoundst)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(chaloosOotaghParser.T__4)
            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==23:
                self.state = 105
                self.match(chaloosOotaghParser.NEWLINE)
                self.state = 110
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2101408) != 0):
                self.state = 111
                self.statement()
                self.state = 115
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==23:
                    self.state = 112
                    self.match(chaloosOotaghParser.NEWLINE)
                    self.state = 117
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 122
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 123
            self.match(chaloosOotaghParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhilestContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def cond(self):
            return self.getTypedRuleContext(chaloosOotaghParser.CondContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(chaloosOotaghParser.NEWLINE)
            else:
                return self.getToken(chaloosOotaghParser.NEWLINE, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(chaloosOotaghParser.StatementContext)
            else:
                return self.getTypedRuleContext(chaloosOotaghParser.StatementContext,i)


        def getRuleIndex(self):
            return chaloosOotaghParser.RULE_whilest

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhilest" ):
                listener.enterWhilest(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhilest" ):
                listener.exitWhilest(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhilest" ):
                return visitor.visitWhilest(self)
            else:
                return visitor.visitChildren(self)




    def whilest(self):

        localctx = chaloosOotaghParser.WhilestContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_whilest)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(chaloosOotaghParser.T__6)
            self.state = 126
            self.match(chaloosOotaghParser.T__7)
            self.state = 127
            self.cond(0)
            self.state = 128
            self.match(chaloosOotaghParser.T__8)
            self.state = 129
            self.match(chaloosOotaghParser.T__9)
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==23:
                self.state = 130
                self.match(chaloosOotaghParser.NEWLINE)
                self.state = 135
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2101408) != 0):
                self.state = 136
                self.statement()
                self.state = 140
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==23:
                    self.state = 137
                    self.match(chaloosOotaghParser.NEWLINE)
                    self.state = 142
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 147
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 148
            self.match(chaloosOotaghParser.T__10)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def cond(self):
            return self.getTypedRuleContext(chaloosOotaghParser.CondContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(chaloosOotaghParser.NEWLINE)
            else:
                return self.getToken(chaloosOotaghParser.NEWLINE, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(chaloosOotaghParser.StatementContext)
            else:
                return self.getTypedRuleContext(chaloosOotaghParser.StatementContext,i)


        def getRuleIndex(self):
            return chaloosOotaghParser.RULE_ifst

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfst" ):
                listener.enterIfst(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfst" ):
                listener.exitIfst(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfst" ):
                return visitor.visitIfst(self)
            else:
                return visitor.visitChildren(self)




    def ifst(self):

        localctx = chaloosOotaghParser.IfstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_ifst)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(chaloosOotaghParser.T__11)
            self.state = 151
            self.match(chaloosOotaghParser.T__7)
            self.state = 152
            self.cond(0)
            self.state = 153
            self.match(chaloosOotaghParser.T__8)
            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==23:
                self.state = 154
                self.match(chaloosOotaghParser.NEWLINE)
                self.state = 159
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 160
            self.match(chaloosOotaghParser.T__9)
            self.state = 164
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==23:
                self.state = 161
                self.match(chaloosOotaghParser.NEWLINE)
                self.state = 166
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2101408) != 0):
                self.state = 167
                self.statement()
                self.state = 171
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==23:
                    self.state = 168
                    self.match(chaloosOotaghParser.NEWLINE)
                    self.state = 173
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 178
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 179
            self.match(chaloosOotaghParser.T__10)
            self.state = 207
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 180
                self.match(chaloosOotaghParser.T__12)
                self.state = 184
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==23:
                    self.state = 181
                    self.match(chaloosOotaghParser.NEWLINE)
                    self.state = 186
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 187
                self.match(chaloosOotaghParser.T__9)
                self.state = 191
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==23:
                    self.state = 188
                    self.match(chaloosOotaghParser.NEWLINE)
                    self.state = 193
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 203
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2101408) != 0):
                    self.state = 194
                    self.statement()
                    self.state = 198
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==23:
                        self.state = 195
                        self.match(chaloosOotaghParser.NEWLINE)
                        self.state = 200
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 205
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 206
                self.match(chaloosOotaghParser.T__10)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(chaloosOotaghParser.ExprContext)
            else:
                return self.getTypedRuleContext(chaloosOotaghParser.ExprContext,i)


        def RELOP(self):
            return self.getToken(chaloosOotaghParser.RELOP, 0)

        def BOOLEAN(self):
            return self.getToken(chaloosOotaghParser.BOOLEAN, 0)

        def cond(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(chaloosOotaghParser.CondContext)
            else:
                return self.getTypedRuleContext(chaloosOotaghParser.CondContext,i)


        def LOGICOP(self):
            return self.getToken(chaloosOotaghParser.LOGICOP, 0)

        def getRuleIndex(self):
            return chaloosOotaghParser.RULE_cond

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCond" ):
                listener.enterCond(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCond" ):
                listener.exitCond(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCond" ):
                return visitor.visitCond(self)
            else:
                return visitor.visitChildren(self)



    def cond(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = chaloosOotaghParser.CondContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_cond, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 210
                self.expr(0)
                self.state = 211
                self.match(chaloosOotaghParser.RELOP)
                self.state = 212
                self.expr(0)
                pass

            elif la_ == 2:
                self.state = 214
                self.match(chaloosOotaghParser.BOOLEAN)
                pass

            elif la_ == 3:
                self.state = 215
                self.match(chaloosOotaghParser.T__7)
                self.state = 216
                self.cond(0)
                self.state = 217
                self.match(chaloosOotaghParser.T__8)
                pass

            elif la_ == 4:
                self.state = 219
                self.match(chaloosOotaghParser.T__13)
                self.state = 220
                self.cond(1)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 228
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = chaloosOotaghParser.CondContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_cond)
                    self.state = 223
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 224
                    self.match(chaloosOotaghParser.LOGICOP)
                    self.state = 225
                    self.cond(3) 
                self.state = 230
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(chaloosOotaghParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(chaloosOotaghParser.ExprContext,0)


        def getRuleIndex(self):
            return chaloosOotaghParser.RULE_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)




    def assign(self):

        localctx = chaloosOotaghParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.match(chaloosOotaghParser.ID)
            self.state = 232
            self.match(chaloosOotaghParser.T__0)
            self.state = 233
            self.expr(0)
            self.state = 234
            self.match(chaloosOotaghParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return chaloosOotaghParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class Expr_term_minusContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a chaloosOotaghParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(chaloosOotaghParser.ExprContext,0)

        def term(self):
            return self.getTypedRuleContext(chaloosOotaghParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_term_minus" ):
                listener.enterExpr_term_minus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_term_minus" ):
                listener.exitExpr_term_minus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_term_minus" ):
                return visitor.visitExpr_term_minus(self)
            else:
                return visitor.visitChildren(self)


    class Expr_term_plusContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a chaloosOotaghParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(chaloosOotaghParser.ExprContext,0)

        def term(self):
            return self.getTypedRuleContext(chaloosOotaghParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_term_plus" ):
                listener.enterExpr_term_plus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_term_plus" ):
                listener.exitExpr_term_plus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_term_plus" ):
                return visitor.visitExpr_term_plus(self)
            else:
                return visitor.visitChildren(self)


    class Term4Context(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a chaloosOotaghParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(chaloosOotaghParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm4" ):
                listener.enterTerm4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm4" ):
                listener.exitTerm4(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm4" ):
                return visitor.visitTerm4(self)
            else:
                return visitor.visitChildren(self)


    class Expr_term_relopContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a chaloosOotaghParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(chaloosOotaghParser.ExprContext,0)

        def RELOP(self):
            return self.getToken(chaloosOotaghParser.RELOP, 0)
        def term(self):
            return self.getTypedRuleContext(chaloosOotaghParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_term_relop" ):
                listener.enterExpr_term_relop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_term_relop" ):
                listener.exitExpr_term_relop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_term_relop" ):
                return visitor.visitExpr_term_relop(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = chaloosOotaghParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = chaloosOotaghParser.Term4Context(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 237
            self.term(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 250
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 248
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
                    if la_ == 1:
                        localctx = chaloosOotaghParser.Expr_term_plusContext(self, chaloosOotaghParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 239
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 240
                        self.match(chaloosOotaghParser.T__14)
                        self.state = 241
                        self.term(0)
                        pass

                    elif la_ == 2:
                        localctx = chaloosOotaghParser.Expr_term_minusContext(self, chaloosOotaghParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 242
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 243
                        self.match(chaloosOotaghParser.T__15)
                        self.state = 244
                        self.term(0)
                        pass

                    elif la_ == 3:
                        localctx = chaloosOotaghParser.Expr_term_relopContext(self, chaloosOotaghParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 245
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 246
                        self.match(chaloosOotaghParser.RELOP)
                        self.state = 247
                        self.term(0)
                        pass

             
                self.state = 252
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return chaloosOotaghParser.RULE_term

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class Term_fact_divideContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a chaloosOotaghParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(chaloosOotaghParser.TermContext,0)

        def factor(self):
            return self.getTypedRuleContext(chaloosOotaghParser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm_fact_divide" ):
                listener.enterTerm_fact_divide(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm_fact_divide" ):
                listener.exitTerm_fact_divide(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm_fact_divide" ):
                return visitor.visitTerm_fact_divide(self)
            else:
                return visitor.visitChildren(self)


    class Term_fact_mutiplyContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a chaloosOotaghParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(chaloosOotaghParser.TermContext,0)

        def factor(self):
            return self.getTypedRuleContext(chaloosOotaghParser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm_fact_mutiply" ):
                listener.enterTerm_fact_mutiply(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm_fact_mutiply" ):
                listener.exitTerm_fact_mutiply(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm_fact_mutiply" ):
                return visitor.visitTerm_fact_mutiply(self)
            else:
                return visitor.visitChildren(self)


    class Factor3Context(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a chaloosOotaghParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def factor(self):
            return self.getTypedRuleContext(chaloosOotaghParser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor3" ):
                listener.enterFactor3(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor3" ):
                listener.exitFactor3(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor3" ):
                return visitor.visitFactor3(self)
            else:
                return visitor.visitChildren(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = chaloosOotaghParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_term, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = chaloosOotaghParser.Factor3Context(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 254
            self.factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 264
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 262
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
                    if la_ == 1:
                        localctx = chaloosOotaghParser.Term_fact_mutiplyContext(self, chaloosOotaghParser.TermContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 256
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 257
                        self.match(chaloosOotaghParser.T__16)
                        self.state = 258
                        self.factor()
                        pass

                    elif la_ == 2:
                        localctx = chaloosOotaghParser.Term_fact_divideContext(self, chaloosOotaghParser.TermContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 259
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 260
                        self.match(chaloosOotaghParser.T__17)
                        self.state = 261
                        self.factor()
                        pass

             
                self.state = 266
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return chaloosOotaghParser.RULE_factor

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Fact_exprContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a chaloosOotaghParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(chaloosOotaghParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFact_expr" ):
                listener.enterFact_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFact_expr" ):
                listener.exitFact_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFact_expr" ):
                return visitor.visitFact_expr(self)
            else:
                return visitor.visitChildren(self)


    class Fact_idContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a chaloosOotaghParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(chaloosOotaghParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFact_id" ):
                listener.enterFact_id(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFact_id" ):
                listener.exitFact_id(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFact_id" ):
                return visitor.visitFact_id(self)
            else:
                return visitor.visitChildren(self)


    class Fact_booleanContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a chaloosOotaghParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOLEAN(self):
            return self.getToken(chaloosOotaghParser.BOOLEAN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFact_boolean" ):
                listener.enterFact_boolean(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFact_boolean" ):
                listener.exitFact_boolean(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFact_boolean" ):
                return visitor.visitFact_boolean(self)
            else:
                return visitor.visitChildren(self)


    class Fact_numberContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a chaloosOotaghParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def number(self):
            return self.getTypedRuleContext(chaloosOotaghParser.NumberContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFact_number" ):
                listener.enterFact_number(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFact_number" ):
                listener.exitFact_number(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFact_number" ):
                return visitor.visitFact_number(self)
            else:
                return visitor.visitChildren(self)



    def factor(self):

        localctx = chaloosOotaghParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_factor)
        try:
            self.state = 274
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                localctx = chaloosOotaghParser.Fact_exprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 267
                self.match(chaloosOotaghParser.T__7)
                self.state = 268
                self.expr(0)
                self.state = 269
                self.match(chaloosOotaghParser.T__8)
                pass
            elif token in [21]:
                localctx = chaloosOotaghParser.Fact_idContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 271
                self.match(chaloosOotaghParser.ID)
                pass
            elif token in [19]:
                localctx = chaloosOotaghParser.Fact_numberContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 272
                self.number()
                pass
            elif token in [20]:
                localctx = chaloosOotaghParser.Fact_booleanContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 273
                self.match(chaloosOotaghParser.BOOLEAN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return chaloosOotaghParser.RULE_number

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Number_intContext(NumberContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a chaloosOotaghParser.NumberContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(chaloosOotaghParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber_int" ):
                listener.enterNumber_int(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber_int" ):
                listener.exitNumber_int(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber_int" ):
                return visitor.visitNumber_int(self)
            else:
                return visitor.visitChildren(self)



    def number(self):

        localctx = chaloosOotaghParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_number)
        try:
            localctx = chaloosOotaghParser.Number_intContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.match(chaloosOotaghParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[9] = self.cond_sempred
        self._predicates[11] = self.expr_sempred
        self._predicates[12] = self.term_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def cond_sempred(self, localctx:CondContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         




