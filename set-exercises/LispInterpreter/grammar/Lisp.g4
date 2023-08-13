grammar Lisp;

expr: '(' OP expr+ ')'                      # Arithmetic
    | INT                                   # Int
    | ID                                    # ID
    | '(' expr* ')'                         # List
    | '(' FUNC expr ')'                     # FuncCall
    | '(' EQ_FUNC expr expr ')'             # FuncEq
    | '(' COND_FUNC cond_clause+ ')'        # FuncCond
    | '(' LET '(' var+ ')' expr ')'         # Let
    ;

var: '(' ID expr ')';
cond_clause: '(' expr expr ')';

OP: ADD | SUB | MUL | DIV;
FUNC: 'sin' | 'cos' | 'square' | 'sqrt' | 'car' | 'cdr' | 'quote' | 'atom' ;
EQ_FUNC: 'eq';
COND_FUNC: 'cond';
LET: 'let';

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';

ID: [a-zA-Z]+;
INT: ('+' | '-')? [0-9]+;
WS: [ \t\r\n]+ -> skip;