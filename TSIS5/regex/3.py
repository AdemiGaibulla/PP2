import re

str = str(input("Enter some string joined with a underscore: "))
match = re.findall(r'[a-z]',str)

print(match)