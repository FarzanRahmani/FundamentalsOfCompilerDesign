class ILMapper:
    def __init__(self):
        self.stack = []
        self.il_codes = []
        self.global_variables = []
        self.label_counter = 0
        self.case_numbers = 0

    binary_operators = ['>=', '>', '==', '!=', '<', '<=', '&&', '||', '+', '-', '*', '/', '=', '&&', '||', '>>', '<<', ]
    flow_control_operators = ['if', 'for', 'while', 'block', 'switch']
    scope_operators = ['begin', 'end']
    ternary_operators = ['?']
    operators = binary_operators + flow_control_operators + ternary_operators + scope_operators

    # ///////HELPERS__START/////// define your helper functions below
    def create_new_label(self):
        self.label_counter += 1
        return 'Label' + str(self.label_counter)

    def add_global_variable(self, item):
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
        return item == "__Temporary"

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
            if item == 'case':
                self.case_numbers = self.case_numbers + 1
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
        if item in self.scope_operators:
            return item
        if item in self.flow_control_operators:
            return self.flow_control(item)



    # ///////CORE__FUNCTIONS__END/////// define your core functions above

    # ///////GENERATOR__FUNCTIONS__START/////// define your generator functions below

    def binary_operator(self, a, b, item):
        if item == "=":
            return self.assignment(a, b)
        first_load_statement = ''
        second_load_statement = ''



        # Operator selection logic
        operator = (
            'add' if item == '+' else
            'sub' if item == '-' else
            'div' if item == '/' else
            'mul' if item == '*' else
            'and' if item == '&&' else
            'or' if item == '||' else
            'ceq' if item == '==' else
            'cgt' if item == '>' else
            'clt' if item == '<' else
            'bge' if item == '>=' else
            'ble' if item == '<=' else
            'dif' if item == '!=' else
            'bne.un'
        )
        temp_operators = ['bge' , 'ble' , 'dif']
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
        if operator not in temp_operators:
            self.push_temporary_to_stack()
            return first_load_statement + second_load_statement + f"{operator}\n"
        else:
            self.push_temporary_to_stack()
            return self.comparison_operator(first_load_statement,second_load_statement,operator)

    def comparison_operator(self, first_load_statement,second_load_statement,operator):
        result = ''
        if operator == 'bge':
            temp_operator = 'clt'
            temp_operator2 = 'ceq'
            result = result + first_load_statement + second_load_statement + f"{temp_operator}\n"
            result = result + "ldc.i8 0\n" + f"{temp_operator2}\n"
        elif operator == 'ble' :
            temp_operator = 'cgt'
            temp_operator2 = 'ceq'
            result = result + first_load_statement + second_load_statement + f"{temp_operator}\n"
            result = result + "ldc.i8 0\n" + f"{temp_operator2}\n"
        elif operator == 'dif' :
            temp_operator = 'ceq'
            temp_operator2 = 'ceq'
            result = result + first_load_statement + second_load_statement + f"{temp_operator}\n"
            result = result + "ldc.i8 0\n" + f"{temp_operator2}\n"
        return result


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

        iteratorDec = temp_for_statement.pop()

        loop_var = ''
        for index in iteratorDec.split('\n'):
            if 'stloc' in index:
                loop_var = index[6:]

        if "stloc" in str(iteratorDec):
            result = result + iteratorDec
        else:
            result = result + iteratorDec
            result = result + temp_for_statement.pop()

        result = result + f"{for_body_start}:\n"
        exprValue = self.stack.pop()

        if self.is_temporary_operand(exprValue):
            result = result + temp_for_statement.pop()
        else:
            if self.is_identifier(exprValue):
                result = result + f"ldloc {exprValue}\n"
            else:
                result = result + f"ldc.i8 {exprValue}\n"

        # result = result + "ldloc i\n"
        result = result + f'ldloc {loop_var}\n'
        result = result + f"cgt\nbrfalse {for_body_end}\n"

        while len(temp_for_statement) != 0:
            result = result + temp_for_statement.pop()

        # result = result + f"ldc.i8 1\nldloc i\nadd\nstloc i\n"
        result = result + f'ldc.i8 1\nldloc {loop_var}\nadd\nstloc {loop_var}\n'
        result = result + f"br {for_body_start}\n"
        result = result + f"{for_body_end}:\n"
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

        result = result + f'{while_body_start}:\n'
        result = result + temp_while_statement.pop() + f'brfalse {while_body_end}\n'

        while len(temp_while_statement) != 0:
            result = result + temp_while_statement.pop()

        result = result + f'br {while_body_start}\n'
        result = result + f'{while_body_end}:\n'
        return result

    def switch_statement(self):
        temp_switch_statement = []
        for i in range(self.case_numbers):
            current_code = self.il_codes.pop()
            temp_switch_statement.append(current_code)
        self.stack.reverse()
        switch_variable = self.stack.pop()
        stack_array = []
        label_array = []
        label_array2 = []
        for i in self.stack:
            if i != 'case':
                stack_array.append(i)
        for j in range(len(stack_array)):
            label_array.append(self.create_new_label())
        result = ''
        label_array.reverse()
        for p in range(len(stack_array)):
            label = label_array.pop()
            result = result + f'ldc.i8 {stack_array.pop()}\n' + f'ldloc {switch_variable}\n' + 'ceq \n' + f'brtrue {label}\n'
            label_array2.append(label)

        last_label = f'Label{1 + self.case_numbers}'
        label_array2.reverse()
        for i in range (self.case_numbers):
            result = result + f'{label_array2.pop()}:\n' + temp_switch_statement.pop() + f'br {last_label}\n'
        result = result + f'{last_label}:\n'
        return result



