import re

# 1. Email format
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# 2. Mathematical expression (including operations of multiplication, division, addition, and subtraction)
math_expression_pattern = r'^[0-9+\-*/.()]+$'

# 3. URL
url_pattern = r'^(http|https):\/\/[a-zA-Z0-9-\.]+\.[a-zA-Z]{2,}(\/.*)?$'

# 4. Zip Code (US zip code pattern)
zip_code_pattern = r'^\d{5}(?:[-\s]\d{4})?$'

# 5. Phone number (US phone number pattern)
phone_number_pattern = r'^\+?1?\s*?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$'

# Test the patterns
test_cases = {
    "Emails": ["test.email@gmail.com", "invalid.email@com", "another_email@domain.co.in"],
    "Math Expressions": ["2+3*5", "9-6/3", "10+5*(2-3)", "12.5/2"],
    "URLs": ["http://www.example.com", "https://www.test-site.co.in", "invalid-url"],
    "Zip Codes": ["12345", "12345-6789", "123456", "ABCDE"],
    "Phone Numbers": ["123-456-7890", "123 456 7890", "+1 (123) 456-7890", "123-abc-7890"]
}

patterns = {
    "Emails": email_pattern,
    "Math Expressions": math_expression_pattern,
    "URLs": url_pattern,
    "Zip Codes": zip_code_pattern,
    "Phone Numbers": phone_number_pattern
}

for key, value in test_cases.items():
    print(f"Testing {key}:")
    pattern = patterns[key]
    for test_string in value:
        match = re.match(pattern, test_string)
        if match:
            print(f"{test_string} matches the pattern.")
        else:
            print(f"{test_string} does not match the pattern.")
    print("-----------------------")
