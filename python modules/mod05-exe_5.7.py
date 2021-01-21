# 7. Write a lambda function (area_circle_lambda)
# that returns the area of a circle of a given radius.

from math import pi

r = float(input("Enter the radius of the circle: "))
area_circle_lambda = lambda r: round(pi * r**2 , 2)
print("The area of circle for given radius is: " , area_circle_lambda(r))
