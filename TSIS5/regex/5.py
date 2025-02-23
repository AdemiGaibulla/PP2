import re

str = str = str(input("Enter some string: "))

match = re.search(r'a.*b',str)

if match:
    print("Yes, it matches")
else:
    print("No, it doesn't match")