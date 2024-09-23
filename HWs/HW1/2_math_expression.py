import re

def test_math_expr(expr):
    # pattern = r'^[0-9]+(\.[0-9]+)?([+\-*/][0-9]+(\.[0-9]+)?)+$' # without () and do not accept space
    # pattern = r'^[0-9+\-*/.()]+$' # do not accept space
    pattern = r'^[0-9+\-*/.() ]+$' # accept space
    # ^ asserts the start of a line.
    # [0-9+\-*/.()] matches any character that is a digit, '+', '-', '*', '/', '.', '(', or ')'.
    # + is a quantifier that matches the preceding element one or more times.
    # $ asserts the end of a line.
    if re.match(pattern, expr):
        return True
    return False

# Valid expression
print("Test 1: (3 + 2) * 5")
print(test_math_expr("(3 + 2) * 5"))  # Expected output: True
print()

print("Test 2: 2+3*5")
print(test_math_expr("2+3*5"))  # Expected output: True
print()

print("Test 3: 10+5*(2-3)")
print(test_math_expr("10+5*(2-3)"))  # Expected output: True
print()

print("Test 4: 12.5/2")
print(test_math_expr("12.5/2"))  # Expected output: True
print()

# Invalid expression
print("Test 5: (3 + a) * 5")
print(test_math_expr("(3 + a) * 5"))  # Expected output: False
print()

print("Test 6: hello")
print(test_math_expr("hello"))  # Expected output: False
print()

print("Test 7: 25+89*87$12")
print(test_math_expr("25+89*87$12"))  # Expected output: True
print()
