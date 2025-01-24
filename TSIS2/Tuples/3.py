x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

tuple1 = ("apple", "banana", "cherry")
y = list(tuple1)
y.append("orange")
tuple1 = tuple(y)
print(tuple1)

tuple2 = ("apple", "banana", "cherry")
y = ("orange",)
tuple2 += y
print(tuple2)

tuple3 = ("apple", "banana", "cherry")
y = list(tuple3)
y.remove("apple")
tuple3 = tuple(y)
print(tuple3)

tuple4 = ("apple", "banana", "cherry")
del tuple4
print(tuple4)