import queue
import networkx as nx
from Gen.AssignmentStatementListener import AssignmentStatementListener
from Gen.AssignmentStatementParser import AssignmentStatementParser


class ASTListener(AssignmentStatementListener):
    def __init__(self):
        self.ast = AST()  # Data structure for holding the abstract syntax tree
        self.q = queue.Queue()  # Use to print and visualize InClassPresentation
        self.g = nx.DiGraph()  # Use to visualize InClassPresentation

    def print_tree(self, node=None, level=1):
        if node is None:
            # print()
            return

        print()
        while node is not None:
            current_node = node
            print(current_node.value, end='')
            if node.child is not None:
                self.g.add_edge(current_node, node.child, edge_type='C', color='red', weight=4)
                self.q.put(node.child)
            else:
                tn = TreeNode(value='▓', child=None, brother=None)
                self.g.add_edge(current_node, tn, edge_type='C', color='red', weight=4)
            node = node.brother
            if node is not None:
                print('\t───\t', end='')
                self.g.add_edge(current_node, node, edge_type='B', color='green', weight=4)
            else:
                tn = TreeNode(value='▓', child=None, brother=None)
                self.g.add_edge(current_node, tn, edge_type='B', color='green', weight=4)

        if not self.q.empty():
            self.print_tree(node=self.q.get(), level=level + 1)

    def exitStart(self, ctx: AssignmentStatementParser.StartContext):
        self.print_tree(node=self.ast.root, level=1)

    def exitStatement(self, ctx: AssignmentStatementParser.StatementContext):
        ctx.value_attr = ctx.getChild(0).value_attr

    def exitIfst(self, ctx: AssignmentStatementParser.IfstContext):  # 'if' cond 'then' statement ('else' statement)? ;
        condPntr = self.ast.make_node(value=ctx.cond().value_attr.value, child=ctx.cond().value_attr.child,
                                      brother=None)
        ifPntr = self.ast.make_node(value="if", child=condPntr, brother=None)
        thenPntr = self.ast.make_node(value="then", child=ctx.statement(0).value_attr, brother=None)
        if ctx.getChildCount() > 4:
            elsePntr = self.ast.make_node(value="else", child=ctx.statement(1).value_attr, brother=None)
            self.ast.add_brother(thenPntr, elsePntr)
        self.ast.add_brother(condPntr, thenPntr)
        ctx.value_attr = ifPntr
        self.ast.root = ifPntr

    def exitCond(self, ctx: AssignmentStatementParser.CondContext):  # expr '>' expr ;
        self.ast.add_brother(ctx.expr(0).value_attr, ctx.expr(1).value_attr)
        condPntr = self.ast.make_node(value=">", child=ctx.expr(0).value_attr, brother=None)
        ctx.value_attr = condPntr
        self.ast.root = condPntr

    def exitForst(self, ctx: AssignmentStatementParser.ForstContext):  # 'for' ID ':=' expr 'to' expr 'do' statement ;
        IDPntr = self.ast.make_node(value=ctx.ID().getText(), child=None, brother=None)
        ExpressionPntr = self.ast.make_node(value=ctx.expr(0).value_attr.value, child=ctx.expr(0).value_attr.child,
                                            brother=None)
        self.ast.add_brother(IDPntr, ExpressionPntr)
        AssignmentPntr = self.ast.make_node(value=":=", child=IDPntr, brother=None)

        ExpressionPntr2 = self.ast.make_node(value=ctx.expr(1).value_attr.value, child=ctx.expr(1).value_attr.child,
                                             brother=None)
        self.ast.add_brother(AssignmentPntr, ExpressionPntr2)

        toPntr = self.ast.make_node(value="to", child=AssignmentPntr, brother=None)

        DoPntr = self.ast.make_node(value="do", child=ctx.statement().value_attr, brother=None)
        self.ast.add_brother(toPntr, DoPntr)

        ForPntr = self.ast.make_node(value="for", child=toPntr, brother=None)
        ctx.value_attr = ForPntr
        self.ast.root = ForPntr

        # ----------------------

        # idPntr = self.ast.make_node(value=ctx.ID().getText(), child=None, brother=ctx.expr(0).value_attr)
        # assignPntr = self.ast.make_node(value=":=", child=idPntr, brother=ctx.expr(0).value_attr)

        # toPntr = self.ast.make_node(value="to", child=assignPntr, brother=ctx.expr(1).value_attr)
        # loopPntr = self.ast.make_node(value="for", child=toPntr, brother=ctx.statement().value_attr)

        # ctx.value_attr = loopPntr
        # self.ast.root = loopPntr

    def exitWhilest(self, ctx: AssignmentStatementParser.WhilestContext):  # 'while' cond 'do' statement ;
        condPntr = self.ast.make_node(value=ctx.cond().value_attr.value, child=ctx.cond().value_attr.child,
                                      brother=None)
        WhilePntr = self.ast.make_node(value="while", child=condPntr, brother=None)
        statementPntr = self.ast.make_node(value="do", child=ctx.statement().value_attr, brother=None)
        self.ast.add_brother(condPntr, statementPntr)
        ctx.value_attr = WhilePntr
        self.ast.root = WhilePntr

        # ----------------------------------------------

        # loopPntr = self.ast.make_node(value="while", child=ctx.cond().value_attr, brother=ctx.statement().value_attr)
        # ctx.value_attr = loopPntr
        # self.ast.root = loopPntr

    def exitAssign(self, ctx: AssignmentStatementParser.AssignContext):
        # value_attr is a pointer to the node in the AST
        idPntr = self.ast.make_node(value=ctx.ID().getText(), child=None, brother=ctx.expr().value_attr)
        assPntr = self.ast.make_node(value=":=", child=idPntr, brother=None)
        ctx.value_attr = assPntr
        self.ast.root = assPntr

    def exitCompoundst(self, ctx: AssignmentStatementParser.CompoundstContext): # 'begin' NEWLINE (statement NEWLINE)+ 'end'
        count = ctx.getChildCount()
        stPntr = self.ast.make_node(value=ctx.getChild(2).value_attr.value, child=ctx.getChild(2).value_attr.child,
                                    brother=None)
        compPntr = self.ast.make_node(value="block", child=stPntr, brother=None)
        for i in range(2, count - 4, 2):
            print("hello" + ctx.getChild(i).value_attr.value)
            print("print" + ctx.getChild(i + 2).value_attr.value)
            self.ast.add_brother(stPntr, ctx.getChild(i + 2).value_attr)
        ctx.value_attr = compPntr
        self.ast.root = compPntr

    def exitExpr_term_plus(self, ctx: AssignmentStatementParser.Expr_term_plusContext):
        expr_node = ctx.expr().value_attr
        term_node = ctx.term().value_attr
        self.ast.add_brother(expr_node, term_node)
        exprPntr = self.ast.make_node(value="+", child=expr_node, brother=None)
        ctx.value_attr = exprPntr

    def exitExpr_term_minus(self, ctx: AssignmentStatementParser.Expr_term_plusContext):
        self.ast.add_brother(ctx.expr().value_attr, ctx.term().value_attr)
        exprPntr = self.ast.make_node(value="-", child=ctx.expr().value_attr, brother=None)
        ctx.value_attr = exprPntr

    def exitTerm4(self, ctx: AssignmentStatementParser.Term4Context):
        ctx.value_attr = ctx.term().value_attr

    def exitTerm_fact_mutiply(self, ctx: AssignmentStatementParser.Term_fact_mutiplyContext):
        self.ast.add_brother(ctx.term().value_attr, ctx.factor().value_attr)
        termPntr = self.ast.make_node(value="*", child=ctx.term().value_attr, brother=None)
        ctx.value_attr = termPntr

    def exitTerm_fact_divide(self, ctx: AssignmentStatementParser.Term_fact_divideContext): # term '/' factor
        term_node = ctx.term().value_attr
        factor_node = ctx.factor().value_attr
        self.ast.add_brother(term_node, factor_node)
        termPntr = self.ast.make_node(value="/", child=term_node, brother=None)
        ctx.value_attr = termPntr # save the pointer to the node in the AST in context.value_attr

    def exitFactor3(self, ctx: AssignmentStatementParser.Factor3Context):
        ctx.value_attr = ctx.factor().value_attr

    def exitFact_expr(self, ctx: AssignmentStatementParser.Fact_exprContext):
        ctx.value_attr = ctx.expr().value_attr

    def exitFact_id(self, ctx: AssignmentStatementParser.Fact_idContext):
        idPntr = self.ast.make_node(value=ctx.ID().getText(), child=None, brother=None)
        ctx.value_attr = idPntr

    def exitFact_number(self, ctx: AssignmentStatementParser.Fact_numberContext):
        # value_attr is a pointer to the node in the AST
        ctx.value_attr = ctx.number().value_attr # save the pointer to the node in the AST in context.value_attr

    # ----------------------
    def exitNumber_float(self, ctx: AssignmentStatementParser.Number_floatContext):
        numberPntr = self.ast.make_node(value=ctx.FLOAT().getText(), child=None, brother=None)
        ctx.value_attr = numberPntr

    def exitNumber_int(self, ctx: AssignmentStatementParser.Number_intContext):
        numberPntr = self.ast.make_node(value=ctx.INT().getText(), child=None, brother=None)
        ctx.value_attr = numberPntr # save the pointer to the node in the AST in context.value_attr


class TreeNode:
    def __init__(self, value, child, brother):
        self.value = value
        self.child = child
        self.brother = brother


class AST: # Abstract Syntax Tree (AST) data structure
    def __init__(self):
        self.root = None
        self.current = None

    def make_node(self, value, child, brother):
        tree_node = TreeNode(value, child, brother)
        self.current = tree_node
        return tree_node

    def add_child(self, node, new_child):
        if node.child is None:
            node.child = new_child
        else:
            self.current = node.child
            while self.current.brother is not None: # traverse to the last child (most right child)
                self.current = self.current.brother
            self.current.brother = new_child # add the new child to the last child
        self.current = new_child

    def add_brother(self, node, new_brother):
        if node.brother is None:
            node.brother = new_brother
        else:
            self.current = node.brother
            while self.current.brother is not None: # traverse to the last brother (most right brother)
                self.current = self.current.brother
            self.current.brother = new_brother # add the new brother to the last brother
        self.current = new_brother
