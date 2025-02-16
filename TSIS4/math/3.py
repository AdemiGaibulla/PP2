from math import *

n = int(input("Input number of sides: "))
l = int(input("Input the length of a side: "))
a = n*l**2 / (4*tan(pi/n))
print("The area of the polygon is:", int(a))