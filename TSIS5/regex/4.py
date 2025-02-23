import re

str = str(input("Enter some string: "))
match = re.findall(r'[A-Z][a-z]+',str)

print(match)
