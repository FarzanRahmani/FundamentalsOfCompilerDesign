grammar chaloosOotagh;

start :
      prog NEWLINE* EOF ;

prog :
      NEWLINE* declaration? NEWLINE* (statement NEWLINE*)+;
//      NEWLINE* declaration? NEWLINE* (statement NEWLINE*)*;

declaration :
      NEWLINE* (variable_declaration NEWLINE*)+ ;

variable_declaration :
      type NEWLINE* ID ('=' expr)? ';';
//      type NEWLINE*  ID ( COMMA ID | NEWLINE)* ';' ;

type :
      'int' | 'boolean';

statement  :
      ifst | assign | compoundst | whilest;

compoundst  :
      'begin' NEWLINE* (statement NEWLINE*)* 'end' ;
//      'begin' NEWLINE* (statement NEWLINE+)+ 'end' ;

whilest :
    'while' '(' cond ')' '{' NEWLINE* (statement NEWLINE*)* '}';

ifst  :
      'if' '(' cond ')' NEWLINE* '{' NEWLINE* (statement NEWLINE*)* '}'
       ('else' NEWLINE* '{' NEWLINE* (statement NEWLINE*)* '}' )? ;

cond  :
      expr RELOP expr
      | BOOLEAN
      | '(' cond ')'
      | cond LOGICOP cond
      | '!' cond;

assign :
      ID '=' expr ';' ;

expr :
     expr '+' term        #expr_term_plus
    | expr '-' term      #expr_term_minus
    | expr RELOP term    #expr_term_relop
    | term               #term4
    ;

term :
    term '*' factor      #term_fact_mutiply
    | term '/' factor    #term_fact_divide
    | factor             #factor3
    ;

factor :
    '(' expr ')'      #fact_expr
    | ID              #fact_id
    | number          #fact_number
    | BOOLEAN         #fact_boolean
    ;

number :
    INT             #number_int;


/* Lexical Rules */
INT     : ('-')?DIGIT+ ;

BOOLEAN: 'true'|'false';

ID:
    LETTER(LETTER|DIGIT)* ;


fragment
        DIGIT: [0-9] ;
fragment
        LETTER: [a-zA-Z] ;
fragment
        ESC: '\\"' | '\\\\' ;
//In ANTLR, fragment is a keyword used to define lexer rules that contribute to the creation of other lexer rules but cannot be matched directly themselves. Fragments are reusable lexer rules that can be referenced within other lexer rules.
//
//When a rule is marked as a fragment, it means that this rule is a part of other rules but won't create tokens by themselves. They are helpful for organizing and reusing common patterns in lexer rules without generating tokens independently.
//
//For instance, in the provided grammar, you can see the fragment keyword being used in rules like DIGIT, LETTER, and ESC. These rules define patterns for digits, letters, and escape sequences within strings, but they won't generate tokens directly. Instead, they are used within other lexer rules to match and construct tokens.
//
//These fragments are utilized within other lexer rules like INT, ID, and String to define the patterns for integers, identifiers, and strings respectively.

WS: [ \t\r]+ -> skip ;
NEWLINE: '\n' | '\r\n';
RELOP: '>' | '<' | '==' | '!=' | '<=' | '>=';
LOGICOP : '||' | '&&' ;
ArithOp : '+' | '-' | '*' | '/' ;

//COMMENT
//    :   '/*' .*? '*/' -> channel(HIDDEN)
//    ;

LINE_COMMENT
    :   '#' ~[\r\n]* -> channel(HIDDEN); // channel(HIDDEN) means that the token will not be visible to the parser.
    // # '~' in RegEX means that the token will start with # and will end with any character
    // except \r and \n. [\r\n]* means that the token will contain any number of characters except \r and \n.