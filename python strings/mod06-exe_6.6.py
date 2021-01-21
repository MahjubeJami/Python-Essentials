"""
6. Write a program that takes your full name
as input and displays the abbreviations of
the middle name except the first and last name
which is displayed as it is. For example, if
your name is Elvis Aaron Presley, then the
output should be Elvis A. Presley.
"""

fullname = input("What is your full name ? ").title()
list = fullname.split()
middlename= list[1]
print(list[0], middlename[0]+'.', list[-1])
