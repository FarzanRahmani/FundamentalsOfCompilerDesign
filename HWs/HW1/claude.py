import re

# Email 
email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
email = 'test@example.com'
print(re.match(email_pattern, email))

# Mathematical expression
math_pattern = r'^[0-9()+\-*/]+$'  
math_expr = '(2+3)*5/2-4'
print(re.match(math_pattern, math_expr))

# URL
url_pattern = r'^https?://(www\.)?(\w+)(\.\w+)+(/\w+)*/?$'
url = 'http://www.example.com/path/to/page'
print(re.match(url_pattern, url))

# Zip code
zip_pattern = r'^\d{5}(?:[-\s]\d{4})?$'
zip_code = '12345'
print(re.match(zip_pattern, zip_code)) 

# Phone number
phone_pattern = r'^\+?(\d{1,3})?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?$'
phone = '(123) 456-7890'
print(re.match(phone_pattern, phone))