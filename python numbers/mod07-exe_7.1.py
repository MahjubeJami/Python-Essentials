"""Write a program to print and insert the value
of tau in an available field width space of
8 characters (center aligned) , also print and
insert the value of ½ tau to determine the value
and insert / center align as shown in the first
console example below.)
Console:
The value of Tau is {}, which is two times {}."""

import math

t = math.tau
print('The value of Tau is{:8,.3f}'.format(t),end=',')

t2 = t/2
print(' which is two times{:8,.3f}.'.format(t2))
