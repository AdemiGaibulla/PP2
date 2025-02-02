def permute(s, permutation =""):
    if len(s) == 0:
        print(permutation)
    else:
        for i in range(len(s)):
            permute(s[:i] + s[i+1:], permutation + s[i])

str = input("Enter a string: ")
print("Permutations:")
permute(str)
