def str_reverse(s):
    result = ""
    for i in range(1,len(s) + 1):
        result += s[-i]
    return result

def isPalindrome(str):
    if str.lower() == str_reverse(str).lower():
        print("Yes, it's a palindrome")
    else:
        print("No, it's not a palindrome")

somestr = str(input("Enter word or phrase: "))
isPalindrome(somestr)