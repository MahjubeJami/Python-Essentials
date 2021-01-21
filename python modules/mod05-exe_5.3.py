"""
3. Write a recursive Python function that returns the sum
of the first n integers. (Hint: The function will be similar
to the factorial function!) ie sum_nint(3) = 1 + 2 + 3 = 6 ,
sum_nint(4) = 1 + 2 + 3 + 4 = 10.
"""

n = int(input("Enter a number to calculate n!: "))
def sum_nint(n):
    if n <= 1:
        return 1
    return n + sum_nint(n - 1)
print("sum_nint(",n,") is",sum_nint(n))
