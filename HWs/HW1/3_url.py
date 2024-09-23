import re

def test_url(url):
    # pattern = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
    # pattern = r'^https?:\/\/(www\.)?([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$'
    # pattern = r'^https?://(www\.)?([a-zA-Z0-9-]+)(\.\w+)+(/\w+)*/?$'
    pattern = r'^(http|https):\/\/[a-zA-Z0-9-\.]+\.[a-zA-Z]{2,}(\/.*)?$'
    # ^ asserts the start of a line.
    # (http|https) matches either 'http' or 'https'.
    # :\/\/ matches '://' literally.
    # [a-zA-Z0-9-\.]+ matches one or more characters that are letters (either uppercase or lowercase), digits, '-', or '.'.
    # \. matches the literal character '.'.
    # [a-zA-Z]{2,} matches two or more characters that are letters (either uppercase or lowercase).
    # (\/.*)? is an optional group that matches '/' followed by zero or more of any character.
    # $ asserts the end of a line.
    if re.match(pattern, url):
        return True
    return False

# Valid URL
print("Test 1: https://www.example.com")
print(test_url("https://www.example.com"))  # Expected output: True
print()

print("Test 2: https://www.test-site.co.in")
print(test_url("https://www.test-site.co.in"))  # Expected output: True
print()

print("Test 3: https://google.com")
print(test_url("https://google.com"))  # Expected output: True
print()

# Invalid URL
print("Test 2: htp:/example.com")
print(test_url("htp:/example.com"))  # Expected output: False
print()

print("Test 2: invalid-url")
print(test_url("invalid-url"))  # Expected output: False
print()
