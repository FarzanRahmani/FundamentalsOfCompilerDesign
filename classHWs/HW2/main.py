import antlr4
from Gen.TypeCheckerLexer import TypeCheckerLexer
from Gen.TypeCheckerParser import TypeCheckerParser
from Code.MyTypeCheckerListener import MyTypeCheckerListener # MyTypeCheckerListener is a subclass of TypeCheckerListener
# from Gen.TypeCheckerListener import TypeCheckerListener

from io import StringIO

def main():
    # listener = TypeCheckerListener()
    listener = MyTypeCheckerListener()

    expression = input("Enter an expression: ")
    # expression = "2 + 3"
    input_stream = antlr4.InputStream(expression) # not FileStream get the path to the file
    lexer = TypeCheckerLexer(input_stream)
    stream = antlr4.CommonTokenStream(lexer)
    parser = TypeCheckerParser(stream)
    tree = parser.expr() # parser.start()

    walker = antlr4.ParseTreeWalker()

    # walker.walk(listener, tree)
    try:
        walker.walk(listener, tree)
        type = listener.get_type()
        # type = listener.type
        print(type)
    except Exception as e:
        print(e)



    # if type is not None:
    #     print(type)
    # else:
    #     print("Type error")

if __name__ == "__main__":
    main()
