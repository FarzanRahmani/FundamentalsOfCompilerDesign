# Generated from E:/uni/7th term/fundamentals of compiler design/HWs/HW3/chaloosOotagh.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .chaloosOotaghParser import chaloosOotaghParser
else:
    from chaloosOotaghParser import chaloosOotaghParser

# This class defines a complete generic visitor for a parse tree produced by chaloosOotaghParser.

class chaloosOotaghVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by chaloosOotaghParser#start.
    def visitStart(self, ctx:chaloosOotaghParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by chaloosOotaghParser#prog.
    def visitProg(self, ctx:chaloosOotaghParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by chaloosOotaghParser#declaration.
    def visitDeclaration(self, ctx:chaloosOotaghParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by chaloosOotaghParser#variable_declaration.
    def visitVariable_declaration(self, ctx:chaloosOotaghParser.Variable_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by chaloosOotaghParser#type.
    def visitType(self, ctx:chaloosOotaghParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by chaloosOotaghParser#statement.
    def visitStatement(self, ctx:chaloosOotaghParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by chaloosOotaghParser#compoundst.
    def visitCompoundst(self, ctx:chaloosOotaghParser.CompoundstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by chaloosOotaghParser#whilest.
    def visitWhilest(self, ctx:chaloosOotaghParser.WhilestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by chaloosOotaghParser#ifst.
    def visitIfst(self, ctx:chaloosOotaghParser.IfstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by chaloosOotaghParser#cond.
    def visitCond(self, ctx:chaloosOotaghParser.CondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by chaloosOotaghParser#assign.
    def visitAssign(self, ctx:chaloosOotaghParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by chaloosOotaghParser#expr_term_minus.
    def visitExpr_term_minus(self, ctx:chaloosOotaghParser.Expr_term_minusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by chaloosOotaghParser#expr_term_plus.
    def visitExpr_term_plus(self, ctx:chaloosOotaghParser.Expr_term_plusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by chaloosOotaghParser#term4.
    def visitTerm4(self, ctx:chaloosOotaghParser.Term4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by chaloosOotaghParser#expr_term_relop.
    def visitExpr_term_relop(self, ctx:chaloosOotaghParser.Expr_term_relopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by chaloosOotaghParser#term_fact_divide.
    def visitTerm_fact_divide(self, ctx:chaloosOotaghParser.Term_fact_divideContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by chaloosOotaghParser#term_fact_mutiply.
    def visitTerm_fact_mutiply(self, ctx:chaloosOotaghParser.Term_fact_mutiplyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by chaloosOotaghParser#factor3.
    def visitFactor3(self, ctx:chaloosOotaghParser.Factor3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by chaloosOotaghParser#fact_expr.
    def visitFact_expr(self, ctx:chaloosOotaghParser.Fact_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by chaloosOotaghParser#fact_id.
    def visitFact_id(self, ctx:chaloosOotaghParser.Fact_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by chaloosOotaghParser#fact_number.
    def visitFact_number(self, ctx:chaloosOotaghParser.Fact_numberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by chaloosOotaghParser#fact_boolean.
    def visitFact_boolean(self, ctx:chaloosOotaghParser.Fact_booleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by chaloosOotaghParser#number_int.
    def visitNumber_int(self, ctx:chaloosOotaghParser.Number_intContext):
        return self.visitChildren(ctx)



del chaloosOotaghParser