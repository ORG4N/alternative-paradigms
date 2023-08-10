from cmath import exp
from antlr4 import *    
from files import *                                          # Importing Lexer, Parser, Listener, Visitor, EvalListener, EvalVisitor


# parse expression and create parse tree
def interpreter(expression):
    lexer  = LispLexer(expression)                       # tokenize
    stream = CommonTokenStream(lexer) 
    parser = LispParser(stream)                          # parse
    tree   = parser.expr()  
    return tree


# evaluate and print the result using a Visitor
def evaluate(tree):
        
    #print( "\nEvaluate using Visitor")
    result = EvalVisitor().visit(tree)
    return result


# print the parse tree
def print_tree(tree, parser):

    print("\nPrinting the parse tree") 
    print(tree.toStringTree(recog=parser))  


# main method
def main(*args):

    # If no args are given then request user input for expression.
    if not args:
        expression = InputStream(input("\n>>>"))

    # If exactly one arg is given then use that as the expression.
    elif len(args) == 1:
        expression = InputStream(args[0])

    # If more than one arg is given.
    else:
        print("Too many arguments")
        return

    tree = interpreter(expression)      
    result = evaluate(tree)

    print(expression, " = ", result)

    return result

# In command line run: python src/main.py
if __name__ == '__main__':
   main()
