"""
5. Write a Python script that takes input
 from the user and displays that input back
 in upper and lower cases.

Console Output:
    What is your first name ? alison
    What is your last name ? smith
    Hi Alison Smith , welcome to my python greet application!
"""

firstname = input("What is your first name ? ").capitalize()
lastname = input("What is your last name ? ").capitalize()

print("Hi" , firstname, lastname , ", welcome to my python greet application!")
