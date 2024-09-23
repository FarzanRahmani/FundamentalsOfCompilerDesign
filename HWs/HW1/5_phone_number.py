import re 

def test_phone(phone):
    # pattern = r"^(?:\+?1\s?)?((?:[0-9]{3})|(?:\([0-9]{3}\)))[-\s]?(\d{3})[-\s]?(\d{4})$" # US phone number only
    # pattern = r"^(?:\+?(98|0)\s?)?((?:[0-9]{3})|(?:\([0-9]{3}\)))[-\s]?(\d{3})[-\s]?(\d{4})$" # Iran phone number only
    pattern = r"^\+?\d{1,3}\s?((?:[0-9]{3})|(?:\([0-9]{3}\)))[-\s]?(\d{3})[-\s]?(\d{4})$" # all countries
    # •	^ : Start of the line.
    # •	^\+?\d{1,3}\s? : Country Code that includes an optional plus sign (+?), followed by an optional space (\s?). The rest of the pattern matches a phone number in various formats, such as “1234567890”, “123 456 7890”, “(123)4567890”, “(123) 456 7890”, etc.
    if re.match(pattern, phone):
        return True
    return False

# Valid phone number
print("Test 1: +1 (123) 456-7890")
print(test_phone("+1 (123) 456-7890"))  # Expected output: True
print()

print("Test 2: +98 919 456 7890")
print(test_phone("+98 919 456 7890"))  # Expected output: True
print()

print("Test 3: +989128357533")
print(test_phone("+989128357533"))  # Expected output: True
print()

print("Test 4: 1 (690) 069-8585")
print(test_phone("1 (690) 069-8585"))  # Expected output: True
print()

# Invalid phone number
print("Test 5: 123-45-67890")
print(test_phone("123-45-67890"))  # Expected output: False
print()

print("Test 6: +98 9125 7756 1245")
print(test_phone("+98 9125 7756 1245"))  # Expected output: False
print()

print("Test 7: 2222222222")
print(test_phone("2222222222"))  # Expected output: False
print()
