def spy_game(nums):
    n = ""
    for i in nums:
        if i == 0 or i == 7:
            n += str(i)
    if n == "007":
        return True
    return False

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))