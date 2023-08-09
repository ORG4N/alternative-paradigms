from antlr4 import *    
from files import *                                          # Importing Lexer, Parser, Listener, Visitor, EvalListener, EvalVisitor

def main():

    while True:

        text   = InputStream(input("\n>>>"))                   # get user input 

        lexer  = LispLexer(text)                             # tokenize
        stream = CommonTokenStream(lexer) 
        parser = LispParser(stream)                          # parse
        tree   = parser.expr()                       
        
        print("\nPrinting the parse tree")                   # print the parse tree 
        print(tree.toStringTree(recog=parser))               

        print( "\nEvaluate using Visitor")                   # evaluate and print the result using a Visitor
        print( "=", EvalVisitor().visit(tree) )

        #print( "\nEvaluate using Listener")                  # evaluate and print the result using a Listener
        #printer = EvalListener()           
        #walker  = ParseTreeWalker()
        #walker.walk(printer, tree)

if __name__ == '__main__':
    main()