"""
3.Gases consist of atoms or molecules that move at different
speeds in random directions. The root mean square velocity
(RMS velocity) is a way to find a single velocity value for
the particles. The average velocity of gas particles is found
using the root mean square velocity formula:
     μrms = (3RT/M)½ root mean square velocity in m/sec
    R = ideal gas constant = 8.3145 (kg·m2/sec2)/K·mol
    T = absolute temperature in Kelvin
    M = mass of a mole of the gas in kilograms. molar mass of O2 = 3.2 x 10-2 kg/mol
    T = °C + 273

a. By using the decimal module, create a decimal object and apply the
sqrt and quantize method (match pattern “1.000”) and provide the answer
to the question:  What is the average velocity or root mean square
velocity of a molecule in a sample of oxygen at 25 degrees Celsius?

    Sample Console Output:

    The average velocity or root mean square velocity of a molecule in a sample of oxygen
    at 100 degrees Celsius is 539.210 m/sec
"""

from decimal import Decimal
import math

# msv = sgrt(3RT/M)
r = 8.3145
c = 25
t = c + 273
m = 3.2 * (1/100)

msv = Decimal(math.sqrt((3*r*t)/m)).quantize(Decimal("1.000"))
# msv = msv.quantize(Decimal("1.000"))
print("The average velocity or root mean square velocity of a molecule in a sample of oxygen at" ,c,"degrees Celsius is" ,msv, "m/sec")
