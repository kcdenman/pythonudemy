# python program to find the area of a triangle

# sides of triangle

import math
from math import sqrt


# a = 3
# b = 4
# c = 5

# give user ability to input values

a = float(input('Enter side a: '))
b = float(input('Enter side b: '))
c = float(input('Enter side c: '))

# source of herons formula https://www.mathopenref.com/heronsformula.html

# calculate semi-variable

s = (a + b + c)/2 

area = sqrt(s*(s-a)*(s-b)*(s-c))

print('the area is', area)

