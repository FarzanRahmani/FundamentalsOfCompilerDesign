from antlr4 import *
from grammars.JavaLexer import JavaLexer

input_address = input('Enter the java file address : ')
file_stream = FileStream(input_address) # mmd.java

lexer = JavaLexer(file_stream)
token = lexer.nextToken()
refactoredSTR = ''

# # TA code 
# # goal: // comment -> /* comment */
# while token.type != Token.EOF:
#     if(token.type == lexer.LINE_COMMENT): # LINE_COMMENT: '//' ~[\r\n]*
#         refactoredSTR += '/*' + token.text[2:] + ' */'
#     else:
#         refactoredSTR += token.text
#     token=lexer.nextToken()

# # question 1: /* comment */ -> // comment
# while token.type != Token.EOF:
#     if token.type == lexer.COMMENT: # COMMENT: '/*' .*? '*/'
#         # refactoredSTR+='//'+token.text[2:-2]+'\n'
#         removed_comment_text = token.text[2:-2]
#         comments = removed_comment_text.split('\n')
#         for i in range(0, len(comments), 1):
#             comment = comments[i]
#             if i != (len(comments) - 1):
#                 refactoredSTR += '//' + comment + '\n'
#             else:
#                 refactoredSTR += '//' + comment
#     else:
#         refactoredSTR += token.text
#     token = lexer.nextToken()

# question 2: /* comment */ -> /* 99521271 comment */, // comment -> // 99521271 comment, 99521271 is the student ID
student_ID = '99521271'
while token.type != Token.EOF:
    if token.type == lexer.COMMENT: # COMMENT: '/*' .*? '*/'
        refactoredSTR += f'/* [{student_ID}] ' + token.text[2:]
    elif token.type == lexer.LINE_COMMENT: # LINE_COMMENT: '//' ~[\r\n]*
        refactoredSTR += f'// [{student_ID}] ' + token.text[2:]
    else:
        refactoredSTR += token.text
    token = lexer.nextToken()

print(refactoredSTR+'\n')