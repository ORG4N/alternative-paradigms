grammar Lisp;

expr: expr op=('*' | '/') expr   # MulDiv
    | expr op=('+' | '-') expr   # AddSub
    | INT                        # int
    | '(' expr ')'               # parens
    ;

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';

INT: [0-9]+;
WS: [ \t\r\n]+ -> skip;