# implemet the followings with RegEx and test them
# 1. email format
# 2. mathematical expression including +, -, *, /, (, )
# 3. URL
# 4. zip code
# 5. phone number

import re

# 1. email format
email = input("Enter your email address: ")
pattern = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
if pattern.search(email):
    print("Valid email address")
else:
    print("Invalid email address")

# 2. mathematical expression including +, -, *, /, (, )
expression = input("Enter a mathematical expression: ")
# pattern = re.compile(r"^[0-9]+[+\-*/][0-9]+$") # not correct
pattern = re.compile(r"^[0-9]+[+\-*/][0-9]+([+\-*/][0-9]+)$") # not correct
if pattern.search(expression):
    print("Valid mathematical expression")
else:
    print("Invalid mathematical expression")

# 3. URL
url = input("Enter a URL: ")
pattern = re.compile(r"^https?://(www\.)?([a-zA-Z0-9-]+)(\.[a-zA-Z0-9-]+)+$")
if pattern.search(url):
    print("Valid URL")
else:
    print("Invalid URL")

# 4. zip code
zip_code = input("Enter a zip code: ")
pattern = re.compile(r"^[0-9]{5}(?:-[0-9]{5})?$")
if pattern.search(zip_code):
    print("Valid zip code")
else:
    print("Invalid zip code")

# 5. phone number
phone_number = input("Enter a phone number: ")
pattern = re.compile(r"^\d{3}-\d{3}-\d{4}$") # 912-835-7533
if pattern.search(phone_number):
    print("Valid phone number")
else:
    print("Invalid phone number")
