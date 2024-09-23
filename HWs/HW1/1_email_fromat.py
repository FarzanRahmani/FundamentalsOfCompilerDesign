import re

def test_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    # •	^ : Start of the line.
    # •	[a-zA-Z0-9_.+-]+ : One or more (+) of the characters inside the square brackets ([]). These characters can be lowercase letters (a-z), uppercase letters (A-Z), numbers (0-9), underscore (_), dot (.), plus (+), or hyphen (-).
    # •	@ : Matches the @ symbol.
    # •	[a-zA-Z0-9-]+ : One or more (+) of the characters inside the square brackets ([]). These characters can be lowercase letters (a-z), uppercase letters (A-Z), numbers (0-9), or hyphen (-).
    # •	\. : Matches the dot symbol (.).
    # •	[a-zA-Z0-9-.]+ : One or more (+) of the characters inside the square brackets ([]). These characters can be lowercase letters (a-z), uppercase letters (A-Z), numbers (0-9), dot (.), or hyphen (-).
    # •	$ : End of the line.
    if re.match(pattern, email):
        return True
    return False

# Valid email
print("Test 1: example@example.com")
print(test_email("example@example.com"))  # Expected output: True
print()

print("Test 2: farzanrahmani70@gmail.com")
print(test_email("farzanrahmani70@gmail.com"))  # Expected output: True
print()

print("Test 3: farzan_rahmani@comp.iust.ac.ir")
print(test_email("farzan_rahmani@comp.iust.ac.ir"))  # Expected output: True
print()

# Invalid email
print("Test 4: example@.com")
print(test_email("example@.com"))  # Expected output: False
print()

print("Test 5: abc@x@google.com")
print(test_email("abc@x@google.com"))  # Expected output: False
print()

print("Test 6: xxx@iran")
print(test_email("xxx@iran"))  # Expected output: False
print()
