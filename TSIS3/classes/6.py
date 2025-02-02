is_prime = lambda x : x >= 2 and all(x % i !=0 for i in range(2,x))

mylist = list(map(int, input("Enter numbers: ").split()))

prime_numbers = list(filter(is_prime, mylist))

print("Prime numbers from list:",prime_numbers)