from antlr4 import *
from gen.JavaParser import JavaParser
from gen.JavaLexer import JavaLexer
from Code.VariableListener import VariableTypeAndLineListener


def main():
    # get the path to the java file
    path_to_file = input("Please enter the path to java file: ") # e.g. ./test.java

    # Create an input character stream from standard input
    input_stream = FileStream(path_to_file)

    # Create a lexer that feeds off the input expression
    lexer = JavaLexer(input_stream)

    # Create a stream of tokens using the lexer
    token_stream = CommonTokenStream(lexer)

    # Create a parser that feeds off the token stream
    parser = JavaParser(token_stream)

    # Obtain the parse tree by invoking the parser's entry point
    parse_tree = parser.compilationUnit() # start: compilationUnit EOF ;

    # Create a custom listener object
    my_listener = VariableTypeAndLineListener()

    # Walk the parse tree with the custom listener
    walker = ParseTreeWalker()

    try:
        # Walk the tree
        walker.walk(my_listener, parse_tree)
    except Exception as e:
        # Print the error
        print(e)


# Call the main function
if __name__ == '__main__':
    main()
