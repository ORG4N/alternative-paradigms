grammar Lisp;

expr: '(' op expr+ ')'  # Arithmetic
    | INT               # Int
    | '(' expr ')'      # Parens
    ;

op: ADD | SUB | MUL | DIV;

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';

INT: ('+' | '-')? [0-9]+;
WS: [ \t\r\n]+ -> skip;