def str_reverse(str):
    words = str.split()
    result = ""
    for i in range(1,len(words) + 1):
        result += words[-i] + " "
    return result

str = str(input("Enter a sentence: "))
print(str_reverse(str))