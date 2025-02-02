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

mylist = list(map(int, input("Enter numbers: ").split()))
print("Prime numbers from list:",filter_prime(mylist))