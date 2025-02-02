import math

def volume(r):
    return (4/3)*math.pi*r**3

r = float(input("Enter radius: "))
print("Volume:",volume(r))