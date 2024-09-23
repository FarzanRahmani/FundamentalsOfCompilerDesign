import re

def test_zip(zip_code):
    pattern = r"^\d{5}(?:[-\s]\d{4})?$" # assuming US format
    # •	^ : Start of the line.
    # •	\d{5} : Exactly five digits.
    # •	(?:[-\s]\d{4})? : An optional group (?) that includes a hyphen (-) or space (\s) followed by exactly four digits (\d{4}).
    # •	$ : End of the line.
    if re.match(pattern, zip_code):
        return True
    return False

print("US format zip code: \n")

# Valid zip code
print("Test 1: 12345")
print(test_zip("12345"))  # Expected output: True
print()

print("Test 2: 12345 6789")
print(test_zip("12345 6789"))  # Expected output: True
print()

print("Test 3: 12345-6789")
print(test_zip("12345-6789"))  # Expected output: True
print()

# Invalid zip code
print("Test 4: 1234")
print(test_zip("1234"))  # Expected output: False
print()

print("Test 4: abc def")
print(test_zip("abc def"))  # Expected output: False
print()


print("########################################################")
###################################################################


def test_iranian_zip(zip_code):
    pattern = r"^\d{5}[-\s]?\d{5}$" # assuming Iran format
    # •	^ : Start of the line.
    # •	\d{5} : Exactly five digits, representing the departure code.
    # •	[-\s]? : An optional group (?) that includes a hyphen (-) or space (\s).
    # •	\d{5} : Exactly five digits, representing the distribution code.
    # •	$ : End of the line.
    if re.match(pattern, zip_code):
        return True
    return False

print("Iran format zip code: \n")

# Valid zip codes
print("Test 1: 1616856761")
print(test_iranian_zip("1616856761"))  # Expected output: True
print()

print("Test 2: 16168 56761")
print(test_iranian_zip("16168 56761"))  # Expected output: True
print()

print("Test 3: 16168-56761")
print(test_iranian_zip("16168-56761"))  # Expected output: True
print()

# Invalid zip code
print("Test 4: 12345678")
print(test_iranian_zip("12345678"))  # Expected output: False
print()

print("Test 5: a1234b789")
print(test_iranian_zip("a1234b789"))  # Expected output: False
print()

print("Test 6: 98765--43210")
print(test_iranian_zip("98765--43210"))  # Expected output: False
print()
