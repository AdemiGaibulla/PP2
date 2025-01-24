list1 = ["apple", "banana", "cherry"]
list1.remove("banana")
print(list1)

list2 = ["apple", "banana", "cherry", "banana", "kiwi"]
list2.remove("banana")
print(list2)

list3 = ["apple", "banana", "cherry"]
list3.pop(1)
print(list3)

list4 = ["apple", "banana", "cherry"]
list4.pop()
print(list4)

list5 = ["apple", "banana", "cherry"]
del list5[0]
print(list5)

list4.clear()
print(list4)

del list5
print(list5)

