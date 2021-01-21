"""
4. The third equation of motion gives the final velocity of an object
under uniform acceleration given the distance traveled and an initial velocity:

a. Using the equation above, build a function called (velocityFinal)
 which returns the final velocity of the object rounded to one decimal
 place. Use the following parameters
        u or vo (initial velocity)
        a (uniform acceleration)
        d (distance traveled)

b. A ball is gently dropped from a height of 51m (167 ft),
the acceleration due to gravity is a constant 9.8 m/s2.
Using the arguments described and function you built above,
what is the calling expression to determine the final velocity before impact?

c. Based on the function you created , calculate the speed of the ball
before it strikes the ground ? Answer should be in m/s
"""

import math   # import module to use sqrt function

# Function definition for velocityFinal
def velocityFinal(u, a, d):

    ''' Formula to find the final velocityself.
        It is rounded to one decimal place. '''
    fv = round(float((u + math.sqrt(2*a*d))), 1)
    return (fv)

def main():
    # ther is no initial velocity (0) for the ball when it is dropped
    fv = velocityFinal(0.0, 9.8, 51.0 )
    print('elapsed time is', fv , 'm/s')

    # calculate the speed of the ball before it strikes
    s = round(float((pow(fv, 2)/(2 * 9.8))), 2)
    print('The speed of the ball before it strikes is', s , 'm/s')

if __name__ == '__main__':
    main()
