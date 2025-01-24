thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

print("banana" in thisset)
print("banana" not in thisset)

thisset.add("orange")
print(thisset)

tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

myset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
myset.update(mylist)
print(myset)