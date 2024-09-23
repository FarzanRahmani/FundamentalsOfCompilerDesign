# Generated from E:/uni/7th term/fundamentals of compiler design/mid_term/ASTListener/AssignmentStatement.g4 by ANTLR 4.13.1
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
        4,1,41,294,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,1,0,1,0,5,0,41,
        8,0,10,0,12,0,44,9,0,1,0,1,0,1,1,1,1,1,1,5,1,51,8,1,10,1,12,1,54,
        9,1,1,1,3,1,57,8,1,1,1,4,1,60,8,1,11,1,12,1,61,1,1,1,1,1,2,1,2,5,
        2,68,8,2,10,2,12,2,71,9,2,1,2,1,2,5,2,75,8,2,10,2,12,2,78,9,2,4,
        2,80,8,2,11,2,12,2,81,1,3,1,3,1,3,1,3,1,4,1,4,1,5,1,5,5,5,92,8,5,
        10,5,12,5,95,9,5,1,5,1,5,4,5,99,8,5,11,5,12,5,100,4,5,103,8,5,11,
        5,12,5,104,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,116,8,6,1,7,1,
        7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,5,8,132,8,8,10,
        8,12,8,135,9,8,1,8,1,8,1,9,1,9,1,9,1,9,5,9,143,8,9,10,9,12,9,146,
        9,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,3,10,155,8,10,1,10,1,10,5,10,
        159,8,10,10,10,12,10,162,9,10,1,10,1,10,1,10,1,10,3,10,168,8,10,
        1,10,1,10,5,10,172,8,10,10,10,12,10,175,9,10,1,10,5,10,178,8,10,
        10,10,12,10,181,9,10,1,10,1,10,1,10,5,10,186,8,10,10,10,12,10,189,
        9,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,5,11,198,8,11,10,11,12,11,
        201,9,11,1,11,1,11,5,11,205,8,11,10,11,12,11,208,9,11,1,11,1,11,
        5,11,212,8,11,10,11,12,11,215,9,11,1,11,3,11,218,8,11,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,231,8,12,1,12,
        1,12,1,12,5,12,236,8,12,10,12,12,12,239,9,12,1,13,1,13,1,13,1,13,
        1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,5,14,
        257,8,14,10,14,12,14,260,9,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,1,15,5,15,271,8,15,10,15,12,15,274,9,15,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,3,16,283,8,16,1,17,1,17,3,17,287,8,17,1,18,1,18,1,
        18,3,18,292,8,18,1,18,0,3,24,28,30,19,0,2,4,6,8,10,12,14,16,18,20,
        22,24,26,28,30,32,34,36,0,1,1,0,4,6,316,0,38,1,0,0,0,2,47,1,0,0,
        0,4,65,1,0,0,0,6,83,1,0,0,0,8,87,1,0,0,0,10,89,1,0,0,0,12,115,1,
        0,0,0,14,117,1,0,0,0,16,123,1,0,0,0,18,138,1,0,0,0,20,149,1,0,0,
        0,22,193,1,0,0,0,24,230,1,0,0,0,26,240,1,0,0,0,28,244,1,0,0,0,30,
        261,1,0,0,0,32,282,1,0,0,0,34,286,1,0,0,0,36,291,1,0,0,0,38,42,3,
        2,1,0,39,41,5,38,0,0,40,39,1,0,0,0,41,44,1,0,0,0,42,40,1,0,0,0,42,
        43,1,0,0,0,43,45,1,0,0,0,44,42,1,0,0,0,45,46,5,0,0,1,46,1,1,0,0,
        0,47,48,5,1,0,0,48,52,5,32,0,0,49,51,5,38,0,0,50,49,1,0,0,0,51,54,
        1,0,0,0,52,50,1,0,0,0,52,53,1,0,0,0,53,56,1,0,0,0,54,52,1,0,0,0,
        55,57,3,4,2,0,56,55,1,0,0,0,56,57,1,0,0,0,57,59,1,0,0,0,58,60,5,
        38,0,0,59,58,1,0,0,0,60,61,1,0,0,0,61,59,1,0,0,0,61,62,1,0,0,0,62,
        63,1,0,0,0,63,64,3,10,5,0,64,3,1,0,0,0,65,69,5,2,0,0,66,68,5,38,
        0,0,67,66,1,0,0,0,68,71,1,0,0,0,69,67,1,0,0,0,69,70,1,0,0,0,70,79,
        1,0,0,0,71,69,1,0,0,0,72,76,3,6,3,0,73,75,5,38,0,0,74,73,1,0,0,0,
        75,78,1,0,0,0,76,74,1,0,0,0,76,77,1,0,0,0,77,80,1,0,0,0,78,76,1,
        0,0,0,79,72,1,0,0,0,80,81,1,0,0,0,81,79,1,0,0,0,81,82,1,0,0,0,82,
        5,1,0,0,0,83,84,5,32,0,0,84,85,5,3,0,0,85,86,3,8,4,0,86,7,1,0,0,
        0,87,88,7,0,0,0,88,9,1,0,0,0,89,93,5,7,0,0,90,92,5,38,0,0,91,90,
        1,0,0,0,92,95,1,0,0,0,93,91,1,0,0,0,93,94,1,0,0,0,94,102,1,0,0,0,
        95,93,1,0,0,0,96,98,3,12,6,0,97,99,5,38,0,0,98,97,1,0,0,0,99,100,
        1,0,0,0,100,98,1,0,0,0,100,101,1,0,0,0,101,103,1,0,0,0,102,96,1,
        0,0,0,103,104,1,0,0,0,104,102,1,0,0,0,104,105,1,0,0,0,105,106,1,
        0,0,0,106,107,5,8,0,0,107,11,1,0,0,0,108,116,3,22,11,0,109,116,3,
        26,13,0,110,116,3,10,5,0,111,116,3,16,8,0,112,116,3,18,9,0,113,116,
        3,20,10,0,114,116,3,14,7,0,115,108,1,0,0,0,115,109,1,0,0,0,115,110,
        1,0,0,0,115,111,1,0,0,0,115,112,1,0,0,0,115,113,1,0,0,0,115,114,
        1,0,0,0,116,13,1,0,0,0,117,118,3,24,12,0,118,119,5,9,0,0,119,120,
        3,28,14,0,120,121,5,3,0,0,121,122,3,28,14,0,122,15,1,0,0,0,123,124,
        5,10,0,0,124,125,5,32,0,0,125,126,5,11,0,0,126,127,3,28,14,0,127,
        128,5,12,0,0,128,129,3,28,14,0,129,133,5,13,0,0,130,132,5,38,0,0,
        131,130,1,0,0,0,132,135,1,0,0,0,133,131,1,0,0,0,133,134,1,0,0,0,
        134,136,1,0,0,0,135,133,1,0,0,0,136,137,3,12,6,0,137,17,1,0,0,0,
        138,139,5,14,0,0,139,140,3,24,12,0,140,144,5,13,0,0,141,143,5,38,
        0,0,142,141,1,0,0,0,143,146,1,0,0,0,144,142,1,0,0,0,144,145,1,0,
        0,0,145,147,1,0,0,0,146,144,1,0,0,0,147,148,3,12,6,0,148,19,1,0,
        0,0,149,150,5,15,0,0,150,151,3,28,14,0,151,154,5,16,0,0,152,155,
        3,34,17,0,153,155,5,32,0,0,154,152,1,0,0,0,154,153,1,0,0,0,155,156,
        1,0,0,0,156,160,5,3,0,0,157,159,5,38,0,0,158,157,1,0,0,0,159,162,
        1,0,0,0,160,158,1,0,0,0,160,161,1,0,0,0,161,163,1,0,0,0,162,160,
        1,0,0,0,163,179,3,12,6,0,164,167,5,16,0,0,165,168,3,34,17,0,166,
        168,5,32,0,0,167,165,1,0,0,0,167,166,1,0,0,0,168,169,1,0,0,0,169,
        173,5,3,0,0,170,172,5,38,0,0,171,170,1,0,0,0,172,175,1,0,0,0,173,
        171,1,0,0,0,173,174,1,0,0,0,174,176,1,0,0,0,175,173,1,0,0,0,176,
        178,3,12,6,0,177,164,1,0,0,0,178,181,1,0,0,0,179,177,1,0,0,0,179,
        180,1,0,0,0,180,182,1,0,0,0,181,179,1,0,0,0,182,183,5,17,0,0,183,
        187,5,3,0,0,184,186,5,38,0,0,185,184,1,0,0,0,186,189,1,0,0,0,187,
        185,1,0,0,0,187,188,1,0,0,0,188,190,1,0,0,0,189,187,1,0,0,0,190,
        191,3,12,6,0,191,192,5,18,0,0,192,21,1,0,0,0,193,194,5,19,0,0,194,
        195,3,24,12,0,195,199,5,20,0,0,196,198,5,38,0,0,197,196,1,0,0,0,
        198,201,1,0,0,0,199,197,1,0,0,0,199,200,1,0,0,0,200,202,1,0,0,0,
        201,199,1,0,0,0,202,206,3,12,6,0,203,205,5,38,0,0,204,203,1,0,0,
        0,205,208,1,0,0,0,206,204,1,0,0,0,206,207,1,0,0,0,207,217,1,0,0,
        0,208,206,1,0,0,0,209,213,5,21,0,0,210,212,5,38,0,0,211,210,1,0,
        0,0,212,215,1,0,0,0,213,211,1,0,0,0,213,214,1,0,0,0,214,216,1,0,
        0,0,215,213,1,0,0,0,216,218,3,12,6,0,217,209,1,0,0,0,217,218,1,0,
        0,0,218,23,1,0,0,0,219,220,6,12,-1,0,220,221,3,28,14,0,221,222,5,
        39,0,0,222,223,3,28,14,0,223,231,1,0,0,0,224,225,5,22,0,0,225,226,
        3,24,12,0,226,227,5,23,0,0,227,231,1,0,0,0,228,229,5,24,0,0,229,
        231,3,24,12,1,230,219,1,0,0,0,230,224,1,0,0,0,230,228,1,0,0,0,231,
        237,1,0,0,0,232,233,10,2,0,0,233,234,5,40,0,0,234,236,3,24,12,3,
        235,232,1,0,0,0,236,239,1,0,0,0,237,235,1,0,0,0,237,238,1,0,0,0,
        238,25,1,0,0,0,239,237,1,0,0,0,240,241,5,32,0,0,241,242,5,11,0,0,
        242,243,3,28,14,0,243,27,1,0,0,0,244,245,6,14,-1,0,245,246,3,30,
        15,0,246,258,1,0,0,0,247,248,10,4,0,0,248,249,5,25,0,0,249,257,3,
        30,15,0,250,251,10,3,0,0,251,252,5,26,0,0,252,257,3,30,15,0,253,
        254,10,2,0,0,254,255,5,39,0,0,255,257,3,30,15,0,256,247,1,0,0,0,
        256,250,1,0,0,0,256,253,1,0,0,0,257,260,1,0,0,0,258,256,1,0,0,0,
        258,259,1,0,0,0,259,29,1,0,0,0,260,258,1,0,0,0,261,262,6,15,-1,0,
        262,263,3,32,16,0,263,272,1,0,0,0,264,265,10,3,0,0,265,266,5,27,
        0,0,266,271,3,32,16,0,267,268,10,2,0,0,268,269,5,28,0,0,269,271,
        3,32,16,0,270,264,1,0,0,0,270,267,1,0,0,0,271,274,1,0,0,0,272,270,
        1,0,0,0,272,273,1,0,0,0,273,31,1,0,0,0,274,272,1,0,0,0,275,276,5,
        22,0,0,276,277,3,28,14,0,277,278,5,23,0,0,278,283,1,0,0,0,279,283,
        5,32,0,0,280,283,3,34,17,0,281,283,3,36,18,0,282,275,1,0,0,0,282,
        279,1,0,0,0,282,280,1,0,0,0,282,281,1,0,0,0,283,33,1,0,0,0,284,287,
        5,30,0,0,285,287,5,29,0,0,286,284,1,0,0,0,286,285,1,0,0,0,287,35,
        1,0,0,0,288,292,5,34,0,0,289,292,5,35,0,0,290,292,5,36,0,0,291,288,
        1,0,0,0,291,289,1,0,0,0,291,290,1,0,0,0,292,37,1,0,0,0,32,42,52,
        56,61,69,76,81,93,100,104,115,133,144,154,160,167,173,179,187,199,
        206,213,217,230,237,256,258,270,272,282,286,291
    ]

