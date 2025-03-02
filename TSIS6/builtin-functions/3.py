text = input("Enter some string: ")

text2 = "".join(reversed(text))

if text.lower() == text2.lower():
    print("Yes, it is palindrome")
else:
    print("No, it isn't palindrome")