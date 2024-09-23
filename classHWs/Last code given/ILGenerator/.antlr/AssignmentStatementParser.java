// Generated from e:/uni/7th term/fundamentals of compiler design/classHWs/Last code given/ILGenerator/AssignmentStatement.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class AssignmentStatementParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		T__24=25, T__25=26, T__26=27, T__27=28, T__28=29, T__29=30, T__30=31, 
		T__31=32, T__32=33, T__33=34, T__34=35, INT=36, FLOAT=37, String=38, ID=39, 
		ARRAY_TYPE=40, INT_ARRAY=41, FLOAT_ARRAY=42, STRING_ARRAY=43, WS=44, COMMENT=45, 
		NEWLINE=46, RELOP=47;
	public static final int
		RULE_start = 0, RULE_prog = 1, RULE_declaration = 2, RULE_variable_declaration = 3, 
		RULE_type = 4, RULE_compoundst = 5, RULE_statement = 6, RULE_ifst = 7, 
		RULE_whilest = 8, RULE_switchst = 9, RULE_case = 10, RULE_casedefault = 11, 
		RULE_breakst = 12, RULE_forst = 13, RULE_cond = 14, RULE_assign = 15, 
		RULE_ternary = 16, RULE_expr = 17, RULE_term = 18, RULE_factor = 19, RULE_number = 20, 
		RULE_array = 21;
	private static String[] makeRuleNames() {
		return new String[] {
			"start", "prog", "declaration", "variable_declaration", "type", "compoundst", 
			"statement", "ifst", "whilest", "switchst", "case", "casedefault", "breakst", 
			"forst", "cond", "assign", "ternary", "expr", "term", "factor", "number", 
			"array"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'program'", "'var'", "':'", "'float'", "'int'", "'string'", "'begin'", 
			"'end'", "'if'", "'then'", "'else'", "'while'", "'do'", "'switch'", "'('", 
			"')'", "'case'", "'default'", "'break'", "'for'", "':='", "'to'", "'>'", 
			"'<'", "'=='", "'!='", "'<='", "'>='", "'&&'", "'||'", "'?'", "'+'", 
			"'-'", "'*'", "'/'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			"INT", "FLOAT", "String", "ID", "ARRAY_TYPE", "INT_ARRAY", "FLOAT_ARRAY", 
			"STRING_ARRAY", "WS", "COMMENT", "NEWLINE", "RELOP"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "AssignmentStatement.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public AssignmentStatementParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StartContext extends ParserRuleContext {
		public  value_attr = str();
		public  type_attr = str();
		public ProgContext prog() {
			return getRuleContext(ProgContext.class,0);
		}
		public TerminalNode EOF() { return getToken(AssignmentStatementParser.EOF, 0); }
		public List<TerminalNode> NEWLINE() { return getTokens(AssignmentStatementParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(AssignmentStatementParser.NEWLINE, i);
		}
		public StartContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_start; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).enterStart(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).exitStart(this);
		}
	}

	public final StartContext start() throws RecognitionException {
		StartContext _localctx = new StartContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_start);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(44);
			prog();
			setState(48);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==NEWLINE) {
				{
				{
				setState(45);
				match(NEWLINE);
				}
				}
				setState(50);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(51);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgContext extends ParserRuleContext {
		public  value_attr = str();
		public  type_attr = str();
		public TerminalNode ID() { return getToken(AssignmentStatementParser.ID, 0); }
		public CompoundstContext compoundst() {
			return getRuleContext(CompoundstContext.class,0);
		}
		public List<TerminalNode> NEWLINE() { return getTokens(AssignmentStatementParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(AssignmentStatementParser.NEWLINE, i);
		}
		public DeclarationContext declaration() {
			return getRuleContext(DeclarationContext.class,0);
		}
		public ProgContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_prog; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).enterProg(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).exitProg(this);
		}
	}

	public final ProgContext prog() throws RecognitionException {
		ProgContext _localctx = new ProgContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_prog);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(53);
			match(T__0);
			setState(54);
			match(ID);
			setState(58);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,1,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(55);
					match(NEWLINE);
					}
					} 
				}
				setState(60);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,1,_ctx);
			}
			setState(62);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__1) {
				{
				setState(61);
				declaration();
				}
			}

			setState(65); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(64);
				match(NEWLINE);
				}
				}
				setState(67); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==NEWLINE );
			setState(69);
			compoundst();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DeclarationContext extends ParserRuleContext {
		public  value_attr = str();
		public  type_attr = str();
		public List<TerminalNode> NEWLINE() { return getTokens(AssignmentStatementParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(AssignmentStatementParser.NEWLINE, i);
		}
		public List<Variable_declarationContext> variable_declaration() {
			return getRuleContexts(Variable_declarationContext.class);
		}
		public Variable_declarationContext variable_declaration(int i) {
			return getRuleContext(Variable_declarationContext.class,i);
		}
		public DeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaration; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).enterDeclaration(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).exitDeclaration(this);
		}
	}

	public final DeclarationContext declaration() throws RecognitionException {
		DeclarationContext _localctx = new DeclarationContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_declaration);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(71);
			match(T__1);
			setState(75);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==NEWLINE) {
				{
				{
				setState(72);
				match(NEWLINE);
				}
				}
				setState(77);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(85); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(78);
				variable_declaration();
				setState(82);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
				while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1 ) {
						{
						{
						setState(79);
						match(NEWLINE);
						}
						} 
					}
					setState(84);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
				}
				}
				}
				setState(87); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==ID );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Variable_declarationContext extends ParserRuleContext {
		public  value_attr = str();
		public  type_attr = str();
		public TerminalNode ID() { return getToken(AssignmentStatementParser.ID, 0); }
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public Variable_declarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variable_declaration; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).enterVariable_declaration(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).exitVariable_declaration(this);
		}
	}

	public final Variable_declarationContext variable_declaration() throws RecognitionException {
		Variable_declarationContext _localctx = new Variable_declarationContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_variable_declaration);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(89);
			match(ID);
			setState(90);
			match(T__2);
			setState(91);
			type();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TypeContext extends ParserRuleContext {
		public  value_attr = str();
		public  type_attr = str();
		public TypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_type; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).enterType(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).exitType(this);
		}
	}

	public final TypeContext type() throws RecognitionException {
		TypeContext _localctx = new TypeContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_type);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(93);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 112L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CompoundstContext extends ParserRuleContext {
		public  value_attr = str();
		public  type_attr = str();
		public List<TerminalNode> NEWLINE() { return getTokens(AssignmentStatementParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(AssignmentStatementParser.NEWLINE, i);
		}
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public CompoundstContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_compoundst; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).enterCompoundst(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).exitCompoundst(this);
		}
	}

	public final CompoundstContext compoundst() throws RecognitionException {
		CompoundstContext _localctx = new CompoundstContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_compoundst);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(95);
			match(T__6);
			setState(99);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==NEWLINE) {
				{
				{
				setState(96);
				match(NEWLINE);
				}
				}
				setState(101);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(108); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(102);
				statement();
				setState(104); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(103);
					match(NEWLINE);
					}
					}
					setState(106); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==NEWLINE );
				}
				}
				setState(110); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 549756883584L) != 0) );
			setState(112);
			match(T__7);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatementContext extends ParserRuleContext {
		public  value_attr = str();
		public  type_attr = str();
		public IfstContext ifst() {
			return getRuleContext(IfstContext.class,0);
		}
		public AssignContext assign() {
			return getRuleContext(AssignContext.class,0);
		}
		public CompoundstContext compoundst() {
			return getRuleContext(CompoundstContext.class,0);
		}
		public WhilestContext whilest() {
			return getRuleContext(WhilestContext.class,0);
		}
		public SwitchstContext switchst() {
			return getRuleContext(SwitchstContext.class,0);
		}
		public ForstContext forst() {
			return getRuleContext(ForstContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).enterStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).exitStatement(this);
		}
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_statement);
		try {
			setState(120);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__8:
				enterOuterAlt(_localctx, 1);
				{
				setState(114);
				ifst();
				}
				break;
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				setState(115);
				assign();
				}
				break;
			case T__6:
				enterOuterAlt(_localctx, 3);
				{
				setState(116);
				compoundst();
				}
				break;
			case T__11:
				enterOuterAlt(_localctx, 4);
				{
				setState(117);
				whilest();
				}
				break;
			case T__13:
				enterOuterAlt(_localctx, 5);
				{
				setState(118);
				switchst();
				}
				break;
			case T__19:
				enterOuterAlt(_localctx, 6);
				{
				setState(119);
				forst();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IfstContext extends ParserRuleContext {
		public  value_attr = str();
		public  type_attr = str();
		public CondContext cond() {
			return getRuleContext(CondContext.class,0);
		}
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public List<TerminalNode> NEWLINE() { return getTokens(AssignmentStatementParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(AssignmentStatementParser.NEWLINE, i);
		}
		public IfstContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifst; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).enterIfst(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).exitIfst(this);
		}
	}

	public final IfstContext ifst() throws RecognitionException {
		IfstContext _localctx = new IfstContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_ifst);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(122);
			match(T__8);
			setState(123);
			cond();
			setState(124);
			match(T__9);
			setState(128);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==NEWLINE) {
				{
				{
				setState(125);
				match(NEWLINE);
				}
				}
				setState(130);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(131);
			statement();
			setState(135);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,12,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(132);
					match(NEWLINE);
					}
					} 
				}
				setState(137);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,12,_ctx);
			}
			setState(146);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,14,_ctx) ) {
			case 1:
				{
				setState(138);
				match(T__10);
				setState(142);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==NEWLINE) {
					{
					{
					setState(139);
					match(NEWLINE);
					}
					}
					setState(144);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(145);
				statement();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class WhilestContext extends ParserRuleContext {
		public  value_attr = str();
		public  type_attr = str();
		public CondContext cond() {
			return getRuleContext(CondContext.class,0);
		}
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public List<TerminalNode> NEWLINE() { return getTokens(AssignmentStatementParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(AssignmentStatementParser.NEWLINE, i);
		}
		public WhilestContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whilest; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).enterWhilest(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).exitWhilest(this);
		}
	}

	public final WhilestContext whilest() throws RecognitionException {
		WhilestContext _localctx = new WhilestContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_whilest);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(148);
			match(T__11);
			setState(149);
			cond();
			setState(150);
			match(T__12);
			setState(154);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==NEWLINE) {
				{
				{
				setState(151);
				match(NEWLINE);
				}
				}
				setState(156);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(157);
			statement();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SwitchstContext extends ParserRuleContext {
		public  value_attr = str();
		public  type_attr = str();
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public List<TerminalNode> NEWLINE() { return getTokens(AssignmentStatementParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(AssignmentStatementParser.NEWLINE, i);
		}
		public List<CaseContext> case_() {
			return getRuleContexts(CaseContext.class);
		}
		public CaseContext case_(int i) {
			return getRuleContext(CaseContext.class,i);
		}
		public CasedefaultContext casedefault() {
			return getRuleContext(CasedefaultContext.class,0);
		}
		public SwitchstContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_switchst; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).enterSwitchst(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).exitSwitchst(this);
		}
	}

	public final SwitchstContext switchst() throws RecognitionException {
		SwitchstContext _localctx = new SwitchstContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_switchst);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(159);
			match(T__13);
			setState(160);
			match(T__14);
			setState(161);
			expr(0);
			setState(162);
			match(T__15);
			setState(166);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==NEWLINE) {
				{
				{
				setState(163);
				match(NEWLINE);
				}
				}
				setState(168);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(169);
			match(T__6);
			setState(173);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==NEWLINE) {
				{
				{
				setState(170);
				match(NEWLINE);
				}
				}
				setState(175);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(177); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(176);
				case_();
				}
				}
				setState(179); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==T__16 );
			setState(182);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__17) {
				{
				setState(181);
				casedefault();
				}
			}

			setState(187);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==NEWLINE) {
				{
				{
				setState(184);
				match(NEWLINE);
				}
				}
				setState(189);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(190);
			match(T__7);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CaseContext extends ParserRuleContext {
		public  value_attr = str();
		public  type_attr = str();
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public List<TerminalNode> NEWLINE() { return getTokens(AssignmentStatementParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(AssignmentStatementParser.NEWLINE, i);
		}
		public BreakstContext breakst() {
			return getRuleContext(BreakstContext.class,0);
		}
		public CaseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_case; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).enterCase(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).exitCase(this);
		}
	}

	public final CaseContext case_() throws RecognitionException {
		CaseContext _localctx = new CaseContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_case);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(192);
			match(T__16);
			setState(193);
			expr(0);
			setState(194);
			match(T__2);
			setState(198);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==NEWLINE) {
				{
				{
				setState(195);
				match(NEWLINE);
				}
				}
				setState(200);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(201);
			statement();
			setState(205);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,22,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(202);
					match(NEWLINE);
					}
					} 
				}
				setState(207);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,22,_ctx);
			}
			setState(209);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__18) {
				{
				setState(208);
				breakst();
				}
			}

			setState(214);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,24,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(211);
					match(NEWLINE);
					}
					} 
				}
				setState(216);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,24,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CasedefaultContext extends ParserRuleContext {
		public  value_attr = str();
		public  type_attr = str();
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public List<TerminalNode> NEWLINE() { return getTokens(AssignmentStatementParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(AssignmentStatementParser.NEWLINE, i);
		}
		public BreakstContext breakst() {
			return getRuleContext(BreakstContext.class,0);
		}
		public CasedefaultContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_casedefault; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).enterCasedefault(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).exitCasedefault(this);
		}
	}

	public final CasedefaultContext casedefault() throws RecognitionException {
		CasedefaultContext _localctx = new CasedefaultContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_casedefault);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(217);
			match(T__17);
			setState(218);
			match(T__2);
			setState(222);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==NEWLINE) {
				{
				{
				setState(219);
				match(NEWLINE);
				}
				}
				setState(224);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(225);
			statement();
			setState(229);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,26,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(226);
					match(NEWLINE);
					}
					} 
				}
				setState(231);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,26,_ctx);
			}
			setState(233);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__18) {
				{
				setState(232);
				breakst();
				}
			}

			setState(238);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,28,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(235);
					match(NEWLINE);
					}
					} 
				}
				setState(240);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,28,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BreakstContext extends ParserRuleContext {
		public  value_attr = str();
		public  type_attr = str();
		public BreakstContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_breakst; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).enterBreakst(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).exitBreakst(this);
		}
	}

	public final BreakstContext breakst() throws RecognitionException {
		BreakstContext _localctx = new BreakstContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_breakst);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(241);
			match(T__18);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ForstContext extends ParserRuleContext {
		public  value_attr = str();
		public  type_attr = str();
		public TerminalNode ID() { return getToken(AssignmentStatementParser.ID, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public List<TerminalNode> NEWLINE() { return getTokens(AssignmentStatementParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(AssignmentStatementParser.NEWLINE, i);
		}
		public ForstContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_forst; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).enterForst(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).exitForst(this);
		}
	}

	public final ForstContext forst() throws RecognitionException {
		ForstContext _localctx = new ForstContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_forst);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(243);
			match(T__19);
			setState(244);
			match(ID);
			setState(245);
			match(T__20);
			setState(246);
			expr(0);
			setState(247);
			match(T__21);
			setState(248);
			expr(0);
			setState(249);
			match(T__12);
			setState(253);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==NEWLINE) {
				{
				{
				setState(250);
				match(NEWLINE);
				}
				}
				setState(255);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(256);
			statement();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CondContext extends ParserRuleContext {
		public  value_attr = str();
		public  type_attr = str();
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public CondContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cond; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).enterCond(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).exitCond(this);
		}
	}

	public final CondContext cond() throws RecognitionException {
		CondContext _localctx = new CondContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_cond);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(258);
			expr(0);
			setState(259);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 2139095040L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(260);
			expr(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AssignContext extends ParserRuleContext {
		public  value_attr = str();
		public  type_attr = str();
		public TerminalNode ID() { return getToken(AssignmentStatementParser.ID, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TernaryContext ternary() {
			return getRuleContext(TernaryContext.class,0);
		}
		public AssignContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assign; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).enterAssign(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).exitAssign(this);
		}
	}

	public final AssignContext assign() throws RecognitionException {
		AssignContext _localctx = new AssignContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_assign);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(262);
			match(ID);
			setState(263);
			match(T__20);
			setState(266);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,30,_ctx) ) {
			case 1:
				{
				setState(264);
				expr(0);
				}
				break;
			case 2:
				{
				setState(265);
				ternary();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TernaryContext extends ParserRuleContext {
		public  value_attr = str();
		public  type_attr = str();
		public CondContext cond() {
			return getRuleContext(CondContext.class,0);
		}
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public List<TernaryContext> ternary() {
			return getRuleContexts(TernaryContext.class);
		}
		public TernaryContext ternary(int i) {
			return getRuleContext(TernaryContext.class,i);
		}
		public TernaryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ternary; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).enterTernary(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).exitTernary(this);
		}
	}

	public final TernaryContext ternary() throws RecognitionException {
		TernaryContext _localctx = new TernaryContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_ternary);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(268);
			cond();
			setState(269);
			match(T__30);
			setState(272);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,31,_ctx) ) {
			case 1:
				{
				setState(270);
				expr(0);
				}
				break;
			case 2:
				{
				setState(271);
				ternary();
				}
				break;
			}
			setState(274);
			match(T__2);
			setState(277);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,32,_ctx) ) {
			case 1:
				{
				setState(275);
				expr(0);
				}
				break;
			case 2:
				{
				setState(276);
				ternary();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprContext extends ParserRuleContext {
		public  value_attr = str();
		public  type_attr = str();
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	 
		public ExprContext() { }
		public void copyFrom(ExprContext ctx) {
			super.copyFrom(ctx);
			this.value_attr = ctx.value_attr;
			this.type_attr = ctx.type_attr;
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class Expr_term_minusContext extends ExprContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TermContext term() {
			return getRuleContext(TermContext.class,0);
		}
		public Expr_term_minusContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).enterExpr_term_minus(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).exitExpr_term_minus(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class Expr_term_plusContext extends ExprContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TermContext term() {
			return getRuleContext(TermContext.class,0);
		}
		public Expr_term_plusContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).enterExpr_term_plus(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).exitExpr_term_plus(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class Term4Context extends ExprContext {
		public TermContext term() {
			return getRuleContext(TermContext.class,0);
		}
		public Term4Context(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).enterTerm4(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).exitTerm4(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class Expr_term_relopContext extends ExprContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode RELOP() { return getToken(AssignmentStatementParser.RELOP, 0); }
		public TermContext term() {
			return getRuleContext(TermContext.class,0);
		}
		public Expr_term_relopContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).enterExpr_term_relop(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).exitExpr_term_relop(this);
		}
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 34;
		enterRecursionRule(_localctx, 34, RULE_expr, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			_localctx = new Term4Context(_localctx);
			_ctx = _localctx;
			_prevctx = _localctx;

			setState(280);
			term(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(293);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,34,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(291);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,33,_ctx) ) {
					case 1:
						{
						_localctx = new Expr_term_plusContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(282);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(283);
						match(T__31);
						setState(284);
						term(0);
						}
						break;
					case 2:
						{
						_localctx = new Expr_term_minusContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(285);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(286);
						match(T__32);
						setState(287);
						term(0);
						}
						break;
					case 3:
						{
						_localctx = new Expr_term_relopContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(288);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(289);
						match(RELOP);
						setState(290);
						term(0);
						}
						break;
					}
					} 
				}
				setState(295);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,34,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TermContext extends ParserRuleContext {
		public  value_attr = str();
		public  type_attr = str();
		public TermContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_term; }
	 
		public TermContext() { }
		public void copyFrom(TermContext ctx) {
			super.copyFrom(ctx);
			this.value_attr = ctx.value_attr;
			this.type_attr = ctx.type_attr;
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class Term_fact_divideContext extends TermContext {
		public TermContext term() {
			return getRuleContext(TermContext.class,0);
		}
		public FactorContext factor() {
			return getRuleContext(FactorContext.class,0);
		}
		public Term_fact_divideContext(TermContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).enterTerm_fact_divide(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).exitTerm_fact_divide(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class Term_fact_mutiplyContext extends TermContext {
		public TermContext term() {
			return getRuleContext(TermContext.class,0);
		}
		public FactorContext factor() {
			return getRuleContext(FactorContext.class,0);
		}
		public Term_fact_mutiplyContext(TermContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).enterTerm_fact_mutiply(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).exitTerm_fact_mutiply(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class Factor3Context extends TermContext {
		public FactorContext factor() {
			return getRuleContext(FactorContext.class,0);
		}
		public Factor3Context(TermContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).enterFactor3(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).exitFactor3(this);
		}
	}

	public final TermContext term() throws RecognitionException {
		return term(0);
	}

	private TermContext term(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		TermContext _localctx = new TermContext(_ctx, _parentState);
		TermContext _prevctx = _localctx;
		int _startState = 36;
		enterRecursionRule(_localctx, 36, RULE_term, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			_localctx = new Factor3Context(_localctx);
			_ctx = _localctx;
			_prevctx = _localctx;

			setState(297);
			factor();
			}
			_ctx.stop = _input.LT(-1);
			setState(307);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,36,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(305);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,35,_ctx) ) {
					case 1:
						{
						_localctx = new Term_fact_mutiplyContext(new TermContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_term);
						setState(299);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(300);
						match(T__33);
						setState(301);
						factor();
						}
						break;
					case 2:
						{
						_localctx = new Term_fact_divideContext(new TermContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_term);
						setState(302);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(303);
						match(T__34);
						setState(304);
						factor();
						}
						break;
					}
					} 
				}
				setState(309);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,36,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FactorContext extends ParserRuleContext {
		public  value_attr = str();
		public  type_attr = str();
		public FactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor; }
	 
		public FactorContext() { }
		public void copyFrom(FactorContext ctx) {
			super.copyFrom(ctx);
			this.value_attr = ctx.value_attr;
			this.type_attr = ctx.type_attr;
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class Fact_exprContext extends FactorContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public Fact_exprContext(FactorContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).enterFact_expr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).exitFact_expr(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class Fact_idContext extends FactorContext {
		public TerminalNode ID() { return getToken(AssignmentStatementParser.ID, 0); }
		public Fact_idContext(FactorContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).enterFact_id(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).exitFact_id(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class Fact_numberContext extends FactorContext {
		public NumberContext number() {
			return getRuleContext(NumberContext.class,0);
		}
		public Fact_numberContext(FactorContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).enterFact_number(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).exitFact_number(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class Fact_arrayContext extends FactorContext {
		public ArrayContext array() {
			return getRuleContext(ArrayContext.class,0);
		}
		public Fact_arrayContext(FactorContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).enterFact_array(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).exitFact_array(this);
		}
	}

	public final FactorContext factor() throws RecognitionException {
		FactorContext _localctx = new FactorContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_factor);
		try {
			setState(317);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__14:
				_localctx = new Fact_exprContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(310);
				match(T__14);
				setState(311);
				expr(0);
				setState(312);
				match(T__15);
				}
				break;
			case ID:
				_localctx = new Fact_idContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(314);
				match(ID);
				}
				break;
			case INT:
			case FLOAT:
				_localctx = new Fact_numberContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(315);
				number();
				}
				break;
			case INT_ARRAY:
			case FLOAT_ARRAY:
			case STRING_ARRAY:
				_localctx = new Fact_arrayContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(316);
				array();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class NumberContext extends ParserRuleContext {
		public  value_attr = str();
		public  type_attr = str();
		public NumberContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_number; }
	 
		public NumberContext() { }
		public void copyFrom(NumberContext ctx) {
			super.copyFrom(ctx);
			this.value_attr = ctx.value_attr;
			this.type_attr = ctx.type_attr;
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class Number_floatContext extends NumberContext {
		public TerminalNode FLOAT() { return getToken(AssignmentStatementParser.FLOAT, 0); }
		public Number_floatContext(NumberContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).enterNumber_float(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).exitNumber_float(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class Number_intContext extends NumberContext {
		public TerminalNode INT() { return getToken(AssignmentStatementParser.INT, 0); }
		public Number_intContext(NumberContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).enterNumber_int(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).exitNumber_int(this);
		}
	}

	public final NumberContext number() throws RecognitionException {
		NumberContext _localctx = new NumberContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_number);
		try {
			setState(321);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case FLOAT:
				_localctx = new Number_floatContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(319);
				match(FLOAT);
				}
				break;
			case INT:
				_localctx = new Number_intContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(320);
				match(INT);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ArrayContext extends ParserRuleContext {
		public  value_attr = str();
		public  type_attr = str();
		public ArrayContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_array; }
	 
		public ArrayContext() { }
		public void copyFrom(ArrayContext ctx) {
			super.copyFrom(ctx);
			this.value_attr = ctx.value_attr;
			this.type_attr = ctx.type_attr;
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class Array_floatContext extends ArrayContext {
		public TerminalNode FLOAT_ARRAY() { return getToken(AssignmentStatementParser.FLOAT_ARRAY, 0); }
		public Array_floatContext(ArrayContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).enterArray_float(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).exitArray_float(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class Array_stringContext extends ArrayContext {
		public TerminalNode STRING_ARRAY() { return getToken(AssignmentStatementParser.STRING_ARRAY, 0); }
		public Array_stringContext(ArrayContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).enterArray_string(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).exitArray_string(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class Array_intContext extends ArrayContext {
		public TerminalNode INT_ARRAY() { return getToken(AssignmentStatementParser.INT_ARRAY, 0); }
		public Array_intContext(ArrayContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).enterArray_int(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).exitArray_int(this);
		}
	}

	public final ArrayContext array() throws RecognitionException {
		ArrayContext _localctx = new ArrayContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_array);
		try {
			setState(326);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT_ARRAY:
				_localctx = new Array_intContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(323);
				match(INT_ARRAY);
				}
				break;
			case FLOAT_ARRAY:
				_localctx = new Array_floatContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(324);
				match(FLOAT_ARRAY);
				}
				break;
			case STRING_ARRAY:
				_localctx = new Array_stringContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(325);
				match(STRING_ARRAY);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 17:
			return expr_sempred((ExprContext)_localctx, predIndex);
		case 18:
			return term_sempred((TermContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 4);
		case 1:
			return precpred(_ctx, 3);
		case 2:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean term_sempred(TermContext _localctx, int predIndex) {
		switch (predIndex) {
		case 3:
			return precpred(_ctx, 3);
		case 4:
			return precpred(_ctx, 2);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001/\u0149\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0001\u0000\u0001\u0000\u0005\u0000/\b\u0000\n\u0000\f\u00002\t\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0005\u0001"+
		"9\b\u0001\n\u0001\f\u0001<\t\u0001\u0001\u0001\u0003\u0001?\b\u0001\u0001"+
		"\u0001\u0004\u0001B\b\u0001\u000b\u0001\f\u0001C\u0001\u0001\u0001\u0001"+
		"\u0001\u0002\u0001\u0002\u0005\u0002J\b\u0002\n\u0002\f\u0002M\t\u0002"+
		"\u0001\u0002\u0001\u0002\u0005\u0002Q\b\u0002\n\u0002\f\u0002T\t\u0002"+
		"\u0004\u0002V\b\u0002\u000b\u0002\f\u0002W\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0005"+
		"\u0005b\b\u0005\n\u0005\f\u0005e\t\u0005\u0001\u0005\u0001\u0005\u0004"+
		"\u0005i\b\u0005\u000b\u0005\f\u0005j\u0004\u0005m\b\u0005\u000b\u0005"+
		"\f\u0005n\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0003\u0006y\b\u0006\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0005\u0007\u007f\b\u0007\n\u0007"+
		"\f\u0007\u0082\t\u0007\u0001\u0007\u0001\u0007\u0005\u0007\u0086\b\u0007"+
		"\n\u0007\f\u0007\u0089\t\u0007\u0001\u0007\u0001\u0007\u0005\u0007\u008d"+
		"\b\u0007\n\u0007\f\u0007\u0090\t\u0007\u0001\u0007\u0003\u0007\u0093\b"+
		"\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0005\b\u0099\b\b\n\b\f\b\u009c"+
		"\t\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0005\t\u00a5"+
		"\b\t\n\t\f\t\u00a8\t\t\u0001\t\u0001\t\u0005\t\u00ac\b\t\n\t\f\t\u00af"+
		"\t\t\u0001\t\u0004\t\u00b2\b\t\u000b\t\f\t\u00b3\u0001\t\u0003\t\u00b7"+
		"\b\t\u0001\t\u0005\t\u00ba\b\t\n\t\f\t\u00bd\t\t\u0001\t\u0001\t\u0001"+
		"\n\u0001\n\u0001\n\u0001\n\u0005\n\u00c5\b\n\n\n\f\n\u00c8\t\n\u0001\n"+
		"\u0001\n\u0005\n\u00cc\b\n\n\n\f\n\u00cf\t\n\u0001\n\u0003\n\u00d2\b\n"+
		"\u0001\n\u0005\n\u00d5\b\n\n\n\f\n\u00d8\t\n\u0001\u000b\u0001\u000b\u0001"+
		"\u000b\u0005\u000b\u00dd\b\u000b\n\u000b\f\u000b\u00e0\t\u000b\u0001\u000b"+
		"\u0001\u000b\u0005\u000b\u00e4\b\u000b\n\u000b\f\u000b\u00e7\t\u000b\u0001"+
		"\u000b\u0003\u000b\u00ea\b\u000b\u0001\u000b\u0005\u000b\u00ed\b\u000b"+
		"\n\u000b\f\u000b\u00f0\t\u000b\u0001\f\u0001\f\u0001\r\u0001\r\u0001\r"+
		"\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0005\r\u00fc\b\r\n\r\f\r\u00ff"+
		"\t\r\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001"+
		"\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0003\u000f\u010b\b\u000f\u0001"+
		"\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0003\u0010\u0111\b\u0010\u0001"+
		"\u0010\u0001\u0010\u0001\u0010\u0003\u0010\u0116\b\u0010\u0001\u0011\u0001"+
		"\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001"+
		"\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0005\u0011\u0124"+
		"\b\u0011\n\u0011\f\u0011\u0127\t\u0011\u0001\u0012\u0001\u0012\u0001\u0012"+
		"\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012"+
		"\u0005\u0012\u0132\b\u0012\n\u0012\f\u0012\u0135\t\u0012\u0001\u0013\u0001"+
		"\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0003"+
		"\u0013\u013e\b\u0013\u0001\u0014\u0001\u0014\u0003\u0014\u0142\b\u0014"+
		"\u0001\u0015\u0001\u0015\u0001\u0015\u0003\u0015\u0147\b\u0015\u0001\u0015"+
		"\u0000\u0002\"$\u0016\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012"+
		"\u0014\u0016\u0018\u001a\u001c\u001e \"$&(*\u0000\u0002\u0001\u0000\u0004"+
		"\u0006\u0001\u0000\u0017\u001e\u0162\u0000,\u0001\u0000\u0000\u0000\u0002"+
		"5\u0001\u0000\u0000\u0000\u0004G\u0001\u0000\u0000\u0000\u0006Y\u0001"+
		"\u0000\u0000\u0000\b]\u0001\u0000\u0000\u0000\n_\u0001\u0000\u0000\u0000"+
		"\fx\u0001\u0000\u0000\u0000\u000ez\u0001\u0000\u0000\u0000\u0010\u0094"+
		"\u0001\u0000\u0000\u0000\u0012\u009f\u0001\u0000\u0000\u0000\u0014\u00c0"+
		"\u0001\u0000\u0000\u0000\u0016\u00d9\u0001\u0000\u0000\u0000\u0018\u00f1"+
		"\u0001\u0000\u0000\u0000\u001a\u00f3\u0001\u0000\u0000\u0000\u001c\u0102"+
		"\u0001\u0000\u0000\u0000\u001e\u0106\u0001\u0000\u0000\u0000 \u010c\u0001"+
		"\u0000\u0000\u0000\"\u0117\u0001\u0000\u0000\u0000$\u0128\u0001\u0000"+
		"\u0000\u0000&\u013d\u0001\u0000\u0000\u0000(\u0141\u0001\u0000\u0000\u0000"+
		"*\u0146\u0001\u0000\u0000\u0000,0\u0003\u0002\u0001\u0000-/\u0005.\u0000"+
		"\u0000.-\u0001\u0000\u0000\u0000/2\u0001\u0000\u0000\u00000.\u0001\u0000"+
		"\u0000\u000001\u0001\u0000\u0000\u000013\u0001\u0000\u0000\u000020\u0001"+
		"\u0000\u0000\u000034\u0005\u0000\u0000\u00014\u0001\u0001\u0000\u0000"+
		"\u000056\u0005\u0001\u0000\u00006:\u0005\'\u0000\u000079\u0005.\u0000"+
		"\u000087\u0001\u0000\u0000\u00009<\u0001\u0000\u0000\u0000:8\u0001\u0000"+
		"\u0000\u0000:;\u0001\u0000\u0000\u0000;>\u0001\u0000\u0000\u0000<:\u0001"+
		"\u0000\u0000\u0000=?\u0003\u0004\u0002\u0000>=\u0001\u0000\u0000\u0000"+
		">?\u0001\u0000\u0000\u0000?A\u0001\u0000\u0000\u0000@B\u0005.\u0000\u0000"+
		"A@\u0001\u0000\u0000\u0000BC\u0001\u0000\u0000\u0000CA\u0001\u0000\u0000"+
		"\u0000CD\u0001\u0000\u0000\u0000DE\u0001\u0000\u0000\u0000EF\u0003\n\u0005"+
		"\u0000F\u0003\u0001\u0000\u0000\u0000GK\u0005\u0002\u0000\u0000HJ\u0005"+
		".\u0000\u0000IH\u0001\u0000\u0000\u0000JM\u0001\u0000\u0000\u0000KI\u0001"+
		"\u0000\u0000\u0000KL\u0001\u0000\u0000\u0000LU\u0001\u0000\u0000\u0000"+
		"MK\u0001\u0000\u0000\u0000NR\u0003\u0006\u0003\u0000OQ\u0005.\u0000\u0000"+
		"PO\u0001\u0000\u0000\u0000QT\u0001\u0000\u0000\u0000RP\u0001\u0000\u0000"+
		"\u0000RS\u0001\u0000\u0000\u0000SV\u0001\u0000\u0000\u0000TR\u0001\u0000"+
		"\u0000\u0000UN\u0001\u0000\u0000\u0000VW\u0001\u0000\u0000\u0000WU\u0001"+
		"\u0000\u0000\u0000WX\u0001\u0000\u0000\u0000X\u0005\u0001\u0000\u0000"+
		"\u0000YZ\u0005\'\u0000\u0000Z[\u0005\u0003\u0000\u0000[\\\u0003\b\u0004"+
		"\u0000\\\u0007\u0001\u0000\u0000\u0000]^\u0007\u0000\u0000\u0000^\t\u0001"+
		"\u0000\u0000\u0000_c\u0005\u0007\u0000\u0000`b\u0005.\u0000\u0000a`\u0001"+
		"\u0000\u0000\u0000be\u0001\u0000\u0000\u0000ca\u0001\u0000\u0000\u0000"+
		"cd\u0001\u0000\u0000\u0000dl\u0001\u0000\u0000\u0000ec\u0001\u0000\u0000"+
		"\u0000fh\u0003\f\u0006\u0000gi\u0005.\u0000\u0000hg\u0001\u0000\u0000"+
		"\u0000ij\u0001\u0000\u0000\u0000jh\u0001\u0000\u0000\u0000jk\u0001\u0000"+
		"\u0000\u0000km\u0001\u0000\u0000\u0000lf\u0001\u0000\u0000\u0000mn\u0001"+
		"\u0000\u0000\u0000nl\u0001\u0000\u0000\u0000no\u0001\u0000\u0000\u0000"+
		"op\u0001\u0000\u0000\u0000pq\u0005\b\u0000\u0000q\u000b\u0001\u0000\u0000"+
		"\u0000ry\u0003\u000e\u0007\u0000sy\u0003\u001e\u000f\u0000ty\u0003\n\u0005"+
		"\u0000uy\u0003\u0010\b\u0000vy\u0003\u0012\t\u0000wy\u0003\u001a\r\u0000"+
		"xr\u0001\u0000\u0000\u0000xs\u0001\u0000\u0000\u0000xt\u0001\u0000\u0000"+
		"\u0000xu\u0001\u0000\u0000\u0000xv\u0001\u0000\u0000\u0000xw\u0001\u0000"+
		"\u0000\u0000y\r\u0001\u0000\u0000\u0000z{\u0005\t\u0000\u0000{|\u0003"+
		"\u001c\u000e\u0000|\u0080\u0005\n\u0000\u0000}\u007f\u0005.\u0000\u0000"+
		"~}\u0001\u0000\u0000\u0000\u007f\u0082\u0001\u0000\u0000\u0000\u0080~"+
		"\u0001\u0000\u0000\u0000\u0080\u0081\u0001\u0000\u0000\u0000\u0081\u0083"+
		"\u0001\u0000\u0000\u0000\u0082\u0080\u0001\u0000\u0000\u0000\u0083\u0087"+
		"\u0003\f\u0006\u0000\u0084\u0086\u0005.\u0000\u0000\u0085\u0084\u0001"+
		"\u0000\u0000\u0000\u0086\u0089\u0001\u0000\u0000\u0000\u0087\u0085\u0001"+
		"\u0000\u0000\u0000\u0087\u0088\u0001\u0000\u0000\u0000\u0088\u0092\u0001"+
		"\u0000\u0000\u0000\u0089\u0087\u0001\u0000\u0000\u0000\u008a\u008e\u0005"+
		"\u000b\u0000\u0000\u008b\u008d\u0005.\u0000\u0000\u008c\u008b\u0001\u0000"+
		"\u0000\u0000\u008d\u0090\u0001\u0000\u0000\u0000\u008e\u008c\u0001\u0000"+
		"\u0000\u0000\u008e\u008f\u0001\u0000\u0000\u0000\u008f\u0091\u0001\u0000"+
		"\u0000\u0000\u0090\u008e\u0001\u0000\u0000\u0000\u0091\u0093\u0003\f\u0006"+
		"\u0000\u0092\u008a\u0001\u0000\u0000\u0000\u0092\u0093\u0001\u0000\u0000"+
		"\u0000\u0093\u000f\u0001\u0000\u0000\u0000\u0094\u0095\u0005\f\u0000\u0000"+
		"\u0095\u0096\u0003\u001c\u000e\u0000\u0096\u009a\u0005\r\u0000\u0000\u0097"+
		"\u0099\u0005.\u0000\u0000\u0098\u0097\u0001\u0000\u0000\u0000\u0099\u009c"+
		"\u0001\u0000\u0000\u0000\u009a\u0098\u0001\u0000\u0000\u0000\u009a\u009b"+
		"\u0001\u0000\u0000\u0000\u009b\u009d\u0001\u0000\u0000\u0000\u009c\u009a"+
		"\u0001\u0000\u0000\u0000\u009d\u009e\u0003\f\u0006\u0000\u009e\u0011\u0001"+
		"\u0000\u0000\u0000\u009f\u00a0\u0005\u000e\u0000\u0000\u00a0\u00a1\u0005"+
		"\u000f\u0000\u0000\u00a1\u00a2\u0003\"\u0011\u0000\u00a2\u00a6\u0005\u0010"+
		"\u0000\u0000\u00a3\u00a5\u0005.\u0000\u0000\u00a4\u00a3\u0001\u0000\u0000"+
		"\u0000\u00a5\u00a8\u0001\u0000\u0000\u0000\u00a6\u00a4\u0001\u0000\u0000"+
		"\u0000\u00a6\u00a7\u0001\u0000\u0000\u0000\u00a7\u00a9\u0001\u0000\u0000"+
		"\u0000\u00a8\u00a6\u0001\u0000\u0000\u0000\u00a9\u00ad\u0005\u0007\u0000"+
		"\u0000\u00aa\u00ac\u0005.\u0000\u0000\u00ab\u00aa\u0001\u0000\u0000\u0000"+
		"\u00ac\u00af\u0001\u0000\u0000\u0000\u00ad\u00ab\u0001\u0000\u0000\u0000"+
		"\u00ad\u00ae\u0001\u0000\u0000\u0000\u00ae\u00b1\u0001\u0000\u0000\u0000"+
		"\u00af\u00ad\u0001\u0000\u0000\u0000\u00b0\u00b2\u0003\u0014\n\u0000\u00b1"+
		"\u00b0\u0001\u0000\u0000\u0000\u00b2\u00b3\u0001\u0000\u0000\u0000\u00b3"+
		"\u00b1\u0001\u0000\u0000\u0000\u00b3\u00b4\u0001\u0000\u0000\u0000\u00b4"+
		"\u00b6\u0001\u0000\u0000\u0000\u00b5\u00b7\u0003\u0016\u000b\u0000\u00b6"+
		"\u00b5\u0001\u0000\u0000\u0000\u00b6\u00b7\u0001\u0000\u0000\u0000\u00b7"+
		"\u00bb\u0001\u0000\u0000\u0000\u00b8\u00ba\u0005.\u0000\u0000\u00b9\u00b8"+
		"\u0001\u0000\u0000\u0000\u00ba\u00bd\u0001\u0000\u0000\u0000\u00bb\u00b9"+
		"\u0001\u0000\u0000\u0000\u00bb\u00bc\u0001\u0000\u0000\u0000\u00bc\u00be"+
		"\u0001\u0000\u0000\u0000\u00bd\u00bb\u0001\u0000\u0000\u0000\u00be\u00bf"+
		"\u0005\b\u0000\u0000\u00bf\u0013\u0001\u0000\u0000\u0000\u00c0\u00c1\u0005"+
		"\u0011\u0000\u0000\u00c1\u00c2\u0003\"\u0011\u0000\u00c2\u00c6\u0005\u0003"+
		"\u0000\u0000\u00c3\u00c5\u0005.\u0000\u0000\u00c4\u00c3\u0001\u0000\u0000"+
		"\u0000\u00c5\u00c8\u0001\u0000\u0000\u0000\u00c6\u00c4\u0001\u0000\u0000"+
		"\u0000\u00c6\u00c7\u0001\u0000\u0000\u0000\u00c7\u00c9\u0001\u0000\u0000"+
		"\u0000\u00c8\u00c6\u0001\u0000\u0000\u0000\u00c9\u00cd\u0003\f\u0006\u0000"+
		"\u00ca\u00cc\u0005.\u0000\u0000\u00cb\u00ca\u0001\u0000\u0000\u0000\u00cc"+
		"\u00cf\u0001\u0000\u0000\u0000\u00cd\u00cb\u0001\u0000\u0000\u0000\u00cd"+
		"\u00ce\u0001\u0000\u0000\u0000\u00ce\u00d1\u0001\u0000\u0000\u0000\u00cf"+
		"\u00cd\u0001\u0000\u0000\u0000\u00d0\u00d2\u0003\u0018\f\u0000\u00d1\u00d0"+
		"\u0001\u0000\u0000\u0000\u00d1\u00d2\u0001\u0000\u0000\u0000\u00d2\u00d6"+
		"\u0001\u0000\u0000\u0000\u00d3\u00d5\u0005.\u0000\u0000\u00d4\u00d3\u0001"+
		"\u0000\u0000\u0000\u00d5\u00d8\u0001\u0000\u0000\u0000\u00d6\u00d4\u0001"+
		"\u0000\u0000\u0000\u00d6\u00d7\u0001\u0000\u0000\u0000\u00d7\u0015\u0001"+
		"\u0000\u0000\u0000\u00d8\u00d6\u0001\u0000\u0000\u0000\u00d9\u00da\u0005"+
		"\u0012\u0000\u0000\u00da\u00de\u0005\u0003\u0000\u0000\u00db\u00dd\u0005"+
		".\u0000\u0000\u00dc\u00db\u0001\u0000\u0000\u0000\u00dd\u00e0\u0001\u0000"+
		"\u0000\u0000\u00de\u00dc\u0001\u0000\u0000\u0000\u00de\u00df\u0001\u0000"+
		"\u0000\u0000\u00df\u00e1\u0001\u0000\u0000\u0000\u00e0\u00de\u0001\u0000"+
		"\u0000\u0000\u00e1\u00e5\u0003\f\u0006\u0000\u00e2\u00e4\u0005.\u0000"+
		"\u0000\u00e3\u00e2\u0001\u0000\u0000\u0000\u00e4\u00e7\u0001\u0000\u0000"+
		"\u0000\u00e5\u00e3\u0001\u0000\u0000\u0000\u00e5\u00e6\u0001\u0000\u0000"+
		"\u0000\u00e6\u00e9\u0001\u0000\u0000\u0000\u00e7\u00e5\u0001\u0000\u0000"+
		"\u0000\u00e8\u00ea\u0003\u0018\f\u0000\u00e9\u00e8\u0001\u0000\u0000\u0000"+
		"\u00e9\u00ea\u0001\u0000\u0000\u0000\u00ea\u00ee\u0001\u0000\u0000\u0000"+
		"\u00eb\u00ed\u0005.\u0000\u0000\u00ec\u00eb\u0001\u0000\u0000\u0000\u00ed"+
		"\u00f0\u0001\u0000\u0000\u0000\u00ee\u00ec\u0001\u0000\u0000\u0000\u00ee"+
		"\u00ef\u0001\u0000\u0000\u0000\u00ef\u0017\u0001\u0000\u0000\u0000\u00f0"+
		"\u00ee\u0001\u0000\u0000\u0000\u00f1\u00f2\u0005\u0013\u0000\u0000\u00f2"+
		"\u0019\u0001\u0000\u0000\u0000\u00f3\u00f4\u0005\u0014\u0000\u0000\u00f4"+
		"\u00f5\u0005\'\u0000\u0000\u00f5\u00f6\u0005\u0015\u0000\u0000\u00f6\u00f7"+
		"\u0003\"\u0011\u0000\u00f7\u00f8\u0005\u0016\u0000\u0000\u00f8\u00f9\u0003"+
		"\"\u0011\u0000\u00f9\u00fd\u0005\r\u0000\u0000\u00fa\u00fc\u0005.\u0000"+
		"\u0000\u00fb\u00fa\u0001\u0000\u0000\u0000\u00fc\u00ff\u0001\u0000\u0000"+
		"\u0000\u00fd\u00fb\u0001\u0000\u0000\u0000\u00fd\u00fe\u0001\u0000\u0000"+
		"\u0000\u00fe\u0100\u0001\u0000\u0000\u0000\u00ff\u00fd\u0001\u0000\u0000"+
		"\u0000\u0100\u0101\u0003\f\u0006\u0000\u0101\u001b\u0001\u0000\u0000\u0000"+
		"\u0102\u0103\u0003\"\u0011\u0000\u0103\u0104\u0007\u0001\u0000\u0000\u0104"+
		"\u0105\u0003\"\u0011\u0000\u0105\u001d\u0001\u0000\u0000\u0000\u0106\u0107"+
		"\u0005\'\u0000\u0000\u0107\u010a\u0005\u0015\u0000\u0000\u0108\u010b\u0003"+
		"\"\u0011\u0000\u0109\u010b\u0003 \u0010\u0000\u010a\u0108\u0001\u0000"+
		"\u0000\u0000\u010a\u0109\u0001\u0000\u0000\u0000\u010b\u001f\u0001\u0000"+
		"\u0000\u0000\u010c\u010d\u0003\u001c\u000e\u0000\u010d\u0110\u0005\u001f"+
		"\u0000\u0000\u010e\u0111\u0003\"\u0011\u0000\u010f\u0111\u0003 \u0010"+
		"\u0000\u0110\u010e\u0001\u0000\u0000\u0000\u0110\u010f\u0001\u0000\u0000"+
		"\u0000\u0111\u0112\u0001\u0000\u0000\u0000\u0112\u0115\u0005\u0003\u0000"+
		"\u0000\u0113\u0116\u0003\"\u0011\u0000\u0114\u0116\u0003 \u0010\u0000"+
		"\u0115\u0113\u0001\u0000\u0000\u0000\u0115\u0114\u0001\u0000\u0000\u0000"+
		"\u0116!\u0001\u0000\u0000\u0000\u0117\u0118\u0006\u0011\uffff\uffff\u0000"+
		"\u0118\u0119\u0003$\u0012\u0000\u0119\u0125\u0001\u0000\u0000\u0000\u011a"+
		"\u011b\n\u0004\u0000\u0000\u011b\u011c\u0005 \u0000\u0000\u011c\u0124"+
		"\u0003$\u0012\u0000\u011d\u011e\n\u0003\u0000\u0000\u011e\u011f\u0005"+
		"!\u0000\u0000\u011f\u0124\u0003$\u0012\u0000\u0120\u0121\n\u0002\u0000"+
		"\u0000\u0121\u0122\u0005/\u0000\u0000\u0122\u0124\u0003$\u0012\u0000\u0123"+
		"\u011a\u0001\u0000\u0000\u0000\u0123\u011d\u0001\u0000\u0000\u0000\u0123"+
		"\u0120\u0001\u0000\u0000\u0000\u0124\u0127\u0001\u0000\u0000\u0000\u0125"+
		"\u0123\u0001\u0000\u0000\u0000\u0125\u0126\u0001\u0000\u0000\u0000\u0126"+
		"#\u0001\u0000\u0000\u0000\u0127\u0125\u0001\u0000\u0000\u0000\u0128\u0129"+
		"\u0006\u0012\uffff\uffff\u0000\u0129\u012a\u0003&\u0013\u0000\u012a\u0133"+
		"\u0001\u0000\u0000\u0000\u012b\u012c\n\u0003\u0000\u0000\u012c\u012d\u0005"+
		"\"\u0000\u0000\u012d\u0132\u0003&\u0013\u0000\u012e\u012f\n\u0002\u0000"+
		"\u0000\u012f\u0130\u0005#\u0000\u0000\u0130\u0132\u0003&\u0013\u0000\u0131"+
		"\u012b\u0001\u0000\u0000\u0000\u0131\u012e\u0001\u0000\u0000\u0000\u0132"+
		"\u0135\u0001\u0000\u0000\u0000\u0133\u0131\u0001\u0000\u0000\u0000\u0133"+
		"\u0134\u0001\u0000\u0000\u0000\u0134%\u0001\u0000\u0000\u0000\u0135\u0133"+
		"\u0001\u0000\u0000\u0000\u0136\u0137\u0005\u000f\u0000\u0000\u0137\u0138"+
		"\u0003\"\u0011\u0000\u0138\u0139\u0005\u0010\u0000\u0000\u0139\u013e\u0001"+
		"\u0000\u0000\u0000\u013a\u013e\u0005\'\u0000\u0000\u013b\u013e\u0003("+
		"\u0014\u0000\u013c\u013e\u0003*\u0015\u0000\u013d\u0136\u0001\u0000\u0000"+
		"\u0000\u013d\u013a\u0001\u0000\u0000\u0000\u013d\u013b\u0001\u0000\u0000"+
		"\u0000\u013d\u013c\u0001\u0000\u0000\u0000\u013e\'\u0001\u0000\u0000\u0000"+
		"\u013f\u0142\u0005%\u0000\u0000\u0140\u0142\u0005$\u0000\u0000\u0141\u013f"+
		"\u0001\u0000\u0000\u0000\u0141\u0140\u0001\u0000\u0000\u0000\u0142)\u0001"+
		"\u0000\u0000\u0000\u0143\u0147\u0005)\u0000\u0000\u0144\u0147\u0005*\u0000"+
		"\u0000\u0145\u0147\u0005+\u0000\u0000\u0146\u0143\u0001\u0000\u0000\u0000"+
		"\u0146\u0144\u0001\u0000\u0000\u0000\u0146\u0145\u0001\u0000\u0000\u0000"+
		"\u0147+\u0001\u0000\u0000\u0000(0:>CKRWcjnx\u0080\u0087\u008e\u0092\u009a"+
		"\u00a6\u00ad\u00b3\u00b6\u00bb\u00c6\u00cd\u00d1\u00d6\u00de\u00e5\u00e9"+
		"\u00ee\u00fd\u010a\u0110\u0115\u0123\u0125\u0131\u0133\u013d\u0141\u0146";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}