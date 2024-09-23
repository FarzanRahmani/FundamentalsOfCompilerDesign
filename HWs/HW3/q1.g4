grammar Q1;

// Lexer rules
WS : [ \t\r\n]+ -> skip;
INT : 'int';
BOOLEAN : 'boolean';
IF : 'if';
WHILE : 'while';
TRUE : 'true';
FALSE : 'false';
ID : [a-zA-Z]+;
NUMBER : [0-9]+;
ASSIGN : '=';
SEMI : ';';
LPAREN : '(';
RPAREN : ')';
LBRACE : '{';
RBRACE : '}';
ADD : '+';
SUB : '-';
EQ : '==';
GT : '>';
LT : '<';
COMMENT : '#' ~[\r\n]* -> skip;

// Parser rules
program : statement+;

statement : variableDeclaration
          | assignment
          | ifStatement
          | whileStatement
          | COMMENT;

variableDeclaration : type ID (ASSIGN expression)? SEMI;

type : INT | BOOLEAN;

assignment : ID ASSIGN expression SEMI;

expression : NUMBER
           | TRUE
           | FALSE
           | ID
           | expression ADD expression
           | expression SUB expression
           | expression EQ expression
           | expression GT expression
           | expression LT expression
           | LPAREN expression RPAREN;

ifStatement : IF LPAREN expression RPAREN LBRACE statement RBRACE;

whileStatement : WHILE LPAREN expression RPAREN LBRACE statement RBRACE;