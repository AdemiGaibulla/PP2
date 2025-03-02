text = input("Enter some string: ")

uppercount = sum(1 for i in text if i.isupper())
lowercount = sum(1 for i in text if i.islower())

print("The number of upper case letters:", uppercount)
print("The number of lower case letters:", lowercount)