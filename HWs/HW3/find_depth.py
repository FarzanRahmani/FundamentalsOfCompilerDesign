from antlr4 import *
from Gen.chaloosOotaghParser import chaloosOotaghParser
from Gen.chaloosOotaghLexer import chaloosOotaghLexer
from Code.MyListener import MyListener


def main(filePath):
    # Step 1: Load input source into stream
    stream = FileStream(filePath)

    # Step 2: Create an instance of AssignmentStLexer
    lexer = chaloosOotaghLexer(stream)

    # Step 3: Convert the input source into a list of tokens
    token_stream = CommonTokenStream(lexer)

    # Step 4: Create an instance of the AssignmentStParser
    parser = chaloosOotaghParser(token_stream)

    # Step 5: Create parse tree
    parse_tree = parser.start()

    # Step 6: Create an instance of AssignmentStListener
    ast_generator = MyListener()

    # Step 7: Walk parse tree with a customized listener (Automatically)
    walker = ParseTreeWalker()
    walker.walk(t=parse_tree, listener=ast_generator)
    print("\n Finished")


if __name__ == '__main__':
    path = input("please enter the file path : ")
    main(path)
