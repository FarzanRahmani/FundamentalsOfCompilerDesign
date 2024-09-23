from antlr4 import  *
from Gen.chaloosOotaghLexer import chaloosOotaghLexer

file_path = input("Enter your file path: ")
student_num = input('Enter your student number: ')
student_name = input('Enter your name: ')
print("------------------------------------")
input_stream = FileStream(file_path)
lexer = chaloosOotaghLexer(input_stream)
token = lexer.nextToken()
refactored_str = ''

while token.type != Token.EOF:
    if token.type == lexer.LINE_COMMENT:
        refactored_str += '#' + student_name + ' ' + token.text[1:] + ' ' + student_num
    else:
        refactored_str += token.text
    token = lexer.nextToken()

print(refactored_str + '\n')
