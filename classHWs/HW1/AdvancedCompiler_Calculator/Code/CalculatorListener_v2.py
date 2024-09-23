# new version with attributed grammars

from antlr4 import *
from Gen.ArithmeticLexer import ArithmeticLexer
from Gen.ArithmeticListener import ArithmeticListener
from Gen.ArithmeticParser import ArithmeticParser
from antlr4 import *
from Gen.ArithmeticLexer import ArithmeticLexer
from Gen.ArithmeticListener import ArithmeticListener
from Gen.ArithmeticParser import ArithmeticParser

class CalculatorListener(ArithmeticListener):

    def init(self):
        self.result = 0

    def exitExpr(self, ctx:ArithmeticParser.ExprContext):
        if ctx.getChildCount() == 1:
            ctx.value = ctx.getChild(0).value
            self.result = ctx.value
            # return ctx.getChild(0).value
        else: # term ((ADD | SUB) term)*
            result = ctx.getChild(0).value
            len = ctx.getChildCount() - 1
            for i in range(1, len, 2): # calculate from left to right
                op = ctx.getChild(i).getText()
                if (op == '+'):
                    # value = self.exitTerm(ctx.getChild(i+1)) # first method
                    value = ctx.getChild(i+1).value # second method
                    result = result + value
                elif (op == '-'):
                    # value = self.exitTerm(ctx.getChild(i+1)) # first method
                    value = ctx.getChild(i + 1).value # second method
                    result = result - value
            self.result = result
            ctx.value = result
            # return self.result


    def exitTerm(self, ctx:ArithmeticParser.TermContext):
        if ctx.getChildCount() == 1:
            # return ctx.getChild(0).value
            ctx.value = ctx.getChild(0).value
        else:
            # result = self.exitFactor(ctx.getChild(0))
            result = ctx.getChild(0).value
            len = ctx.getChildCount() - 1
            for i in range(1, len, 2): # factor ((MUL | DIV) factor)*
                op = ctx.getChild(i).getText()
                if (op == '*'):
                    # value = self.exitFactor(ctx.getChild(i + 1)) # first method
                    value = ctx.getChild(i + 1).value # second method
                    result = result * value
                elif (op == '/'):
                    # value = self.exitFactor(ctx.getChild(i + 1)) # first method
                    value = ctx.getChild(i + 1).value # second method
                    result = result / value
            # self.result = result
            ctx.value = result
            # return self.result

    def exitFactor(self, ctx:ArithmeticParser.FactorContext):
        if ctx.getChildCount() == 1: # NUMBER
            ctx.value = float(ctx.NUMBER().getText()) # first method
            # ctx.value = float(ctx.getChild(0).getText())

            # return ctx.value # second method
        else: # LPAREN expr RPAREN
            # return self.exitExpr(ctx.getChild(1))
            ctx.value = ctx.getChild(1).value # ( term ) # first method
            # ctx.value = ctx.expr()

            # return ctx.value # second method

## previous version without attributed grammers
#
# from antlr4 import *
# from Gen.ArithmeticLexer import ArithmeticLexer
# from Gen.ArithmeticListener import ArithmeticListener
# from Gen.ArithmeticParser import ArithmeticParser
#
# class CalculatorListener(ArithmeticListener):
#
#     def __init__(self):
#         self.result = 0
#
# # Expression:
#     def exitExpr(self, ctx:ArithmeticParser.ExprContext):
#         if ctx.getChildCount() == 1:
#             return self.exitTerm(ctx.getChild(0))
#         else:
#             result = self.exitTerm(ctx.getChild(0))
#             len = ctx.getChildCount()-1
#             for i in range(1,len,2):
#                 op = ctx.getChild(i).getText()
#                 if (op == '+'):
#                     value = self.exitTerm(ctx.getChild(i+1))
#                     result = result + value
#                 elif (op == '-'):
#                     value = self.exitTerm(ctx.getChild(i+1))
#                     result = result - value
#             self.result = result
#             return self.result
#
# # Term:
#     def exitTerm(self, ctx:ArithmeticParser.TermContext):
#         if ctx.getChildCount() == 1:
#             return self.exitFactor(ctx.getChild(0))
#         else:
#             result = self.exitFactor(ctx.getChild(0))
#             len = ctx.getChildCount() - 1
#             for i in range(1, len, 2):
#                 op = ctx.getChild(i).getText()
#                 if (op == '*'):
#                     value = self.exitFactor(ctx.getChild(i + 1))
#                     result = result * value
#                 elif (op == '/'):
#                     value = self.exitFactor(ctx.getChild(i + 1))
#                     result = result / value
#             self.result = result
#             return self.result
#
#     def exitFactor(self, ctx:ArithmeticParser.FactorContext):
#         if ctx.getChildCount() == 1:
#             return float(ctx.NUMBER().getText())
#         else:
#             return self.exitExpr(ctx.getChild(1))
