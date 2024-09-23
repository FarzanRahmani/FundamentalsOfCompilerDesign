class ILMapper:
    def __init__(self):
        self.stack = []
        self.il_codes = [] # result
        self.global_variables = []
        self.label_counter = 0

    binary_operators = ['>=', '>', '==', '!=', '<', '<=', '&&', '||', '+', '-', '*', '/', '=', '&&', '||', '>>', '<<', ]
    flow_control_operators = ['if', 'for', 'while', 'block'] # switch
    scope_operators = ['begin', 'end']
    ternary_operators = ['?']
    operators = binary_operators + flow_control_operators + ternary_operators + scope_operators

    # ///////HELPERS__START/////// define your helper functions below
    def create_new_label(self):
        self.label_counter += 1
        return 'Label' + str(self.label_counter)

    def add_global_variable(self,item):
        if item in self.global_variables:
            return
        else:
            self.global_variables.append(item)

    def is_operator(self, item):
        if item in self.operators:
            return True
        else:
            return False

    def is_identifier(self, item):
        if not self.is_operator(item) and item[0].isalpha():
            return True
        else:
            return False

    def push_temporary_to_stack(self):
        self.stack.append("__Temporary")

    def is_temporary_operand(self, item):
        return item == "__Temporary" # for informing we have a number in IL Runtime Stack, we push a __Temporary to IL mappaer stack

    def get_msil_header(self):
        result = (".assembly extern mscorlib {}\n"
                  ".assembly output {}\n"
                  ".module output.exe\n"
                  ".class private auto ansi beforefieldinit ConsoleApp1.Program extends [mscorlib]System.Object\n"
                  "{\n"
                  ".method private hidebysig static void  Main(string[] args) cil managed\n"
                  "{\n"
                  ".entrypoint\n"
                  ".maxstack  100\n")

        for i in range(len(self.global_variables)):
            result += f".locals init ([{i}] int64 {self.global_variables[i]})\n"
        if not 'output' in self.global_variables:
            result += f".locals init ([{len(self.global_variables)}] int64 output)\n"

        result += ("nop\n"
                   "///////////////////////// IL CODE\n")

        return result

    @staticmethod
    def get_msil_footer():
        return ("\n///////////////////////// IL CODE\n"
                "ldloca.s   output\n"
                "call       instance string [mscorlib]System.Int64::ToString()\n"
                "call       void [mscorlib]System.Console::WriteLine(string)\n"
                "nop\n"
                "ret\n"
                "} // end of method Program::Main\n"
                ".method public hidebysig specialname rtspecialname instance void  .ctor() cil managed\n"
                "{\n"
                ".maxstack  8\n"
                "ldarg.0\n"
                "call       instance void [mscorlib]System.Object::.ctor()\n"
                "nop\n"
                "ret\n"
                "} // end of method Program::.ctor\n"
                "} // end of class\n")

    # ///////HELPERS__END/////// define your helper functions above

    # ///////CORE__FUNCTIONS__START/////// define your core functions below

    def generate_intermediate_language(self, post_order_array):
        for item in post_order_array:
            if self.is_operator(item):
                self.il_codes.append(self.generate_il_based_on_operator(item))
            else:
                if self.is_identifier(item):
                    self.add_global_variable(item)
                self.stack.append(item)

        result = ''
        for string in self.il_codes:
            if string is not None:
                result += string

        with open("output.il", "w") as my_file:
            my_file.write(self.get_msil_header())
            my_file.write(result)
            my_file.write(self.get_msil_footer())
        return result

    def generate_il_based_on_operator(self, item):
        if item in self.binary_operators:
            second_operand = self.stack.pop()
            first_operand = self.stack.pop()
            return self.binary_operator(first_operand, second_operand, item)
        if item in self.ternary_operators:
            third_operand = self.stack.pop()
            second_operand = self.stack.pop()
            first_operand = self.stack.pop()
            return self.ternary(first_operand, second_operand, third_operand)
        if item in self.scope_operators: # begin, end
            return item
        if item in self.flow_control_operators:
            return self.flow_control(item)

        # if item == '<=':
        #     return self.binary_operator_with_comparison('cgt', '<=')
        # elif item == '>=':
        #     return self.binary_operator_with_comparison('clt', '>=')
        # elif item == '!=':
        #     return self.binary_operator_with_comparison('ceq', '!=')

    # ///////CORE__FUNCTIONS__END/////// define your core functions above

    # ///////GENERATOR__FUNCTIONS__START/////// define your generator functions below

    def binary_operator(self, a, b, item):
        if item == "=":
            return self.assignment(a, b)
        elif item == "!=":
            return self.not_equal(a, b)
        elif item == "<=":
            return self.less_than_or_equal(a, b)
        elif item == ">=":
            return self.greater_than_or_equal(a, b)
        
        first_load_statement = ''
        second_load_statement = ''
        operator = 'add' if item == '+' else 'sub' if item == '-'\
            else 'div' if item == '/' else 'mul' if item == '*' else\
            'and' if item == '&&' else 'or' if item == '||' else\
            'ceq' if item == '==' else 'cgt' if item == '>' else 'clt'

        if not self.is_temporary_operand(b):
            if self.is_identifier(b):
                second_load_statement = f"ldloc {b}\n"
            else:
                second_load_statement = f"ldc.i8 {b}\n"
        else:
            second_load_statement = self.il_codes.pop()

        if not self.is_temporary_operand(a):
            if self.is_identifier(a):
                first_load_statement = f"ldloc {a}\n"
            else:
                first_load_statement = f"ldc.i8 {a}\n"
        else:
            first_load_statement = self.il_codes.pop()

        self.push_temporary_to_stack()
        return first_load_statement + second_load_statement + f"{operator}\n"

    def assignment(self, first_operand, second_operand):
        if not self.is_identifier(first_operand):
            raise Exception
        if self.is_identifier(second_operand):
            load_statement = f"ldloc {second_operand}\n"
        elif self.is_temporary_operand(second_operand):
            load_statement = ''
        else:
            load_statement = f"ldc.i8 {second_operand}\n"
        return load_statement + f"stloc {first_operand}\n"

    def ternary(self, condition, a, b):
        if not self.is_temporary_operand(b):
            if self.is_identifier(b):
                second_load_statement = f"ldloc {b}\n"
            else:
                second_load_statement = f"ldc.i8 {b}\n"
        else:
            second_load_statement = self.il_codes.pop()

        if not self.is_temporary_operand(a):
            if self.is_identifier(a):
                first_load_statement = f"ldloc {a}\n"
            else:
                first_load_statement = f"ldc.i8 {a}\n"
        else:
            first_load_statement = self.il_codes.pop()

        if not self.is_temporary_operand(condition):
            if self.is_identifier(condition):
                condition_load_statement = f"ldloc {condition}\n"
            else:
                condition_load_statement = f"ldc.i8 {condition}\n"
        else:
            condition_load_statement = self.il_codes.pop()

        self.push_temporary_to_stack()
        true_start_label = self.create_new_label()
        false_start_label = self.create_new_label()
        false_end_label = self.create_new_label()

        return (condition_load_statement
                + f"brtrue {true_start_label}\n"
                + f"br {false_start_label}\n"
                + f"{true_start_label + ':'}\n"
                + first_load_statement
                + f"br {false_end_label} \n"
                + f"{false_start_label + ':'}\n"
                + second_load_statement
                + f"{false_end_label + ':'}\n")

    def not_equal(self, a, b):
        # load second operand to IL Runtime Stack
        if not self.is_temporary_operand(b):
            if self.is_identifier(b):
                second_load_statement = f"ldloc {b}\n"
            else:
                second_load_statement = f"ldc.i8 {b}\n"
        else:
            second_load_statement = self.il_codes.pop()

        # load first operand to IL Runtime Stack
        if not self.is_temporary_operand(a):
            if self.is_identifier(a):
                first_load_statement = f"ldloc {a}\n"
            else:
                first_load_statement = f"ldc.i8 {a}\n"
        else:
            first_load_statement = self.il_codes.pop()
        
        result = ''
        # Push 1 (of type int32) if a equals b, else push 0.
        result += first_load_statement
        result += second_load_statement
        result += f"ceq\n"
        # if equal with 0(not equal), push 1, else(equal) push 0
        result += "ldc.i8 0\nceq\n" 

        self.push_temporary_to_stack() # for informing we have a number in IL Runtime Stack, we push a __Temporary to IL mappaer stack
        return result
    
    def less_than_or_equal(self, a, b):
        # load second operand to IL Runtime Stack
        if not self.is_temporary_operand(b):
            if self.is_identifier(b):
                second_load_statement = f"ldloc {b}\n"
            else:
                second_load_statement = f"ldc.i8 {b}\n"
        else:
            second_load_statement = self.il_codes.pop()

        # load second operand to IL Runtime Stack
        if not self.is_temporary_operand(a):
            if self.is_identifier(a):
                first_load_statement = f"ldloc {a}\n"
            else:
                first_load_statement = f"ldc.i8 {a}\n"
        else:
            first_load_statement = self.il_codes.pop()
        
        result = ''
        # a <= b  ->  a - b <= 0  ->  a - b < 1  ->  a - b < 1  
        # result = first_load_statement + second_load_statement + f"sub\n"
        result += first_load_statement
        result += second_load_statement
        result += f"sub\n"
        result += "ldc.i8 1\nclt\n" # Push 1 (of type int32) if value1 lower than value2, else push 0.
        
        self.push_temporary_to_stack() # Push 1 (of type int32) if value1 lower than value2, else push 0.
        return result

    def greater_than_or_equal(self, a, b):
        # load second operand to IL Runtime Stack
        if not self.is_temporary_operand(b):
            if self.is_identifier(b):
                second_load_statement = f"ldloc {b}\n"
            else:
                second_load_statement = f"ldc.i8 {b}\n"
        else:
            second_load_statement = self.il_codes.pop()

        # load second operand to IL Runtime Stack
        if not self.is_temporary_operand(a):
            if self.is_identifier(a):
                first_load_statement = f"ldloc {a}\n"
            else:
                first_load_statement = f"ldc.i8 {a}\n"
        else:
            first_load_statement = self.il_codes.pop()

        result = ''
        # a >= b  ->  a - b >= 0  ->  a - b > -1  ->  a - b > -1
        result += first_load_statement
        result += second_load_statement
        result += f"sub\n"
        result += "ldc.i8 -1\ncgt\n" # 	Push 1 (of type int32) if value1 greater that value2, else push 0.
        
        self.push_temporary_to_stack() # for informing we have a number in IL Runtime Stack, we push a __Temporary to IL mappaer stack
        return result

    def flow_control(self, item):
        if item == 'block':
            return self.block()
        if item == 'if':
            return self.if_statement()
        if item == 'for':
            return self.for_statement()
        if item == 'while':
            return self.while_statement()
        if item == 'switch':
            return self.switch_statement()

    def block(self):
        temp_block_stack = []
        current_code = self.il_codes.pop()
        if current_code != 'end':
            return current_code
        while current_code != 'begin':
            current_code = self.il_codes.pop()
            temp_block_stack.append(current_code)
        temp_block_stack.pop()
        result = ''
        while len(temp_block_stack) != 0:
            result = result + temp_block_stack.pop()
        return result

    def if_statement(self):
        temp_if_stack = []
        current_code = self.il_codes.pop()
        if current_code != 'end':
            return current_code
        while current_code != 'begin':
            current_code = self.il_codes.pop()
            temp_if_stack.append(current_code)
        temp_if_stack.pop()
        result = ''
        if len(temp_if_stack) == 2:
            true_label_start = self.create_new_label()
            true_label_end = self.create_new_label()
            result = (temp_if_stack.pop()
                      + f"brtrue {true_label_start}\n"
                      + f"br {true_label_end}\n"
                      + f"{true_label_start}:\n"
                      + temp_if_stack.pop()
                      + f"{true_label_end}:\n")
        elif len(temp_if_stack) == 3:
            true_label_start = self.create_new_label()
            true_label_end = self.create_new_label()
            false_label_end = self.create_new_label()
            result = (temp_if_stack.pop()
                      + f"brtrue {true_label_start}\n"
                      + f"br {true_label_end}\n"
                      + f"{true_label_start}:\n"
                      + temp_if_stack.pop()
                      + f"br {false_label_end}\n"
                      + f"{true_label_end}:\n"
                      + temp_if_stack.pop()
                      + f"{false_label_end}:\n")
        return result

    def for_statement(self):
        temp_for_statement = []
        current_code = self.il_codes.pop()
        if current_code != 'end':
            return current_code
        while current_code != 'begin':
            current_code = self.il_codes.pop()
            temp_for_statement.append(current_code)
        temp_for_statement.pop()

        for_body_start = self.create_new_label()
        for_body_end = self.create_new_label()

        result = ''

        iteratorAssignment = temp_for_statement.pop()

        loop_var = ''
        for index in iteratorAssignment.split('\n'): # i := 1 
            if 'stloc' in index:
                loop_var = index[6:]

        result += iteratorAssignment

        result += f"{for_body_start}:\n"
        toValue = self.stack.pop() # for i := 1 to """10""" do 

        if self.is_temporary_operand(toValue):
            result += temp_for_statement.pop()
        else:
            if self.is_identifier(toValue):
                result += f"ldloc {toValue}\n"
            else:
                result += f"ldc.i8 {toValue}\n"

        result += f'ldloc {loop_var}\n' # loop_var -> i
        result += f"cgt\nbrfalse {for_body_end}\n"

        while len(temp_for_statement) != 0:
            result = result + temp_for_statement.pop()

        result += f'ldc.i8 1\nldloc {loop_var}\nadd\nstloc {loop_var}\n' # i -> i + 1
        result += f"br {for_body_start}\n"
        result += f"{for_body_end}:\n"

        return result

    def while_statement(self):
        temp_while_statement = []
        current_code = self.il_codes.pop()
        if current_code != 'end':
            return current_code
        while current_code != 'begin':
            current_code = self.il_codes.pop()
            temp_while_statement.append(current_code)
        temp_while_statement.pop()

        while_body_start = self.create_new_label()
        while_body_end = self.create_new_label()

        result = ''

        result += f'{while_body_start}:\n'
        result += temp_while_statement.pop() + f'brfalse {while_body_end}\n'

        while len(temp_while_statement) != 0:
            result += temp_while_statement.pop()

        result += f'br {while_body_start}\n'
        result += f'{while_body_end}:\n'

        return result

    # grammar of switch statement is az follows: 
    # switchst
    #     returns[value_attr = str(), type_attr = str()]:
    #     'switch' '(' ID ')' NEWLINE* '{' NEWLINE* case+ '}';
    def switch_statement(self):
        temp_switch_statement = []
        current_code = self.il_codes.pop()
        if current_code != 'end':
            return current_code
        while current_code != 'begin':
            current_code = self.il_codes.pop()
            temp_switch_statement.append(current_code)
        temp_switch_statement.pop()

        switch_body_start = self.create_new_label()
        switch_body_end = self.create_new_label()

        result = ''
        result += f'{switch_body_start}:\n'
        result += temp_switch_statement.pop() + f'brfalse {switch_body_end}\n'

        while len(temp_switch_statement) != 0:
            result += temp_switch_statement.pop()

        result += f'br {switch_body_start}\n'
        result += f'{switch_body_end}:\n'
        
        return result


    # ///////GENERATOR__FUNCTIONS__END/////// define your generator functions above
