// Generated from e:/uni/7th term/fundamentals of compiler design/HWs/HW3/chaloosOotagh.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link chaloosOotaghParser}.
 */
public interface chaloosOotaghListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link chaloosOotaghParser#start}.
	 * @param ctx the parse tree
	 */
	void enterStart(chaloosOotaghParser.StartContext ctx);
	/**
	 * Exit a parse tree produced by {@link chaloosOotaghParser#start}.
	 * @param ctx the parse tree
	 */
	void exitStart(chaloosOotaghParser.StartContext ctx);
	/**
	 * Enter a parse tree produced by {@link chaloosOotaghParser#prog}.
	 * @param ctx the parse tree
	 */
	void enterProg(chaloosOotaghParser.ProgContext ctx);
	/**
	 * Exit a parse tree produced by {@link chaloosOotaghParser#prog}.
	 * @param ctx the parse tree
	 */
	void exitProg(chaloosOotaghParser.ProgContext ctx);
	/**
	 * Enter a parse tree produced by {@link chaloosOotaghParser#declaration}.
	 * @param ctx the parse tree
	 */
	void enterDeclaration(chaloosOotaghParser.DeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link chaloosOotaghParser#declaration}.
	 * @param ctx the parse tree
	 */
	void exitDeclaration(chaloosOotaghParser.DeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link chaloosOotaghParser#variable_declaration}.
	 * @param ctx the parse tree
	 */
	void enterVariable_declaration(chaloosOotaghParser.Variable_declarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link chaloosOotaghParser#variable_declaration}.
	 * @param ctx the parse tree
	 */
	void exitVariable_declaration(chaloosOotaghParser.Variable_declarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link chaloosOotaghParser#type}.
	 * @param ctx the parse tree
	 */
	void enterType(chaloosOotaghParser.TypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link chaloosOotaghParser#type}.
	 * @param ctx the parse tree
	 */
	void exitType(chaloosOotaghParser.TypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link chaloosOotaghParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(chaloosOotaghParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link chaloosOotaghParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(chaloosOotaghParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link chaloosOotaghParser#compoundst}.
	 * @param ctx the parse tree
	 */
	void enterCompoundst(chaloosOotaghParser.CompoundstContext ctx);
	/**
	 * Exit a parse tree produced by {@link chaloosOotaghParser#compoundst}.
	 * @param ctx the parse tree
	 */
	void exitCompoundst(chaloosOotaghParser.CompoundstContext ctx);
	/**
	 * Enter a parse tree produced by {@link chaloosOotaghParser#whilest}.
	 * @param ctx the parse tree
	 */
	void enterWhilest(chaloosOotaghParser.WhilestContext ctx);
	/**
	 * Exit a parse tree produced by {@link chaloosOotaghParser#whilest}.
	 * @param ctx the parse tree
	 */
	void exitWhilest(chaloosOotaghParser.WhilestContext ctx);
	/**
	 * Enter a parse tree produced by {@link chaloosOotaghParser#ifst}.
	 * @param ctx the parse tree
	 */
	void enterIfst(chaloosOotaghParser.IfstContext ctx);
	/**
	 * Exit a parse tree produced by {@link chaloosOotaghParser#ifst}.
	 * @param ctx the parse tree
	 */
	void exitIfst(chaloosOotaghParser.IfstContext ctx);
	/**
	 * Enter a parse tree produced by {@link chaloosOotaghParser#cond}.
	 * @param ctx the parse tree
	 */
	void enterCond(chaloosOotaghParser.CondContext ctx);
	/**
	 * Exit a parse tree produced by {@link chaloosOotaghParser#cond}.
	 * @param ctx the parse tree
	 */
	void exitCond(chaloosOotaghParser.CondContext ctx);
	/**
	 * Enter a parse tree produced by {@link chaloosOotaghParser#assign}.
	 * @param ctx the parse tree
	 */
	void enterAssign(chaloosOotaghParser.AssignContext ctx);
	/**
	 * Exit a parse tree produced by {@link chaloosOotaghParser#assign}.
	 * @param ctx the parse tree
	 */
	void exitAssign(chaloosOotaghParser.AssignContext ctx);
	/**
	 * Enter a parse tree produced by the {@code expr_term_minus}
	 * labeled alternative in {@link chaloosOotaghParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr_term_minus(chaloosOotaghParser.Expr_term_minusContext ctx);
	/**
	 * Exit a parse tree produced by the {@code expr_term_minus}
	 * labeled alternative in {@link chaloosOotaghParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr_term_minus(chaloosOotaghParser.Expr_term_minusContext ctx);
	/**
	 * Enter a parse tree produced by the {@code expr_term_plus}
	 * labeled alternative in {@link chaloosOotaghParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr_term_plus(chaloosOotaghParser.Expr_term_plusContext ctx);
	/**
	 * Exit a parse tree produced by the {@code expr_term_plus}
	 * labeled alternative in {@link chaloosOotaghParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr_term_plus(chaloosOotaghParser.Expr_term_plusContext ctx);
	/**
	 * Enter a parse tree produced by the {@code term4}
	 * labeled alternative in {@link chaloosOotaghParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterTerm4(chaloosOotaghParser.Term4Context ctx);
	/**
	 * Exit a parse tree produced by the {@code term4}
	 * labeled alternative in {@link chaloosOotaghParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitTerm4(chaloosOotaghParser.Term4Context ctx);
	/**
	 * Enter a parse tree produced by the {@code expr_term_relop}
	 * labeled alternative in {@link chaloosOotaghParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr_term_relop(chaloosOotaghParser.Expr_term_relopContext ctx);
	/**
	 * Exit a parse tree produced by the {@code expr_term_relop}
	 * labeled alternative in {@link chaloosOotaghParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr_term_relop(chaloosOotaghParser.Expr_term_relopContext ctx);
	/**
	 * Enter a parse tree produced by the {@code term_fact_divide}
	 * labeled alternative in {@link chaloosOotaghParser#term}.
	 * @param ctx the parse tree
	 */
	void enterTerm_fact_divide(chaloosOotaghParser.Term_fact_divideContext ctx);
	/**
	 * Exit a parse tree produced by the {@code term_fact_divide}
	 * labeled alternative in {@link chaloosOotaghParser#term}.
	 * @param ctx the parse tree
	 */
	void exitTerm_fact_divide(chaloosOotaghParser.Term_fact_divideContext ctx);
	/**
	 * Enter a parse tree produced by the {@code term_fact_mutiply}
	 * labeled alternative in {@link chaloosOotaghParser#term}.
	 * @param ctx the parse tree
	 */
	void enterTerm_fact_mutiply(chaloosOotaghParser.Term_fact_mutiplyContext ctx);
	/**
	 * Exit a parse tree produced by the {@code term_fact_mutiply}
	 * labeled alternative in {@link chaloosOotaghParser#term}.
	 * @param ctx the parse tree
	 */
	void exitTerm_fact_mutiply(chaloosOotaghParser.Term_fact_mutiplyContext ctx);
	/**
	 * Enter a parse tree produced by the {@code factor3}
	 * labeled alternative in {@link chaloosOotaghParser#term}.
	 * @param ctx the parse tree
	 */
	void enterFactor3(chaloosOotaghParser.Factor3Context ctx);
	/**
	 * Exit a parse tree produced by the {@code factor3}
	 * labeled alternative in {@link chaloosOotaghParser#term}.
	 * @param ctx the parse tree
	 */
	void exitFactor3(chaloosOotaghParser.Factor3Context ctx);
	/**
	 * Enter a parse tree produced by the {@code fact_expr}
	 * labeled alternative in {@link chaloosOotaghParser#factor}.
	 * @param ctx the parse tree
	 */
	void enterFact_expr(chaloosOotaghParser.Fact_exprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code fact_expr}
	 * labeled alternative in {@link chaloosOotaghParser#factor}.
	 * @param ctx the parse tree
	 */
	void exitFact_expr(chaloosOotaghParser.Fact_exprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code fact_id}
	 * labeled alternative in {@link chaloosOotaghParser#factor}.
	 * @param ctx the parse tree
	 */
	void enterFact_id(chaloosOotaghParser.Fact_idContext ctx);
	/**
	 * Exit a parse tree produced by the {@code fact_id}
	 * labeled alternative in {@link chaloosOotaghParser#factor}.
	 * @param ctx the parse tree
	 */
	void exitFact_id(chaloosOotaghParser.Fact_idContext ctx);
	/**
	 * Enter a parse tree produced by the {@code fact_number}
	 * labeled alternative in {@link chaloosOotaghParser#factor}.
	 * @param ctx the parse tree
	 */
	void enterFact_number(chaloosOotaghParser.Fact_numberContext ctx);
	/**
	 * Exit a parse tree produced by the {@code fact_number}
	 * labeled alternative in {@link chaloosOotaghParser#factor}.
	 * @param ctx the parse tree
	 */
	void exitFact_number(chaloosOotaghParser.Fact_numberContext ctx);
	/**
	 * Enter a parse tree produced by the {@code fact_boolean}
	 * labeled alternative in {@link chaloosOotaghParser#factor}.
	 * @param ctx the parse tree
	 */
	void enterFact_boolean(chaloosOotaghParser.Fact_booleanContext ctx);
	/**
	 * Exit a parse tree produced by the {@code fact_boolean}
	 * labeled alternative in {@link chaloosOotaghParser#factor}.
	 * @param ctx the parse tree
	 */
	void exitFact_boolean(chaloosOotaghParser.Fact_booleanContext ctx);
	/**
	 * Enter a parse tree produced by the {@code number_int}
	 * labeled alternative in {@link chaloosOotaghParser#number}.
	 * @param ctx the parse tree
	 */
	void enterNumber_int(chaloosOotaghParser.Number_intContext ctx);
	/**
	 * Exit a parse tree produced by the {@code number_int}
	 * labeled alternative in {@link chaloosOotaghParser#number}.
	 * @param ctx the parse tree
	 */
	void exitNumber_int(chaloosOotaghParser.Number_intContext ctx);
}