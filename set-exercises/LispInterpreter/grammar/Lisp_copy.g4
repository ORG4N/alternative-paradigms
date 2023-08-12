grammar Lisp;

expr: expr op=('*' | '/') expr          # MulDiv
    | expr op=('+' | '-') expr          # AddSub
    | INT                               # Int
    | ID                                # ID
    | '(' expr ')'                      # Parens
    | FUNC '(' expr ')'                 # FuncCall
    | LET '(' ID '=' expr ')' expr      # Let
    ;


ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';

FUNC: 'sin' | 'cos' | 'square' | 'sqrt' | 'car' | 'cdr' | 'quote' | 'atom' | 'cond' | 'eq';
LET: 'let';
ID: [a-zA-Z]+;
INT: ('+' | '-')? [0-9]+;
WS: [ \t\r\n]+ -> skip;