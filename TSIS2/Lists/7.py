fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)
print(1, newlist)


fruits2 = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist2 = [x for x in fruits2 if "a" in x]
print(2, newlist2)

newlist3 = [x.upper() for x in fruits2]
print(3, newlist3)

newlist4 = ['hello' for x in fruits2]
print(4, newlist4)

newlist5 = [x if x != "banana" else "orange" for x in fruits2]
print(5, newlist5)

list = [x for x in range(10) if x < 5]
print(6, list)
