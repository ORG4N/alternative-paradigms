grammar Lisp;

expr: '(' OP expr+ ')'                      # Arithmetic
    | INT                                   # Int
    | ID                                    # ID
    | '(' expr ')'                          # Parens
    | '('FUNC expr ')'                      # FuncCall
    | '(' LET '(' var+ ')' expr ')'         # Let
    ;

var: '(' ID expr ')';

OP: ADD | SUB | MUL | DIV;
FUNC: 'sin' | 'cos' | 'square' | 'sqrt' ;
LET: 'let';

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';

ID: [a-zA-Z]+;
INT: ('+' | '-')? [0-9]+;
WS: [ \t\r\n]+ -> skip;