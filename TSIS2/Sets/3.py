set1 = {"apple", "banana", "cherry"}
set1.remove("banana")
print(set1)

set2 = {"apple", "banana", "cherry"}
set2.discard("banana")
print(set2)

set3 = {"apple", "banana", "cherry"}
x = set3.pop()
print(x)
print(set3)

set4 = {"apple", "banana", "cherry"}
set4.clear()
print(set4)

set5 = {"apple", "banana", "cherry"}
del set5
print(set5)