grammar Lisp;

expr: '(' op expr+ ')'  // Function call
    | INT              // Integer literal
    ;

op: '+' | '-' | '*' | '/';

INT: [0-9]+;
WS: [ \t\r\n]+ -> skip;