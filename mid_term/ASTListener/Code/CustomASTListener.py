import queue
import networkx as nx
import matplotlib.pyplot as plt
from tkinter import ttk
import tkinter as tk

from Gen.AssignmentStatementListener import AssignmentStatementListener
from Gen.AssignmentStatementParser import AssignmentStatementParser

class ASTListener(AssignmentStatementListener):
    def __init__(self):
        self.ast = AST()               # Data structure for holding the abstract syntax tree
        self.q = queue.Queue()         # Use to print and visualize InClassPresentation
        self.g = nx.DiGraph()          # Use to visualize InClassPresentation
        self.max_x = 0

        # super().__init__()
        self.variable_types = {}  # Dictionary to store variable types

# -------------------------------------------------------
    def draw_tree(self, node, x, y):
        if node is None:
             return
        # Draw the node
        if x < self.max_x:
            x = self.max_x
        plt.plot(x, y, 'o', markersize=15, color='cyan')
        plt.text(x, y, str(node.value), ha='center', va='center')
        print("x = ", x, "max_x ", self.max_x," y = ", y, " nd: ", node.value)
        if node.brother is not None:
            print("brother of ", node.value, " is", node.brother.value)
        if node.child is not None:
            print("child of ", node.value, " is", node.child.value)
        
        # Draw the vertical line to the first child
        if node.child is not None:
            plt.plot([x, x], [y - 0.1, y - 1], 'k-', linewidth=2, color='red')
            self.draw_tree(node.child, x, y - 1)

        # Draw the horizontal line to the first brother
        if node.brother is not None:
            plt.plot([x + 0.1, self.max_x +  1], [y, y], 'k-', linewidth=2, color='red')
            print("----x is :", x, "self.max_x ", self.max_x)
            self.max_x += 1
            self.draw_tree(node.brother, x + 1, y)

    def transform_binary_tree(self, root):
        if root is None:
            return None

        tree=ttk.Treeview()
        nodes={}

        def traverse(node, parent, iid=None):
            if node is None:
                return

            node_id=len(nodes)
            nodes[node_id]=node

            if parent is None:
                iid=tree.insert('', 'end', text=str(node.value))
            else:
                iid=tree.insert(parent, 'end', text=str(node.value))

            traverse(node.child, iid)
            traverse(node.brother, parent)

        traverse(root, None)
        return tree

    def display_treeview(self, tree):
        tree.pack()
        tk.mainloop()

    # -------------------------------------------------------

    def exitStart(self, ctx: AssignmentStatementParser.StartContext):
        #self.print_tree(node=self.ast.root, level=1)
        # Draw the tree
        self.draw_tree(node=self.ast.root, x = 0, y = 0)
        tree = self.transform_binary_tree(self.ast.root)
        self.display_treeview(tree)
        
        # Show the plot
        #plt.axis('off')
        print("Bye")
        # Save the plot to a file
        plt.savefig('tree.png')
        print('tree.png')
        plt.show()

    def exitStatement(self, ctx: AssignmentStatementParser.StatementContext):
        ctx.value_attr = ctx.getChild(0).value_attr # Pass the value_attr attribute of the first child to the parent node

    # Make a subtree for a given parsa tree node, tree node.
    def make_AST_subtree(self, tree_node, opertor): # magical function
        first_child = None
        previous_child = None # brother = None
        no_children = tree_node.getChildCount()
        for i in range(0, no_children):
            next_child = tree_node.getChild(i)
            if(hasattr(next_child, 'value_attr')): # if the child has a value_attr attribute (i.e. it is a node in the AST)
                # print("i = ", i, "count = ", no_children, next_child.value_attr.value)

                if first_child == None:
                    first_child = next_child.value_attr # first_child is a pointer to the node in the AST
                if previous_child != None: # if previous_child is not None (i.e. if it is not the first child)
                    previous_child.value_attr.brother = next_child.value_attr # add the new child as a brother of previous child
                    # self.ast.add_brother(previous_child, next_child)
                previous_child = next_child
        sub_tree_pntr = self.ast.make_node(value=opertor, child=first_child, brother=None)
        tree_node.value_attr = sub_tree_pntr # save the sub_tree in value_attr of the ctx
        self.ast.root = sub_tree_pntr

    def exitIfst(self, ctx: AssignmentStatementParser.IfstContext):
        self.make_AST_subtree(tree_node = ctx, opertor = "if")

    # Exit a parse tree produced by AssignmentStatementParser#ternaryoperator.
    def exitTernaryoperator(self, ctx: AssignmentStatementParser.TernaryoperatorContext):
        self.make_AST_subtree(tree_node = ctx, opertor = "ternary")

        # expr_node = ctx.expr().value_attr
        # idPntr = self.ast.make_node(value=ctx.ID().getText(), child=None, brother=expr_node)
        # assPntr = self.ast.make_node(value=":=", child=idPntr, brother=None)
        # ctx.value_attr = assPntr  # store the pointer to the node in the AST
        # self.ast.root = assPntr

    # Exit a parse tree produced by AssignmentStatementParser#forst.
    def exitForst(self, ctx: AssignmentStatementParser.ForstContext):
        self.make_AST_subtree(tree_node = ctx, opertor = "for")

    # Exit a parse tree produced by AssignmentStatementParser#whilest.
    def exitWhilest(self, ctx: AssignmentStatementParser.WhilestContext):
        self.make_AST_subtree(tree_node = ctx, opertor = "while")

    # Exit a parse tree produced by AssignmentStatementParser#switchst.
    def exitSwitchst(self, ctx: AssignmentStatementParser.SwitchstContext):
        self.make_AST_subtree(tree_node = ctx, opertor = "switch")

    def exitCond(self, ctx:AssignmentStatementParser.CondContext):
        self.make_AST_subtree(tree_node=ctx, opertor=">")
        # self.make_AST_subtree(tree_node=ctx, opertor=ctx.getChild(1).getText())



    # def exitAssign(self, ctx: AssignmentStatementParser.AssignContext): # ID ':=' expr
    #     expr_node = ctx.expr().value_attr
    #     idPntr = self.ast.make_node(value=ctx.ID().getText(), child=None, brother=expr_node)
    #     assPntr = self.ast.make_node(value=":=", child=idPntr, brother=None)
    #     ctx.value_attr = assPntr # store the pointer to the node in the AST
    #     self.ast.root = assPntr

    # Exit a parse tree produced by AssignmentStatementParser#assign_expr.
    def exitAssign_expr(self, ctx: AssignmentStatementParser.Assign_exprContext):
        expr_node = ctx.expr().value_attr
        idPntr = self.ast.make_node(value=ctx.ID().getText(), child=None, brother=expr_node)
        assPntr = self.ast.make_node(value=":=", child=idPntr, brother=None)
        ctx.value_attr = assPntr  # store the pointer to the node in the AST
        self.ast.root = assPntr

    # Exit a parse tree produced by AssignmentStatementParser#assign_ternaryoperator.
    def exitAssign_ternaryoperator(self, ctx: AssignmentStatementParser.Assign_ternaryoperatorContext):
        ternaryoperator_node = ctx.ternaryoperator().value_attr
        idPntr = self.ast.make_node(value=ctx.ID().getText(), child=None, brother=ternaryoperator_node)
        assPntr = self.ast.make_node(value=":=", child=idPntr, brother=None)
        ctx.value_attr = assPntr  # store the pointer to the node in the AST
        self.ast.root = assPntr

    def exitCompoundst(self, ctx:AssignmentStatementParser.CompoundstContext):
        self.make_AST_subtree(tree_node = ctx, opertor = "block")

    def exitExpr_term_plus(self, ctx: AssignmentStatementParser.Expr_term_plusContext): # expr '+' term        #expr_term_plus
        # expr_node = ctx.expr().value_attr
        # term_node = ctx.term().value_attr
        # self.ast.add_brother(expr_node, term_node)
        # exprPntr = self.ast.make_node(value="+", child=expr_node, brother=None)
        # ctx.value_attr = exprPntr

        self.make_AST_subtree(tree_node = ctx, opertor = "+")

        # term1_type = ctx.expr(0).type_attr
        # term2_type = ctx.term().type_attr
        # if term1_type != term2_type:
        #     raise TypeError(f"Type error: Cannot perform addition between {term1_type} and {term2_type}")
        #
        # ctx.type_attr = term1_type  # Assuming the expr node has a 'type_attr' attribute to store the type

    def exitExpr_term_minus(self, ctx: AssignmentStatementParser.Expr_term_plusContext):
        self.make_AST_subtree(tree_node= ctx, opertor = "-")
        # term1_type = ctx.expr(0).type_attr
        # term2_type = ctx.term().type_attr
        # if term1_type != term2_type:
        #     raise TypeError(f"Type error: Cannot perform subtraction between {term1_type} and {term2_type}")
        #
        # ctx.type_attr = term1_type  # Assuming the expr node has a 'type_attr' attribute to store the type

    def exitTerm4(self, ctx: AssignmentStatementParser.Term4Context):
        ctx.value_attr = ctx.term().value_attr

    def exitTerm_fact_mutiply(self, ctx: AssignmentStatementParser.Term_fact_mutiplyContext):
        self.make_AST_subtree(tree_node= ctx, opertor = "*")

    def exitTerm_fact_divide(self, ctx: AssignmentStatementParser.Term_fact_divideContext):
        self.make_AST_subtree(tree_node= ctx, opertor = "/")

    def exitFactor3(self, ctx: AssignmentStatementParser.Factor3Context):
        ctx.value_attr = ctx.factor().value_attr

    def exitFact_expr(self, ctx: AssignmentStatementParser.Fact_exprContext):
        ctx.value_attr = ctx.expr().value_attr

    def exitFact_id(self, ctx: AssignmentStatementParser.Fact_idContext):
        idPntr = self.ast.make_node(value=ctx.ID().getText(), child=None, brother=None)
        ctx.value_attr = idPntr

    def exitFact_number(self, ctx: AssignmentStatementParser.Fact_numberContext):
        ctx.value_attr = ctx.number().value_attr

    # ----------------------
    def exitNumber_float(self, ctx: AssignmentStatementParser.Number_floatContext):
        numberPntr = self.ast.make_node(value=ctx.FLOAT().getText(), child=None, brother=None)
        ctx.value_attr = numberPntr # value_attr is a pointer to the node in the AST
        ctx.type_attr = 'float'

    def exitNumber_int(self, ctx: AssignmentStatementParser.Number_intContext):
        numberPntr = self.ast.make_node(value=ctx.INT().getText(), child=None, brother=None)
        ctx.value_attr = numberPntr # value_attr is a pointer to the node in the AST
        ctx.type_attr = 'int'

    # def exitVariable_declaration(self, ctx: AssignmentStatementParser.Variable_declarationContext):
    #     var_name = ctx.ID().getText()
    #     var_type = ctx.type().getText()
    #     self.variable_types[var_name] = var_type  # Store variable types
    #
    # def exitAssign(self, ctx: AssignmentStatementParser.AssignContext):
    #     var_name = ctx.ID().getText()
    #     expr_type = self.visit(ctx.expr())  # Get the type of the expression
    #     if var_name in self.variable_types:
    #         expected_type = self.variable_types[var_name]
    #         if expr_type != expected_type:
    #             raise TypeError(f"Type error: Cannot assign {expr_type} to variable {var_name} of type {expected_type}")

    # def visitNumber_float(self, ctx: AssignmentStatementParser.Number_floatContext):
    #     return 'float'
    #
    # def visitNumber_int(self, ctx: AssignmentStatementParser.Number_intContext):
    #     return 'int'

    # def visitString(self, ctx: AssignmentStatementParser.StringContext):
    #     return 'string'

    # def visitID(self, ctx: AssignmentStatementParser.IDContext):
    #     var_name = ctx.getText()
    #     if var_name in self.variable_types:
    #         return self.variable_types[var_name]
    #     else:
    #         raise NameError(f"Variable {var_name} is not defined")


class TreeNode: # Data structure for holding a node of the abstract syntax tree
    def __init__(self, value, child, brother):
        self.value = value
        self.child = child
        self.brother = brother

class AST: # Data structure for holding the abstract syntax tree (binary tree)
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
            while self.current.brother is not None: # Find the last child (right most child)
                self.current = self.current.brother
            self.current.brother = new_child # Add the new child
        self.current = new_child

    def add_brother(self, node, new_brother):
        if node.brother is None:
            node.brother = new_brother
        else:
            self.current = node.brother
            while self.current.brother is not None: # Find the last brother (right most brother)
                self.current = self.current.brother
            self.current.brother = new_brother
        self.current = new_brother


