# Generated from E:/uni/7th term/fundamentals of compiler design/HWs/HW3/chaloosOotagh.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .chaloosOotaghParser import chaloosOotaghParser
else:
    from chaloosOotaghParser import chaloosOotaghParser

# This class defines a complete listener for a parse tree produced by chaloosOotaghParser.
class chaloosOotaghListener(ParseTreeListener):

    # Enter a parse tree produced by chaloosOotaghParser#start.
    def enterStart(self, ctx:chaloosOotaghParser.StartContext):
        pass

    # Exit a parse tree produced by chaloosOotaghParser#start.
    def exitStart(self, ctx:chaloosOotaghParser.StartContext):
        pass


    # Enter a parse tree produced by chaloosOotaghParser#prog.
    def enterProg(self, ctx:chaloosOotaghParser.ProgContext):
        pass

    # Exit a parse tree produced by chaloosOotaghParser#prog.
    def exitProg(self, ctx:chaloosOotaghParser.ProgContext):
        pass


    # Enter a parse tree produced by chaloosOotaghParser#declaration.
    def enterDeclaration(self, ctx:chaloosOotaghParser.DeclarationContext):
        pass

    # Exit a parse tree produced by chaloosOotaghParser#declaration.
    def exitDeclaration(self, ctx:chaloosOotaghParser.DeclarationContext):
        pass


    # Enter a parse tree produced by chaloosOotaghParser#variable_declaration.
    def enterVariable_declaration(self, ctx:chaloosOotaghParser.Variable_declarationContext):
        pass

    # Exit a parse tree produced by chaloosOotaghParser#variable_declaration.
    def exitVariable_declaration(self, ctx:chaloosOotaghParser.Variable_declarationContext):
        pass


    # Enter a parse tree produced by chaloosOotaghParser#type.
    def enterType(self, ctx:chaloosOotaghParser.TypeContext):
        pass

    # Exit a parse tree produced by chaloosOotaghParser#type.
    def exitType(self, ctx:chaloosOotaghParser.TypeContext):
        pass


    # Enter a parse tree produced by chaloosOotaghParser#statement.
    def enterStatement(self, ctx:chaloosOotaghParser.StatementContext):
        pass

    # Exit a parse tree produced by chaloosOotaghParser#statement.
    def exitStatement(self, ctx:chaloosOotaghParser.StatementContext):
        pass


    # Enter a parse tree produced by chaloosOotaghParser#compoundst.
    def enterCompoundst(self, ctx:chaloosOotaghParser.CompoundstContext):
        pass

    # Exit a parse tree produced by chaloosOotaghParser#compoundst.
    def exitCompoundst(self, ctx:chaloosOotaghParser.CompoundstContext):
        pass


    # Enter a parse tree produced by chaloosOotaghParser#whilest.
    def enterWhilest(self, ctx:chaloosOotaghParser.WhilestContext):
        pass

    # Exit a parse tree produced by chaloosOotaghParser#whilest.
    def exitWhilest(self, ctx:chaloosOotaghParser.WhilestContext):
        pass


    # Enter a parse tree produced by chaloosOotaghParser#ifst.
    def enterIfst(self, ctx:chaloosOotaghParser.IfstContext):
        pass

    # Exit a parse tree produced by chaloosOotaghParser#ifst.
    def exitIfst(self, ctx:chaloosOotaghParser.IfstContext):
        pass


    # Enter a parse tree produced by chaloosOotaghParser#cond.
    def enterCond(self, ctx:chaloosOotaghParser.CondContext):
        pass

    # Exit a parse tree produced by chaloosOotaghParser#cond.
    def exitCond(self, ctx:chaloosOotaghParser.CondContext):
        pass


    # Enter a parse tree produced by chaloosOotaghParser#assign.
    def enterAssign(self, ctx:chaloosOotaghParser.AssignContext):
        pass

    # Exit a parse tree produced by chaloosOotaghParser#assign.
    def exitAssign(self, ctx:chaloosOotaghParser.AssignContext):
        pass


    # Enter a parse tree produced by chaloosOotaghParser#expr_term_minus.
    def enterExpr_term_minus(self, ctx:chaloosOotaghParser.Expr_term_minusContext):
        pass

    # Exit a parse tree produced by chaloosOotaghParser#expr_term_minus.
    def exitExpr_term_minus(self, ctx:chaloosOotaghParser.Expr_term_minusContext):
        pass


    # Enter a parse tree produced by chaloosOotaghParser#expr_term_plus.
    def enterExpr_term_plus(self, ctx:chaloosOotaghParser.Expr_term_plusContext):
        pass

    # Exit a parse tree produced by chaloosOotaghParser#expr_term_plus.
    def exitExpr_term_plus(self, ctx:chaloosOotaghParser.Expr_term_plusContext):
        pass


    # Enter a parse tree produced by chaloosOotaghParser#term4.
    def enterTerm4(self, ctx:chaloosOotaghParser.Term4Context):
        pass

    # Exit a parse tree produced by chaloosOotaghParser#term4.
    def exitTerm4(self, ctx:chaloosOotaghParser.Term4Context):
        pass


    # Enter a parse tree produced by chaloosOotaghParser#expr_term_relop.
    def enterExpr_term_relop(self, ctx:chaloosOotaghParser.Expr_term_relopContext):
        pass

    # Exit a parse tree produced by chaloosOotaghParser#expr_term_relop.
    def exitExpr_term_relop(self, ctx:chaloosOotaghParser.Expr_term_relopContext):
        pass


    # Enter a parse tree produced by chaloosOotaghParser#term_fact_divide.
    def enterTerm_fact_divide(self, ctx:chaloosOotaghParser.Term_fact_divideContext):
        pass

    # Exit a parse tree produced by chaloosOotaghParser#term_fact_divide.
    def exitTerm_fact_divide(self, ctx:chaloosOotaghParser.Term_fact_divideContext):
        pass


    # Enter a parse tree produced by chaloosOotaghParser#term_fact_mutiply.
    def enterTerm_fact_mutiply(self, ctx:chaloosOotaghParser.Term_fact_mutiplyContext):
        pass

    # Exit a parse tree produced by chaloosOotaghParser#term_fact_mutiply.
    def exitTerm_fact_mutiply(self, ctx:chaloosOotaghParser.Term_fact_mutiplyContext):
        pass


    # Enter a parse tree produced by chaloosOotaghParser#factor3.
    def enterFactor3(self, ctx:chaloosOotaghParser.Factor3Context):
        pass

    # Exit a parse tree produced by chaloosOotaghParser#factor3.
    def exitFactor3(self, ctx:chaloosOotaghParser.Factor3Context):
        pass


    # Enter a parse tree produced by chaloosOotaghParser#fact_expr.
    def enterFact_expr(self, ctx:chaloosOotaghParser.Fact_exprContext):
        pass

    # Exit a parse tree produced by chaloosOotaghParser#fact_expr.
    def exitFact_expr(self, ctx:chaloosOotaghParser.Fact_exprContext):
        pass


    # Enter a parse tree produced by chaloosOotaghParser#fact_id.
    def enterFact_id(self, ctx:chaloosOotaghParser.Fact_idContext):
        pass

    # Exit a parse tree produced by chaloosOotaghParser#fact_id.
    def exitFact_id(self, ctx:chaloosOotaghParser.Fact_idContext):
        pass


    # Enter a parse tree produced by chaloosOotaghParser#fact_number.
    def enterFact_number(self, ctx:chaloosOotaghParser.Fact_numberContext):
        pass

    # Exit a parse tree produced by chaloosOotaghParser#fact_number.
    def exitFact_number(self, ctx:chaloosOotaghParser.Fact_numberContext):
        pass


    # Enter a parse tree produced by chaloosOotaghParser#fact_boolean.
    def enterFact_boolean(self, ctx:chaloosOotaghParser.Fact_booleanContext):
        pass

    # Exit a parse tree produced by chaloosOotaghParser#fact_boolean.
    def exitFact_boolean(self, ctx:chaloosOotaghParser.Fact_booleanContext):
        pass


    # Enter a parse tree produced by chaloosOotaghParser#number_int.
    def enterNumber_int(self, ctx:chaloosOotaghParser.Number_intContext):
        pass

    # Exit a parse tree produced by chaloosOotaghParser#number_int.
    def exitNumber_int(self, ctx:chaloosOotaghParser.Number_intContext):
        pass



del chaloosOotaghParser