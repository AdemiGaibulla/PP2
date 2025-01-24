thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
thisdict["year"] = 2018
thisdict["color"] = "red"
print(thisdict)

thisdict.update({"year" : 2020})
thisdict.update({"color" : "red"})
print(thisdict)

thisdict.pop("model")
print(thisdict)

thisdict.popitem()
print(thisdict)

del thisdict["brand"]
print(thisdict)

thisdict.clear()
print(thisdict)