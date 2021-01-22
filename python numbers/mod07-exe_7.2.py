"""
2. The data type integer signed range is from
-2,1471483,648 to 2,1471483,648 (4 bytes).
Write a program that determines the range of numbers
for an integer based on the number of bytes it can encode
(Hint integral type with n bits can encode 2n numbers).
Console:
Enter number of Bytes you would like to determine the signed range of: 4
4 Byte(s) integral type with 8 bits can encode 4,294,967,296 numbers.
The signed range will be from -2,147,483,648 to 2,147,483,647
"""

import math
input = int(input("Enter number of Bytes you would like to determine the signed range of:"))
num = input * 8
num = pow(2,num)

print(input,"Byte(s) integral type with 8 bits can encode", "{:,}".format(num) ,
      "numbers. The signed range will be from -"+"{:,.0f}".format(num/2), "to",
      "{:,.0f}".format(num/2))
