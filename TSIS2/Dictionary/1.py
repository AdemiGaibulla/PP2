thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964,
    "year" : 2020,
    "colors" : ["red", "blue", "yellow"]
}

print(thisdict)

print(thisdict["brand"])

print(len(thisdict))

print(type(thisdict))

x = thisdict["model"]
y = thisdict.get("model")
z = thisdict.keys()
k = thisdict.values()
n = thisdict.items()
print(x,y)
print(z)
print(k)
print(n)

print("")

thisdict["color"] = "white"
thisdict["year"] = 2020
print(z)
print(k)
print(n)

mydict = dict(name = "John", age = 36, country = "Norway" )
print(mydict)

if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
