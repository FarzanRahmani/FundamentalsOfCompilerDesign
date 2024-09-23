import re

email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'

def validate_email(email):
  match = re.match(email_regex, email)
  if match is None:
    return False
  else:
    return True

# Example usage:

email_address = 'john.doe@example.com'

if validate_email(email_address):
  print('The email address is valid.')
else:
  print('The email address is invalid.')

################################
import re

math_expr_regex = r'^[+-\/*\d()]+$'

def validate_math_expr(expr):
  match = re.match(math_expr_regex, expr)
  if match is None:
    return False
  else:
    return True

# Example usage:

math_expr = '(2 + 3) * 4'

if validate_math_expr(math_expr):
  print('The mathematical expression is valid.')
else:
  print('The mathematical expression is invalid.')

################################
import re

url_regex = r'^https?:\/\/(www\.)?([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$'

def validate_url(url):
  match = re.match(url_regex, url)
  if match is None:
    return False
  else:
    return True

# Example usage:

url = 'https://www.google.com'

if validate_url(url):
  print('The URL is valid.')
else:
  print('The URL is invalid.')

################################
import re

zip_code_regex = r'^\d{5}(-\d{4})?$'

def validate_zip_code(zip_code):
  match = re.match(zip_code_regex, zip_code)
  if match is None:
    return False
  else:
    return True

# Example usage:

zip_code = '94085'

if validate_zip_code(zip_code):
  print('The zip code is valid.')
else:
  print('The zip code is invalid.')

################################
import re

phone_number_regex = r'^\(?\d{3}\)?[-]?(\d{3})[-]?(\d{4})$'

def validate_phone_number(phone_number):
  match = re.match(phone_number_regex, phone_number)
  if match is None:
    return False
  else:
    return True

# Example usage:

phone_number = '(123) 456-7890'

if validate_phone_number(phone_number):
  print('The phone number is valid.')
else:
  print('The phone number is invalid.')
