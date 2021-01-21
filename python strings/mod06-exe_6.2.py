"""
Take the following Python
code that stores a string: str = 'inet addr:127.0.0.1  Mask:255.0.0.0'.
Use find and string slicing to extract the portion of the string
after the colon inet address character and then use the
rstrip function to remove any trailing characters.
"""

str = 'inet addr:127.0.0.1  Mask:255.0.0.0'

at_por = str.find(':')
portion = str[at_por+1:]
print(portion.rstrip('  Mask:255.0.0.0'))
