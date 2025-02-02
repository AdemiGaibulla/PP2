def histogram(list):
    for x in list:
        print("*"*x)
    
mylist = list(map(int, input("Enter numbers: ").split()))
histogram(mylist)