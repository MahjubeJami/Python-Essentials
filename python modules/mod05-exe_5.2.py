"""
2. In mathematics, the factorial of a number n is defined
as n! = 1 ⋅ 2 ⋅ ... ⋅ n (as the product of all integer numbers
from 1 to n). For example, 4! = 1 ⋅ 2 ⋅ 3 ⋅ 4 = 24. Write a
recursive function for calculating n!

"""
n = int(input("Enter a number to calculate n!: "))
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
print( n,'! =', factorial(n))

