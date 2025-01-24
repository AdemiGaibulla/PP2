thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

set5 = set1.union(set2)
print(set5)

set6 = set1 | set2
print(set6)

set7 = set1.union(set2, set3, set4)
print(set7)

set8 = set1 | set2 | set3 | set4
print(set8)

x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)

