def isPrime(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def filter_prime(list):
    prime_nums = []
    for x in list:
        if isPrime(x):
            prime_nums.append(x)
    return prime_nums

def has_33(nums):
    for i in range(len(nums) -1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

def spy_game(nums):
    n = ""
    for i in nums:
        if i == 0 or i == 7:
            n += str(i)
    if n == "007":
        return True
    return False

def unique(list):
    new_list = []
    for x in list:
        if x not in new_list:
            new_list.append(x)
    return new_list

mylist = list(map(int, input("Enter numbers: ").split()))
print("1)Prime numbers from list: ",filter_prime(mylist))
if has_33(mylist):
    print("This list has 33")
else: 
    print("This list doesn't have 33")
if spy_game(mylist):
    print("This list has 007")
else:
    print("This list doesn't have 007")
print("Unique elements from list:", unique(mylist))