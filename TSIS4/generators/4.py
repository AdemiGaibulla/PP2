def square_generator(a, b):
    for i in range(a, b+1):
        yield i**2


a = int(input("Enter a number 1: "))
b = int(input("Enter a number 2: "))

for x in square_generator(a, b):
    print(x)