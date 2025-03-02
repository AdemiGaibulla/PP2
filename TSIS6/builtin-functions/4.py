import time
from math import sqrt

number = int(input("Enter a number: "))
milliseconds = float(input("Enter a milliseconds: "))

time.sleep(milliseconds / 1000)

print("Square root of", number, "after", int(milliseconds), "milliseconds is", sqrt(number))
