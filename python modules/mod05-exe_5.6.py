# 6. Write a simple function (area_circle) that returns 
# the area of a circle of a given radius.


from math import pi

r = float(input("Enter the radius of the circle: "))
def area_circle(r):
    return round(pi * r**2 , 2)
print("The area of circle for given radius is: " , area_circle(r))
