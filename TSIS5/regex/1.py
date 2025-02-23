import re

str = str(input("Enter some string: "))
match = re.search(r'ab*',str)

if match:
    print("Yes, it matches")
else:
    print("No, it doesn't match")