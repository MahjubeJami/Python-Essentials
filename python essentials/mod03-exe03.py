"""
3. You are trying to build a program that will ask the user the following:
        First Name
        Temperature
Based on the user's entries, the program will recommend the user to wear
a T-shirt  if the temperature is over or equal to 70º or bring a sweater if it is less than 70º.

Console Output

What shall I wear today?
Please Enter Your First Name: John
What is Today's Temperature: 33
Hi John , You should probably bring a sweater
____________________________________________
Console Output
What shall I wear today?
Please Enter Your First Name: Mike
What is Today's Temperature: 75
Hi Mike , It will be a warm day , T-shirt time!

"""

print("What shall I wear today? \n")

name = input("Please Enter Your First Name: ")
temp = int(input("What is Today's Temperature: "))
print("\n")

if temp >= 70:
    print("Hi" , name, ", It will be a warm day , T-shirt time!")
elif temp < 70:
    print("Hi" , name , ", You should probably bring a sweater")
