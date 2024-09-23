grammar TypeChecker;

// Parser Rules: starts with lower cases
start:
    expr EOF
    ;

expr returns [type=str()]:
    e2=expr '+' t1=term  #expr1 // label for grammar (#expr1)
    | expr '-' term  #expr2
    | term #expr3
    ;

term returns [type=str()]:
    term '*' fact  #term1
    | term '/' fact #term2
    | fact #term3
    ;

fact returns [type=str()]:
     STRING #factString
    |INTEGER #factInteger
    |FLOAT #factFloat
    |'('expr')' #factExpr;

/* Lexical rules: starts with capital cases */
Plus: '+';
MINUS: '-';
MUL: '*';
DIVIDE: '/';
ASSIGN: '=';

STRING:'"' .*? '"';
INTEGER: [0-9]+;
FLOAT:[0-9]*'.'[0-9]+; // .1, 0.1

Whitespace: [ \t]+ -> channel(HIDDEN);
Newline: '\n' -> skip;



