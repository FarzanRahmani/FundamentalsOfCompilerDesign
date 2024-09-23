grammar Arithmetic;

// Parser Rules
start returns[value=float()]: expr EOF;
expr returns[value=float()]: term ((ADD | SUB) term)*; // priority 3
term returns[value=float()]: factor ((MUL | DIV) factor)*; // priority 2
factor returns[value=float()]: NUMBER | LPAREN expr RPAREN; // priority 1

// Lexical Rules
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
LPAREN: '(';
RPAREN: ')';
NUMBER: [0-9]+ | [0-9]+('.'[0-9]+); // int or float
WS: [ \t\r\n]+ -> skip; // shite space

//## previous version without attributed grammers
//
//grammar Arithmetic;
//
//start: expr EOF;
//expr: term ((ADD | SUB) term)*;
//term: factor ((MUL | DIV) factor)*;
//factor: NUMBER | LPAREN expr RPAREN;
//
//ADD: '+';
//SUB: '-';
//MUL: '*';
//DIV: '/';
//LPAREN: '(';
//RPAREN: ')';
//NUMBER: [0-9]+ | [0-9]+('.'[0-9]+);
//WS: [ \t\r\n]+ -> skip;