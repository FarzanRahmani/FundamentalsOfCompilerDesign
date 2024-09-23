from gen.JavaParser import *

class VariableTypeAndLineListener(ParseTreeListener):

    def enterVariableDeclarator(self, ctx:JavaParser.VariableDeclaratorContext):
            # get the name of the variable
            variable_name = ctx.variableDeclaratorId().Identifier().getText()

            # get the type of the variable
            variable_type = ctx.parentCtx.parentCtx.children[0].getText()

            # get the line number
            line_number = ctx.start.line

            # check if the variable is an array
            variable_declarator_id = ctx.variableDeclaratorId()

            if variable_declarator_id.dims(): # variable is an array
                # get the dimensions of the array
                dims_text = variable_declarator_id.dims().getText()

                # print the variable type, name and dimensions
                print(f'line {line_number}: {variable_type}{dims_text} - name: {variable_name}')
            else: # variable is not an array
                # print the variable type and name
                print(f'line {line_number}: {variable_type} - name: {variable_name}')