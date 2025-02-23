import re

text = input("Enter string with uppercase letters: ")

result = re.findall(r"([A-Z][a-z]*)", text)

print(result)