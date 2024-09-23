// Generated from e:/uni/7th term/fundamentals of compiler design/classHWs/IL1/AssignmentStatement.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class AssignmentStatementLexer extends Lexer {
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
		ARRAY_TYPE=40, INT_ARRAY=41, FLOAT_ARRAY=42, STRING_ARRAY=43, WS=44, NEWLINE=45, 
		RELOP=46;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "T__8", 
			"T__9", "T__10", "T__11", "T__12", "T__13", "T__14", "T__15", "T__16", 
			"T__17", "T__18", "T__19", "T__20", "T__21", "T__22", "T__23", "T__24", 
			"T__25", "T__26", "T__27", "T__28", "T__29", "T__30", "T__31", "T__32", 
			"T__33", "T__34", "INT", "FLOAT", "String", "ID", "ARRAY_TYPE", "INT_ARRAY", 
			"FLOAT_ARRAY", "STRING_ARRAY", "DIGIT", "LETTER", "ESC", "WS", "NEWLINE", 
			"RELOP"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'program'", "'var'", "':'", "'float'", "'int'", "'string'", "'begin'", 
			"'end'", "'if'", "'then'", "'else'", "'while'", "'do'", "'switch'", "'('", 
			"')'", "'{'", "'}'", "'case'", "'for'", "':='", "'to'", "'>'", "'<'", 
			"'=='", "'!='", "'<='", "'>='", "'&&'", "'||'", "'?'", "'+'", "'-'", 
			"'*'", "'/'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			"INT", "FLOAT", "String", "ID", "ARRAY_TYPE", "INT_ARRAY", "FLOAT_ARRAY", 
			"STRING_ARRAY", "WS", "NEWLINE", "RELOP"
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


	public AssignmentStatementLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "AssignmentStatement.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000.\u014d\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002"+
		"\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002"+
		"\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002"+
		"\u0015\u0007\u0015\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002"+
		"\u0018\u0007\u0018\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0002"+
		"\u001b\u0007\u001b\u0002\u001c\u0007\u001c\u0002\u001d\u0007\u001d\u0002"+
		"\u001e\u0007\u001e\u0002\u001f\u0007\u001f\u0002 \u0007 \u0002!\u0007"+
		"!\u0002\"\u0007\"\u0002#\u0007#\u0002$\u0007$\u0002%\u0007%\u0002&\u0007"+
		"&\u0002\'\u0007\'\u0002(\u0007(\u0002)\u0007)\u0002*\u0007*\u0002+\u0007"+
		"+\u0002,\u0007,\u0002-\u0007-\u0002.\u0007.\u0002/\u0007/\u00020\u0007"+
		"0\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001"+
		"\b\u0001\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001"+
		"\n\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001"+
		"\u000b\u0001\u000b\u0001\f\u0001\f\u0001\f\u0001\r\u0001\r\u0001\r\u0001"+
		"\r\u0001\r\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f"+
		"\u0001\u0010\u0001\u0010\u0001\u0011\u0001\u0011\u0001\u0012\u0001\u0012"+
		"\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0013\u0001\u0013\u0001\u0013"+
		"\u0001\u0013\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0015\u0001\u0015"+
		"\u0001\u0015\u0001\u0016\u0001\u0016\u0001\u0017\u0001\u0017\u0001\u0018"+
		"\u0001\u0018\u0001\u0018\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u001a"+
		"\u0001\u001a\u0001\u001a\u0001\u001b\u0001\u001b\u0001\u001b\u0001\u001c"+
		"\u0001\u001c\u0001\u001c\u0001\u001d\u0001\u001d\u0001\u001d\u0001\u001e"+
		"\u0001\u001e\u0001\u001f\u0001\u001f\u0001 \u0001 \u0001!\u0001!\u0001"+
		"\"\u0001\"\u0001#\u0004#\u00e2\b#\u000b#\f#\u00e3\u0001$\u0004$\u00e7"+
		"\b$\u000b$\f$\u00e8\u0001$\u0001$\u0005$\u00ed\b$\n$\f$\u00f0\t$\u0001"+
		"$\u0001$\u0004$\u00f4\b$\u000b$\f$\u00f5\u0003$\u00f8\b$\u0001%\u0001"+
		"%\u0001%\u0005%\u00fd\b%\n%\f%\u0100\t%\u0001%\u0001%\u0001&\u0001&\u0001"+
		"&\u0005&\u0107\b&\n&\f&\u010a\t&\u0001\'\u0001\'\u0001\'\u0001\'\u0001"+
		"\'\u0001(\u0001(\u0001(\u0001(\u0005(\u0115\b(\n(\f(\u0118\t(\u0001(\u0001"+
		"(\u0001)\u0001)\u0001)\u0001)\u0005)\u0120\b)\n)\f)\u0123\t)\u0001)\u0001"+
		")\u0001*\u0001*\u0001*\u0001*\u0005*\u012b\b*\n*\f*\u012e\t*\u0001*\u0001"+
		"*\u0001+\u0001+\u0001,\u0001,\u0001-\u0001-\u0001-\u0001-\u0003-\u013a"+
		"\b-\u0001.\u0004.\u013d\b.\u000b.\f.\u013e\u0001.\u0001.\u0001/\u0001"+
		"/\u0001/\u0001/\u0003/\u0147\b/\u00010\u00010\u00010\u00030\u014c\b0\u0001"+
		"\u00fe\u00001\u0001\u0001\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005"+
		"\u000b\u0006\r\u0007\u000f\b\u0011\t\u0013\n\u0015\u000b\u0017\f\u0019"+
		"\r\u001b\u000e\u001d\u000f\u001f\u0010!\u0011#\u0012%\u0013\'\u0014)\u0015"+
		"+\u0016-\u0017/\u00181\u00193\u001a5\u001b7\u001c9\u001d;\u001e=\u001f"+
		"? A!C\"E#G$I%K&M\'O(Q)S*U+W\u0000Y\u0000[\u0000],_-a.\u0001\u0000\u0003"+
		"\u0001\u000009\u0002\u0000AZaz\u0003\u0000\t\t\r\r  \u015a\u0000\u0001"+
		"\u0001\u0000\u0000\u0000\u0000\u0003\u0001\u0000\u0000\u0000\u0000\u0005"+
		"\u0001\u0000\u0000\u0000\u0000\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001"+
		"\u0000\u0000\u0000\u0000\u000b\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000"+
		"\u0000\u0000\u0000\u000f\u0001\u0000\u0000\u0000\u0000\u0011\u0001\u0000"+
		"\u0000\u0000\u0000\u0013\u0001\u0000\u0000\u0000\u0000\u0015\u0001\u0000"+
		"\u0000\u0000\u0000\u0017\u0001\u0000\u0000\u0000\u0000\u0019\u0001\u0000"+
		"\u0000\u0000\u0000\u001b\u0001\u0000\u0000\u0000\u0000\u001d\u0001\u0000"+
		"\u0000\u0000\u0000\u001f\u0001\u0000\u0000\u0000\u0000!\u0001\u0000\u0000"+
		"\u0000\u0000#\u0001\u0000\u0000\u0000\u0000%\u0001\u0000\u0000\u0000\u0000"+
		"\'\u0001\u0000\u0000\u0000\u0000)\u0001\u0000\u0000\u0000\u0000+\u0001"+
		"\u0000\u0000\u0000\u0000-\u0001\u0000\u0000\u0000\u0000/\u0001\u0000\u0000"+
		"\u0000\u00001\u0001\u0000\u0000\u0000\u00003\u0001\u0000\u0000\u0000\u0000"+
		"5\u0001\u0000\u0000\u0000\u00007\u0001\u0000\u0000\u0000\u00009\u0001"+
		"\u0000\u0000\u0000\u0000;\u0001\u0000\u0000\u0000\u0000=\u0001\u0000\u0000"+
		"\u0000\u0000?\u0001\u0000\u0000\u0000\u0000A\u0001\u0000\u0000\u0000\u0000"+
		"C\u0001\u0000\u0000\u0000\u0000E\u0001\u0000\u0000\u0000\u0000G\u0001"+
		"\u0000\u0000\u0000\u0000I\u0001\u0000\u0000\u0000\u0000K\u0001\u0000\u0000"+
		"\u0000\u0000M\u0001\u0000\u0000\u0000\u0000O\u0001\u0000\u0000\u0000\u0000"+
		"Q\u0001\u0000\u0000\u0000\u0000S\u0001\u0000\u0000\u0000\u0000U\u0001"+
		"\u0000\u0000\u0000\u0000]\u0001\u0000\u0000\u0000\u0000_\u0001\u0000\u0000"+
		"\u0000\u0000a\u0001\u0000\u0000\u0000\u0001c\u0001\u0000\u0000\u0000\u0003"+
		"k\u0001\u0000\u0000\u0000\u0005o\u0001\u0000\u0000\u0000\u0007q\u0001"+
		"\u0000\u0000\u0000\tw\u0001\u0000\u0000\u0000\u000b{\u0001\u0000\u0000"+
		"\u0000\r\u0082\u0001\u0000\u0000\u0000\u000f\u0088\u0001\u0000\u0000\u0000"+
		"\u0011\u008c\u0001\u0000\u0000\u0000\u0013\u008f\u0001\u0000\u0000\u0000"+
		"\u0015\u0094\u0001\u0000\u0000\u0000\u0017\u0099\u0001\u0000\u0000\u0000"+
		"\u0019\u009f\u0001\u0000\u0000\u0000\u001b\u00a2\u0001\u0000\u0000\u0000"+
		"\u001d\u00a9\u0001\u0000\u0000\u0000\u001f\u00ab\u0001\u0000\u0000\u0000"+
		"!\u00ad\u0001\u0000\u0000\u0000#\u00af\u0001\u0000\u0000\u0000%\u00b1"+
		"\u0001\u0000\u0000\u0000\'\u00b6\u0001\u0000\u0000\u0000)\u00ba\u0001"+
		"\u0000\u0000\u0000+\u00bd\u0001\u0000\u0000\u0000-\u00c0\u0001\u0000\u0000"+
		"\u0000/\u00c2\u0001\u0000\u0000\u00001\u00c4\u0001\u0000\u0000\u00003"+
		"\u00c7\u0001\u0000\u0000\u00005\u00ca\u0001\u0000\u0000\u00007\u00cd\u0001"+
		"\u0000\u0000\u00009\u00d0\u0001\u0000\u0000\u0000;\u00d3\u0001\u0000\u0000"+
		"\u0000=\u00d6\u0001\u0000\u0000\u0000?\u00d8\u0001\u0000\u0000\u0000A"+
		"\u00da\u0001\u0000\u0000\u0000C\u00dc\u0001\u0000\u0000\u0000E\u00de\u0001"+
		"\u0000\u0000\u0000G\u00e1\u0001\u0000\u0000\u0000I\u00f7\u0001\u0000\u0000"+
		"\u0000K\u00f9\u0001\u0000\u0000\u0000M\u0103\u0001\u0000\u0000\u0000O"+
		"\u010b\u0001\u0000\u0000\u0000Q\u0110\u0001\u0000\u0000\u0000S\u011b\u0001"+
		"\u0000\u0000\u0000U\u0126\u0001\u0000\u0000\u0000W\u0131\u0001\u0000\u0000"+
		"\u0000Y\u0133\u0001\u0000\u0000\u0000[\u0139\u0001\u0000\u0000\u0000]"+
		"\u013c\u0001\u0000\u0000\u0000_\u0146\u0001\u0000\u0000\u0000a\u014b\u0001"+
		"\u0000\u0000\u0000cd\u0005p\u0000\u0000de\u0005r\u0000\u0000ef\u0005o"+
		"\u0000\u0000fg\u0005g\u0000\u0000gh\u0005r\u0000\u0000hi\u0005a\u0000"+
		"\u0000ij\u0005m\u0000\u0000j\u0002\u0001\u0000\u0000\u0000kl\u0005v\u0000"+
		"\u0000lm\u0005a\u0000\u0000mn\u0005r\u0000\u0000n\u0004\u0001\u0000\u0000"+
		"\u0000op\u0005:\u0000\u0000p\u0006\u0001\u0000\u0000\u0000qr\u0005f\u0000"+
		"\u0000rs\u0005l\u0000\u0000st\u0005o\u0000\u0000tu\u0005a\u0000\u0000"+
		"uv\u0005t\u0000\u0000v\b\u0001\u0000\u0000\u0000wx\u0005i\u0000\u0000"+
		"xy\u0005n\u0000\u0000yz\u0005t\u0000\u0000z\n\u0001\u0000\u0000\u0000"+
		"{|\u0005s\u0000\u0000|}\u0005t\u0000\u0000}~\u0005r\u0000\u0000~\u007f"+
		"\u0005i\u0000\u0000\u007f\u0080\u0005n\u0000\u0000\u0080\u0081\u0005g"+
		"\u0000\u0000\u0081\f\u0001\u0000\u0000\u0000\u0082\u0083\u0005b\u0000"+
		"\u0000\u0083\u0084\u0005e\u0000\u0000\u0084\u0085\u0005g\u0000\u0000\u0085"+
		"\u0086\u0005i\u0000\u0000\u0086\u0087\u0005n\u0000\u0000\u0087\u000e\u0001"+
		"\u0000\u0000\u0000\u0088\u0089\u0005e\u0000\u0000\u0089\u008a\u0005n\u0000"+
		"\u0000\u008a\u008b\u0005d\u0000\u0000\u008b\u0010\u0001\u0000\u0000\u0000"+
		"\u008c\u008d\u0005i\u0000\u0000\u008d\u008e\u0005f\u0000\u0000\u008e\u0012"+
		"\u0001\u0000\u0000\u0000\u008f\u0090\u0005t\u0000\u0000\u0090\u0091\u0005"+
		"h\u0000\u0000\u0091\u0092\u0005e\u0000\u0000\u0092\u0093\u0005n\u0000"+
		"\u0000\u0093\u0014\u0001\u0000\u0000\u0000\u0094\u0095\u0005e\u0000\u0000"+
		"\u0095\u0096\u0005l\u0000\u0000\u0096\u0097\u0005s\u0000\u0000\u0097\u0098"+
		"\u0005e\u0000\u0000\u0098\u0016\u0001\u0000\u0000\u0000\u0099\u009a\u0005"+
		"w\u0000\u0000\u009a\u009b\u0005h\u0000\u0000\u009b\u009c\u0005i\u0000"+
		"\u0000\u009c\u009d\u0005l\u0000\u0000\u009d\u009e\u0005e\u0000\u0000\u009e"+
		"\u0018\u0001\u0000\u0000\u0000\u009f\u00a0\u0005d\u0000\u0000\u00a0\u00a1"+
		"\u0005o\u0000\u0000\u00a1\u001a\u0001\u0000\u0000\u0000\u00a2\u00a3\u0005"+
		"s\u0000\u0000\u00a3\u00a4\u0005w\u0000\u0000\u00a4\u00a5\u0005i\u0000"+
		"\u0000\u00a5\u00a6\u0005t\u0000\u0000\u00a6\u00a7\u0005c\u0000\u0000\u00a7"+
		"\u00a8\u0005h\u0000\u0000\u00a8\u001c\u0001\u0000\u0000\u0000\u00a9\u00aa"+
		"\u0005(\u0000\u0000\u00aa\u001e\u0001\u0000\u0000\u0000\u00ab\u00ac\u0005"+
		")\u0000\u0000\u00ac \u0001\u0000\u0000\u0000\u00ad\u00ae\u0005{\u0000"+
		"\u0000\u00ae\"\u0001\u0000\u0000\u0000\u00af\u00b0\u0005}\u0000\u0000"+
		"\u00b0$\u0001\u0000\u0000\u0000\u00b1\u00b2\u0005c\u0000\u0000\u00b2\u00b3"+
		"\u0005a\u0000\u0000\u00b3\u00b4\u0005s\u0000\u0000\u00b4\u00b5\u0005e"+
		"\u0000\u0000\u00b5&\u0001\u0000\u0000\u0000\u00b6\u00b7\u0005f\u0000\u0000"+
		"\u00b7\u00b8\u0005o\u0000\u0000\u00b8\u00b9\u0005r\u0000\u0000\u00b9("+
		"\u0001\u0000\u0000\u0000\u00ba\u00bb\u0005:\u0000\u0000\u00bb\u00bc\u0005"+
		"=\u0000\u0000\u00bc*\u0001\u0000\u0000\u0000\u00bd\u00be\u0005t\u0000"+
		"\u0000\u00be\u00bf\u0005o\u0000\u0000\u00bf,\u0001\u0000\u0000\u0000\u00c0"+
		"\u00c1\u0005>\u0000\u0000\u00c1.\u0001\u0000\u0000\u0000\u00c2\u00c3\u0005"+
		"<\u0000\u0000\u00c30\u0001\u0000\u0000\u0000\u00c4\u00c5\u0005=\u0000"+
		"\u0000\u00c5\u00c6\u0005=\u0000\u0000\u00c62\u0001\u0000\u0000\u0000\u00c7"+
		"\u00c8\u0005!\u0000\u0000\u00c8\u00c9\u0005=\u0000\u0000\u00c94\u0001"+
		"\u0000\u0000\u0000\u00ca\u00cb\u0005<\u0000\u0000\u00cb\u00cc\u0005=\u0000"+
		"\u0000\u00cc6\u0001\u0000\u0000\u0000\u00cd\u00ce\u0005>\u0000\u0000\u00ce"+
		"\u00cf\u0005=\u0000\u0000\u00cf8\u0001\u0000\u0000\u0000\u00d0\u00d1\u0005"+
		"&\u0000\u0000\u00d1\u00d2\u0005&\u0000\u0000\u00d2:\u0001\u0000\u0000"+
		"\u0000\u00d3\u00d4\u0005|\u0000\u0000\u00d4\u00d5\u0005|\u0000\u0000\u00d5"+
		"<\u0001\u0000\u0000\u0000\u00d6\u00d7\u0005?\u0000\u0000\u00d7>\u0001"+
		"\u0000\u0000\u0000\u00d8\u00d9\u0005+\u0000\u0000\u00d9@\u0001\u0000\u0000"+
		"\u0000\u00da\u00db\u0005-\u0000\u0000\u00dbB\u0001\u0000\u0000\u0000\u00dc"+
		"\u00dd\u0005*\u0000\u0000\u00ddD\u0001\u0000\u0000\u0000\u00de\u00df\u0005"+
		"/\u0000\u0000\u00dfF\u0001\u0000\u0000\u0000\u00e0\u00e2\u0003W+\u0000"+
		"\u00e1\u00e0\u0001\u0000\u0000\u0000\u00e2\u00e3\u0001\u0000\u0000\u0000"+
		"\u00e3\u00e1\u0001\u0000\u0000\u0000\u00e3\u00e4\u0001\u0000\u0000\u0000"+
		"\u00e4H\u0001\u0000\u0000\u0000\u00e5\u00e7\u0003W+\u0000\u00e6\u00e5"+
		"\u0001\u0000\u0000\u0000\u00e7\u00e8\u0001\u0000\u0000\u0000\u00e8\u00e6"+
		"\u0001\u0000\u0000\u0000\u00e8\u00e9\u0001\u0000\u0000\u0000\u00e9\u00ea"+
		"\u0001\u0000\u0000\u0000\u00ea\u00ee\u0005.\u0000\u0000\u00eb\u00ed\u0003"+
		"W+\u0000\u00ec\u00eb\u0001\u0000\u0000\u0000\u00ed\u00f0\u0001\u0000\u0000"+
		"\u0000\u00ee\u00ec\u0001\u0000\u0000\u0000\u00ee\u00ef\u0001\u0000\u0000"+
		"\u0000\u00ef\u00f8\u0001\u0000\u0000\u0000\u00f0\u00ee\u0001\u0000\u0000"+
		"\u0000\u00f1\u00f3\u0005.\u0000\u0000\u00f2\u00f4\u0003W+\u0000\u00f3"+
		"\u00f2\u0001\u0000\u0000\u0000\u00f4\u00f5\u0001\u0000\u0000\u0000\u00f5"+
		"\u00f3\u0001\u0000\u0000\u0000\u00f5\u00f6\u0001\u0000\u0000\u0000\u00f6"+
		"\u00f8\u0001\u0000\u0000\u0000\u00f7\u00e6\u0001\u0000\u0000\u0000\u00f7"+
		"\u00f1\u0001\u0000\u0000\u0000\u00f8J\u0001\u0000\u0000\u0000\u00f9\u00fe"+
		"\u0005\"\u0000\u0000\u00fa\u00fd\u0003[-\u0000\u00fb\u00fd\t\u0000\u0000"+
		"\u0000\u00fc\u00fa\u0001\u0000\u0000\u0000\u00fc\u00fb\u0001\u0000\u0000"+
		"\u0000\u00fd\u0100\u0001\u0000\u0000\u0000\u00fe\u00ff\u0001\u0000\u0000"+
		"\u0000\u00fe\u00fc\u0001\u0000\u0000\u0000\u00ff\u0101\u0001\u0000\u0000"+
		"\u0000\u0100\u00fe\u0001\u0000\u0000\u0000\u0101\u0102\u0005\"\u0000\u0000"+
		"\u0102L\u0001\u0000\u0000\u0000\u0103\u0108\u0003Y,\u0000\u0104\u0107"+
		"\u0003Y,\u0000\u0105\u0107\u0003W+\u0000\u0106\u0104\u0001\u0000\u0000"+
		"\u0000\u0106\u0105\u0001\u0000\u0000\u0000\u0107\u010a\u0001\u0000\u0000"+
		"\u0000\u0108\u0106\u0001\u0000\u0000\u0000\u0108\u0109\u0001\u0000\u0000"+
		"\u0000\u0109N\u0001\u0000\u0000\u0000\u010a\u0108\u0001\u0000\u0000\u0000"+
		"\u010b\u010c\u0003M&\u0000\u010c\u010d\u0005[\u0000\u0000\u010d\u010e"+
		"\u0003G#\u0000\u010e\u010f\u0005]\u0000\u0000\u010fP\u0001\u0000\u0000"+
		"\u0000\u0110\u0111\u0005[\u0000\u0000\u0111\u0116\u0003G#\u0000\u0112"+
		"\u0113\u0005,\u0000\u0000\u0113\u0115\u0003G#\u0000\u0114\u0112\u0001"+
		"\u0000\u0000\u0000\u0115\u0118\u0001\u0000\u0000\u0000\u0116\u0114\u0001"+
		"\u0000\u0000\u0000\u0116\u0117\u0001\u0000\u0000\u0000\u0117\u0119\u0001"+
		"\u0000\u0000\u0000\u0118\u0116\u0001\u0000\u0000\u0000\u0119\u011a\u0005"+
		"]\u0000\u0000\u011aR\u0001\u0000\u0000\u0000\u011b\u011c\u0005[\u0000"+
		"\u0000\u011c\u0121\u0003I$\u0000\u011d\u011e\u0005,\u0000\u0000\u011e"+
		"\u0120\u0003I$\u0000\u011f\u011d\u0001\u0000\u0000\u0000\u0120\u0123\u0001"+
		"\u0000\u0000\u0000\u0121\u011f\u0001\u0000\u0000\u0000\u0121\u0122\u0001"+
		"\u0000\u0000\u0000\u0122\u0124\u0001\u0000\u0000\u0000\u0123\u0121\u0001"+
		"\u0000\u0000\u0000\u0124\u0125\u0005]\u0000\u0000\u0125T\u0001\u0000\u0000"+
		"\u0000\u0126\u0127\u0005[\u0000\u0000\u0127\u012c\u0003K%\u0000\u0128"+
		"\u0129\u0005,\u0000\u0000\u0129\u012b\u0003K%\u0000\u012a\u0128\u0001"+
		"\u0000\u0000\u0000\u012b\u012e\u0001\u0000\u0000\u0000\u012c\u012a\u0001"+
		"\u0000\u0000\u0000\u012c\u012d\u0001\u0000\u0000\u0000\u012d\u012f\u0001"+
		"\u0000\u0000\u0000\u012e\u012c\u0001\u0000\u0000\u0000\u012f\u0130\u0005"+
		"]\u0000\u0000\u0130V\u0001\u0000\u0000\u0000\u0131\u0132\u0007\u0000\u0000"+
		"\u0000\u0132X\u0001\u0000\u0000\u0000\u0133\u0134\u0007\u0001\u0000\u0000"+
		"\u0134Z\u0001\u0000\u0000\u0000\u0135\u0136\u0005\\\u0000\u0000\u0136"+
		"\u013a\u0005\"\u0000\u0000\u0137\u0138\u0005\\\u0000\u0000\u0138\u013a"+
		"\u0005\\\u0000\u0000\u0139\u0135\u0001\u0000\u0000\u0000\u0139\u0137\u0001"+
		"\u0000\u0000\u0000\u013a\\\u0001\u0000\u0000\u0000\u013b\u013d\u0007\u0002"+
		"\u0000\u0000\u013c\u013b\u0001\u0000\u0000\u0000\u013d\u013e\u0001\u0000"+
		"\u0000\u0000\u013e\u013c\u0001\u0000\u0000\u0000\u013e\u013f\u0001\u0000"+
		"\u0000\u0000\u013f\u0140\u0001\u0000\u0000\u0000\u0140\u0141\u0006.\u0000"+
		"\u0000\u0141^\u0001\u0000\u0000\u0000\u0142\u0147\u0005\n\u0000\u0000"+
		"\u0143\u0144\u0005\r\u0000\u0000\u0144\u0147\u0005\n\u0000\u0000\u0145"+
		"\u0147\u0005\r\u0000\u0000\u0146\u0142\u0001\u0000\u0000\u0000\u0146\u0143"+
		"\u0001\u0000\u0000\u0000\u0146\u0145\u0001\u0000\u0000\u0000\u0147`\u0001"+
		"\u0000\u0000\u0000\u0148\u0149\u0005<\u0000\u0000\u0149\u014c\u0005=\u0000"+
		"\u0000\u014a\u014c\u0005<\u0000\u0000\u014b\u0148\u0001\u0000\u0000\u0000"+
		"\u014b\u014a\u0001\u0000\u0000\u0000\u014cb\u0001\u0000\u0000\u0000\u0011"+
		"\u0000\u00e3\u00e8\u00ee\u00f5\u00f7\u00fc\u00fe\u0106\u0108\u0116\u0121"+
		"\u012c\u0139\u013e\u0146\u014b\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}