thislist = ["apple", "banana", "cherry"]

thislist.append("orange")
print(thislist)

thislist.insert(1, "watermelon")
print(thislist)

tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

anotherlist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
anotherlist.extend(thistuple)
print(anotherlist)