class AssignmentStatementParser ( Parser ):

    grammarFileName = "AssignmentStatement.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'program'", "'var'", "':'", "'float'", 
                     "'int'", "'string'", "'begin'", "'end'", "'?'", "'for'", 
                     "':='", "'to'", "'do'", "'while'", "'switch'", "'case'", 
                     "'default'", "'endsw'", "'if'", "'then'", "'else'", 
                     "'('", "')'", "'!'", "'+'", "'-'", "'*'", "'/'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'>'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "INT", "FLOAT", "String", "ID", "ARRAY_TYPE", 
                      "INT_ARRAY", "FLOAT_ARRAY", "STRING_ARRAY", "WS", 
                      "NEWLINE", "RELOP", "LOGICOP", "LINE_COMMENT" ]

    RULE_start = 0
    RULE_prog = 1
    RULE_declaration = 2
    RULE_variable_declaration = 3
    RULE_type = 4
    RULE_compoundst = 5
    RULE_statement = 6
    RULE_ternaryoperator = 7
    RULE_forst = 8
    RULE_whilest = 9
    RULE_switchst = 10
    RULE_ifst = 11
    RULE_cond = 12
    RULE_assign = 13
    RULE_expr = 14
    RULE_term = 15
    RULE_factor = 16
    RULE_number = 17
    RULE_array = 18

    ruleNames =  [ "start", "prog", "declaration", "variable_declaration", 
                   "type", "compoundst", "statement", "ternaryoperator", 
                   "forst", "whilest", "switchst", "ifst", "cond", "assign", 
                   "expr", "term", "factor", "number", "array" ]

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
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    INT=29
    FLOAT=30
    String=31
    ID=32
    ARRAY_TYPE=33
    INT_ARRAY=34
    FLOAT_ARRAY=35
    STRING_ARRAY=36
    WS=37
    NEWLINE=38
    RELOP=39
    LOGICOP=40
    LINE_COMMENT=41

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
            self.value_attr = str()
            self.type_attr = str()

        def prog(self):
            return self.getTypedRuleContext(AssignmentStatementParser.ProgContext,0)


        def EOF(self):
            return self.getToken(AssignmentStatementParser.EOF, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(AssignmentStatementParser.NEWLINE)
            else:
                return self.getToken(AssignmentStatementParser.NEWLINE, i)

        def getRuleIndex(self):
            return AssignmentStatementParser.RULE_start

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

        localctx = AssignmentStatementParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.prog()
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==38:
                self.state = 39
                self.match(AssignmentStatementParser.NEWLINE)
                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 45
            self.match(AssignmentStatementParser.EOF)
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
            self.value_attr = str()
            self.type_attr = str()

        def ID(self):
            return self.getToken(AssignmentStatementParser.ID, 0)

        def compoundst(self):
            return self.getTypedRuleContext(AssignmentStatementParser.CompoundstContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(AssignmentStatementParser.NEWLINE)
            else:
                return self.getToken(AssignmentStatementParser.NEWLINE, i)

        def declaration(self):
            return self.getTypedRuleContext(AssignmentStatementParser.DeclarationContext,0)


        def getRuleIndex(self):
            return AssignmentStatementParser.RULE_prog

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

        localctx = AssignmentStatementParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(AssignmentStatementParser.T__0)
            self.state = 48
            self.match(AssignmentStatementParser.ID)
            self.state = 52
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 49
                    self.match(AssignmentStatementParser.NEWLINE) 
                self.state = 54
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 55
                self.declaration()


            self.state = 59 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 58
                self.match(AssignmentStatementParser.NEWLINE)
                self.state = 61 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==38):
                    break

            self.state = 63
            self.compoundst()
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
            self.value_attr = str()
            self.type_attr = str()

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(AssignmentStatementParser.NEWLINE)
            else:
                return self.getToken(AssignmentStatementParser.NEWLINE, i)

        def variable_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AssignmentStatementParser.Variable_declarationContext)
            else:
                return self.getTypedRuleContext(AssignmentStatementParser.Variable_declarationContext,i)


        def getRuleIndex(self):
            return AssignmentStatementParser.RULE_declaration

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

        localctx = AssignmentStatementParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(AssignmentStatementParser.T__1)
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==38:
                self.state = 66
                self.match(AssignmentStatementParser.NEWLINE)
                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 79 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 72
                self.variable_declaration()
                self.state = 76
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 73
                        self.match(AssignmentStatementParser.NEWLINE) 
                    self.state = 78
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

                self.state = 81 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==32):
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
            self.value_attr = str()
            self.type_attr = str()

        def ID(self):
            return self.getToken(AssignmentStatementParser.ID, 0)

        def type_(self):
            return self.getTypedRuleContext(AssignmentStatementParser.TypeContext,0)


        def getRuleIndex(self):
            return AssignmentStatementParser.RULE_variable_declaration

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

        localctx = AssignmentStatementParser.Variable_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_variable_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(AssignmentStatementParser.ID)
            self.state = 84
            self.match(AssignmentStatementParser.T__2)
            self.state = 85
            self.type_()
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
            self.value_attr = str()
            self.type_attr = str()


        def getRuleIndex(self):
            return AssignmentStatementParser.RULE_type

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

        localctx = AssignmentStatementParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 112) != 0)):
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


    class CompoundstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(AssignmentStatementParser.NEWLINE)
            else:
                return self.getToken(AssignmentStatementParser.NEWLINE, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AssignmentStatementParser.StatementContext)
            else:
                return self.getTypedRuleContext(AssignmentStatementParser.StatementContext,i)


        def getRuleIndex(self):
            return AssignmentStatementParser.RULE_compoundst

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

        localctx = AssignmentStatementParser.CompoundstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_compoundst)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(AssignmentStatementParser.T__6)
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==38:
                self.state = 90
                self.match(AssignmentStatementParser.NEWLINE)
                self.state = 95
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 102 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 96
                self.statement()
                self.state = 98 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 97
                    self.match(AssignmentStatementParser.NEWLINE)
                    self.state = 100 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==38):
                        break

                self.state = 104 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 126186210432) != 0)):
                    break

            self.state = 106
            self.match(AssignmentStatementParser.T__7)
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
            self.value_attr = str()
            self.type_attr = str()

        def ifst(self):
            return self.getTypedRuleContext(AssignmentStatementParser.IfstContext,0)


        def assign(self):
            return self.getTypedRuleContext(AssignmentStatementParser.AssignContext,0)


        def compoundst(self):
            return self.getTypedRuleContext(AssignmentStatementParser.CompoundstContext,0)


        def forst(self):
            return self.getTypedRuleContext(AssignmentStatementParser.ForstContext,0)


        def whilest(self):
            return self.getTypedRuleContext(AssignmentStatementParser.WhilestContext,0)


        def switchst(self):
            return self.getTypedRuleContext(AssignmentStatementParser.SwitchstContext,0)


        def ternaryoperator(self):
            return self.getTypedRuleContext(AssignmentStatementParser.TernaryoperatorContext,0)


        def getRuleIndex(self):
            return AssignmentStatementParser.RULE_statement

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

        localctx = AssignmentStatementParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_statement)
        try:
            self.state = 115
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 108
                self.ifst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 109
                self.assign()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 110
                self.compoundst()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 111
                self.forst()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 112
                self.whilest()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 113
                self.switchst()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 114
                self.ternaryoperator()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TernaryoperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()

        def cond(self):
            return self.getTypedRuleContext(AssignmentStatementParser.CondContext,0)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AssignmentStatementParser.ExprContext)
            else:
                return self.getTypedRuleContext(AssignmentStatementParser.ExprContext,i)


        def getRuleIndex(self):
            return AssignmentStatementParser.RULE_ternaryoperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTernaryoperator" ):
                listener.enterTernaryoperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTernaryoperator" ):
                listener.exitTernaryoperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTernaryoperator" ):
                return visitor.visitTernaryoperator(self)
            else:
                return visitor.visitChildren(self)




    def ternaryoperator(self):

        localctx = AssignmentStatementParser.TernaryoperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_ternaryoperator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.cond(0)
            self.state = 118
            self.match(AssignmentStatementParser.T__8)
            self.state = 119
            self.expr(0)
            self.state = 120
            self.match(AssignmentStatementParser.T__2)
            self.state = 121
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()

        def ID(self):
            return self.getToken(AssignmentStatementParser.ID, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AssignmentStatementParser.ExprContext)
            else:
                return self.getTypedRuleContext(AssignmentStatementParser.ExprContext,i)


        def statement(self):
            return self.getTypedRuleContext(AssignmentStatementParser.StatementContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(AssignmentStatementParser.NEWLINE)
            else:
                return self.getToken(AssignmentStatementParser.NEWLINE, i)

        def getRuleIndex(self):
            return AssignmentStatementParser.RULE_forst

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForst" ):
                listener.enterForst(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForst" ):
                listener.exitForst(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForst" ):
                return visitor.visitForst(self)
            else:
                return visitor.visitChildren(self)




    def forst(self):

        localctx = AssignmentStatementParser.ForstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_forst)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(AssignmentStatementParser.T__9)
            self.state = 124
            self.match(AssignmentStatementParser.ID)
            self.state = 125
            self.match(AssignmentStatementParser.T__10)
            self.state = 126
            self.expr(0)
            self.state = 127
            self.match(AssignmentStatementParser.T__11)
            self.state = 128
            self.expr(0)
            self.state = 129
            self.match(AssignmentStatementParser.T__12)
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==38:
                self.state = 130
                self.match(AssignmentStatementParser.NEWLINE)
                self.state = 135
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 136
            self.statement()
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
            self.value_attr = str()
            self.type_attr = str()

        def cond(self):
            return self.getTypedRuleContext(AssignmentStatementParser.CondContext,0)


        def statement(self):
            return self.getTypedRuleContext(AssignmentStatementParser.StatementContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(AssignmentStatementParser.NEWLINE)
            else:
                return self.getToken(AssignmentStatementParser.NEWLINE, i)

        def getRuleIndex(self):
            return AssignmentStatementParser.RULE_whilest

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

        localctx = AssignmentStatementParser.WhilestContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_whilest)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.match(AssignmentStatementParser.T__13)
            self.state = 139
            self.cond(0)
            self.state = 140
            self.match(AssignmentStatementParser.T__12)
            self.state = 144
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==38:
                self.state = 141
                self.match(AssignmentStatementParser.NEWLINE)
                self.state = 146
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 147
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()

        def expr(self):
            return self.getTypedRuleContext(AssignmentStatementParser.ExprContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AssignmentStatementParser.StatementContext)
            else:
                return self.getTypedRuleContext(AssignmentStatementParser.StatementContext,i)


        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AssignmentStatementParser.NumberContext)
            else:
                return self.getTypedRuleContext(AssignmentStatementParser.NumberContext,i)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(AssignmentStatementParser.ID)
            else:
                return self.getToken(AssignmentStatementParser.ID, i)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(AssignmentStatementParser.NEWLINE)
            else:
                return self.getToken(AssignmentStatementParser.NEWLINE, i)

        def getRuleIndex(self):
            return AssignmentStatementParser.RULE_switchst

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitchst" ):
                listener.enterSwitchst(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitchst" ):
                listener.exitSwitchst(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSwitchst" ):
                return visitor.visitSwitchst(self)
            else:
                return visitor.visitChildren(self)




    def switchst(self):

        localctx = AssignmentStatementParser.SwitchstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_switchst)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(AssignmentStatementParser.T__14)
            self.state = 150
            self.expr(0)
            self.state = 151
            self.match(AssignmentStatementParser.T__15)
            self.state = 154
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [29, 30]:
                self.state = 152
                self.number()
                pass
            elif token in [32]:
                self.state = 153
                self.match(AssignmentStatementParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 156
            self.match(AssignmentStatementParser.T__2)
            self.state = 160
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==38:
                self.state = 157
                self.match(AssignmentStatementParser.NEWLINE)
                self.state = 162
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 163
            self.statement()
            self.state = 179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 164
                self.match(AssignmentStatementParser.T__15)
                self.state = 167
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [29, 30]:
                    self.state = 165
                    self.number()
                    pass
                elif token in [32]:
                    self.state = 166
                    self.match(AssignmentStatementParser.ID)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 169
                self.match(AssignmentStatementParser.T__2)
                self.state = 173
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==38:
                    self.state = 170
                    self.match(AssignmentStatementParser.NEWLINE)
                    self.state = 175
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 176
                self.statement()
                self.state = 181
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 182
            self.match(AssignmentStatementParser.T__16)
            self.state = 183
            self.match(AssignmentStatementParser.T__2)
            self.state = 187
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==38:
                self.state = 184
                self.match(AssignmentStatementParser.NEWLINE)
                self.state = 189
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 190
            self.statement()
            self.state = 191
            self.match(AssignmentStatementParser.T__17)
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
            self.value_attr = str()
            self.type_attr = str()

        def cond(self):
            return self.getTypedRuleContext(AssignmentStatementParser.CondContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AssignmentStatementParser.StatementContext)
            else:
                return self.getTypedRuleContext(AssignmentStatementParser.StatementContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(AssignmentStatementParser.NEWLINE)
            else:
                return self.getToken(AssignmentStatementParser.NEWLINE, i)

        def getRuleIndex(self):
            return AssignmentStatementParser.RULE_ifst

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

        localctx = AssignmentStatementParser.IfstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_ifst)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.match(AssignmentStatementParser.T__18)
            self.state = 194
            self.cond(0)
            self.state = 195
            self.match(AssignmentStatementParser.T__19)
            self.state = 199
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==38:
                self.state = 196
                self.match(AssignmentStatementParser.NEWLINE)
                self.state = 201
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 202
            self.statement()
            self.state = 206
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 203
                    self.match(AssignmentStatementParser.NEWLINE) 
                self.state = 208
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

            self.state = 217
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 209
                self.match(AssignmentStatementParser.T__20)
                self.state = 213
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==38:
                    self.state = 210
                    self.match(AssignmentStatementParser.NEWLINE)
                    self.state = 215
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 216
                self.statement()


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
            self.value_attr = str()
            self.type_attr = str()

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AssignmentStatementParser.ExprContext)
            else:
                return self.getTypedRuleContext(AssignmentStatementParser.ExprContext,i)


        def RELOP(self):
            return self.getToken(AssignmentStatementParser.RELOP, 0)

        def cond(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AssignmentStatementParser.CondContext)
            else:
                return self.getTypedRuleContext(AssignmentStatementParser.CondContext,i)


        def LOGICOP(self):
            return self.getToken(AssignmentStatementParser.LOGICOP, 0)

        def getRuleIndex(self):
            return AssignmentStatementParser.RULE_cond

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
        localctx = AssignmentStatementParser.CondContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_cond, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 220
                self.expr(0)
                self.state = 221
                self.match(AssignmentStatementParser.RELOP)
                self.state = 222
                self.expr(0)
                pass

            elif la_ == 2:
                self.state = 224
                self.match(AssignmentStatementParser.T__21)
                self.state = 225
                self.cond(0)
                self.state = 226
                self.match(AssignmentStatementParser.T__22)
                pass

            elif la_ == 3:
                self.state = 228
                self.match(AssignmentStatementParser.T__23)
                self.state = 229
                self.cond(1)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 237
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = AssignmentStatementParser.CondContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_cond)
                    self.state = 232
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 233
                    self.match(AssignmentStatementParser.LOGICOP)
                    self.state = 234
                    self.cond(3) 
                self.state = 239
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

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
            self.value_attr = str()
            self.type_attr = str()

        def ID(self):
            return self.getToken(AssignmentStatementParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(AssignmentStatementParser.ExprContext,0)


        def getRuleIndex(self):
            return AssignmentStatementParser.RULE_assign

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

        localctx = AssignmentStatementParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.match(AssignmentStatementParser.ID)
            self.state = 241
            self.match(AssignmentStatementParser.T__10)
            self.state = 242
            self.expr(0)
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
            self.value_attr = str()
            self.type_attr = str()


        def getRuleIndex(self):
            return AssignmentStatementParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.value_attr = ctx.value_attr
            self.type_attr = ctx.type_attr


    class Expr_term_minusContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AssignmentStatementParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(AssignmentStatementParser.ExprContext,0)

        def term(self):
            return self.getTypedRuleContext(AssignmentStatementParser.TermContext,0)


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

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AssignmentStatementParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(AssignmentStatementParser.ExprContext,0)

        def term(self):
            return self.getTypedRuleContext(AssignmentStatementParser.TermContext,0)


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

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AssignmentStatementParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(AssignmentStatementParser.TermContext,0)


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

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AssignmentStatementParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(AssignmentStatementParser.ExprContext,0)

        def RELOP(self):
            return self.getToken(AssignmentStatementParser.RELOP, 0)
        def term(self):
            return self.getTypedRuleContext(AssignmentStatementParser.TermContext,0)


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
        localctx = AssignmentStatementParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = AssignmentStatementParser.Term4Context(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 245
            self.term(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 258
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 256
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
                    if la_ == 1:
                        localctx = AssignmentStatementParser.Expr_term_plusContext(self, AssignmentStatementParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 247
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 248
                        self.match(AssignmentStatementParser.T__24)
                        self.state = 249
                        self.term(0)
                        pass

                    elif la_ == 2:
                        localctx = AssignmentStatementParser.Expr_term_minusContext(self, AssignmentStatementParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 250
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 251
                        self.match(AssignmentStatementParser.T__25)
                        self.state = 252
                        self.term(0)
                        pass

                    elif la_ == 3:
                        localctx = AssignmentStatementParser.Expr_term_relopContext(self, AssignmentStatementParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 253
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 254
                        self.match(AssignmentStatementParser.RELOP)
                        self.state = 255
                        self.term(0)
                        pass

             
                self.state = 260
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

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
            self.value_attr = str()
            self.type_attr = str()


        def getRuleIndex(self):
            return AssignmentStatementParser.RULE_term

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.value_attr = ctx.value_attr
            self.type_attr = ctx.type_attr


    class Term_fact_divideContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AssignmentStatementParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(AssignmentStatementParser.TermContext,0)

        def factor(self):
            return self.getTypedRuleContext(AssignmentStatementParser.FactorContext,0)


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

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AssignmentStatementParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(AssignmentStatementParser.TermContext,0)

        def factor(self):
            return self.getTypedRuleContext(AssignmentStatementParser.FactorContext,0)


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

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AssignmentStatementParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def factor(self):
            return self.getTypedRuleContext(AssignmentStatementParser.FactorContext,0)


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
        localctx = AssignmentStatementParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_term, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = AssignmentStatementParser.Factor3Context(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 262
            self.factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 272
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 270
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                    if la_ == 1:
                        localctx = AssignmentStatementParser.Term_fact_mutiplyContext(self, AssignmentStatementParser.TermContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 264
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 265
                        self.match(AssignmentStatementParser.T__26)
                        self.state = 266
                        self.factor()
                        pass

                    elif la_ == 2:
                        localctx = AssignmentStatementParser.Term_fact_divideContext(self, AssignmentStatementParser.TermContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 267
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 268
                        self.match(AssignmentStatementParser.T__27)
                        self.state = 269
                        self.factor()
                        pass

             
                self.state = 274
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

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
            self.value_attr = str()
            self.type_attr = str()


        def getRuleIndex(self):
            return AssignmentStatementParser.RULE_factor

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.value_attr = ctx.value_attr
            self.type_attr = ctx.type_attr



    class Fact_exprContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AssignmentStatementParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(AssignmentStatementParser.ExprContext,0)


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

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AssignmentStatementParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(AssignmentStatementParser.ID, 0)

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


    class Fact_numberContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AssignmentStatementParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def number(self):
            return self.getTypedRuleContext(AssignmentStatementParser.NumberContext,0)


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


    class Fact_arrayContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AssignmentStatementParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def array(self):
            return self.getTypedRuleContext(AssignmentStatementParser.ArrayContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFact_array" ):
                listener.enterFact_array(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFact_array" ):
                listener.exitFact_array(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFact_array" ):
                return visitor.visitFact_array(self)
            else:
                return visitor.visitChildren(self)



    def factor(self):

        localctx = AssignmentStatementParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_factor)
        try:
            self.state = 282
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                localctx = AssignmentStatementParser.Fact_exprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 275
                self.match(AssignmentStatementParser.T__21)
                self.state = 276
                self.expr(0)
                self.state = 277
                self.match(AssignmentStatementParser.T__22)
                pass
            elif token in [32]:
                localctx = AssignmentStatementParser.Fact_idContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 279
                self.match(AssignmentStatementParser.ID)
                pass
            elif token in [29, 30]:
                localctx = AssignmentStatementParser.Fact_numberContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 280
                self.number()
                pass
            elif token in [34, 35, 36]:
                localctx = AssignmentStatementParser.Fact_arrayContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 281
                self.array()
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
            self.value_attr = str()
            self.type_attr = str()


        def getRuleIndex(self):
            return AssignmentStatementParser.RULE_number

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.value_attr = ctx.value_attr
            self.type_attr = ctx.type_attr



    class Number_floatContext(NumberContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AssignmentStatementParser.NumberContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(AssignmentStatementParser.FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber_float" ):
                listener.enterNumber_float(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber_float" ):
                listener.exitNumber_float(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber_float" ):
                return visitor.visitNumber_float(self)
            else:
                return visitor.visitChildren(self)


    class Number_intContext(NumberContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AssignmentStatementParser.NumberContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(AssignmentStatementParser.INT, 0)

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

        localctx = AssignmentStatementParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_number)
        try:
            self.state = 286
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [30]:
                localctx = AssignmentStatementParser.Number_floatContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 284
                self.match(AssignmentStatementParser.FLOAT)
                pass
            elif token in [29]:
                localctx = AssignmentStatementParser.Number_intContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 285
                self.match(AssignmentStatementParser.INT)
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


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()


        def getRuleIndex(self):
            return AssignmentStatementParser.RULE_array

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.value_attr = ctx.value_attr
            self.type_attr = ctx.type_attr



    class Array_floatContext(ArrayContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AssignmentStatementParser.ArrayContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT_ARRAY(self):
            return self.getToken(AssignmentStatementParser.FLOAT_ARRAY, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray_float" ):
                listener.enterArray_float(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray_float" ):
                listener.exitArray_float(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_float" ):
                return visitor.visitArray_float(self)
            else:
                return visitor.visitChildren(self)


    class Array_stringContext(ArrayContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AssignmentStatementParser.ArrayContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING_ARRAY(self):
            return self.getToken(AssignmentStatementParser.STRING_ARRAY, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray_string" ):
                listener.enterArray_string(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray_string" ):
                listener.exitArray_string(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_string" ):
                return visitor.visitArray_string(self)
            else:
                return visitor.visitChildren(self)


    class Array_intContext(ArrayContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AssignmentStatementParser.ArrayContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT_ARRAY(self):
            return self.getToken(AssignmentStatementParser.INT_ARRAY, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray_int" ):
                listener.enterArray_int(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray_int" ):
                listener.exitArray_int(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_int" ):
                return visitor.visitArray_int(self)
            else:
                return visitor.visitChildren(self)



    def array(self):

        localctx = AssignmentStatementParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_array)
        try:
            self.state = 291
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34]:
                localctx = AssignmentStatementParser.Array_intContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 288
                self.match(AssignmentStatementParser.INT_ARRAY)
                pass
            elif token in [35]:
                localctx = AssignmentStatementParser.Array_floatContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 289
                self.match(AssignmentStatementParser.FLOAT_ARRAY)
                pass
            elif token in [36]:
                localctx = AssignmentStatementParser.Array_stringContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 290
                self.match(AssignmentStatementParser.STRING_ARRAY)
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[12] = self.cond_sempred
        self._predicates[14] = self.expr_sempred
        self._predicates[15] = self.term_sempred
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
         




