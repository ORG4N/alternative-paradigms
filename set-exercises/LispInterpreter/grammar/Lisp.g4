grammar Lisp;

expr: expr op=('*' | '/') expr   # MulDiv
    | expr op=('+' | '-') expr   # AddSub
    | INT                        # int
    | '(' expr ')'               # parens
    | FUNC '(' expr ')'          # funcCall
    ;

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';

FUNC: 'sin' | 'cos' | 'square' | 'sqrt';

INT: [0-9]+;
WS: [ \t\r\n]+ -> skip;