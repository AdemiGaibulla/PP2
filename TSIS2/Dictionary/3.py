thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}

for x in thisdict:
    print(x)

print("\n")

for x in thisdict:
    print(thisdict[x])

print("\n")

for x in thisdict.values():
    print(x)

print("\n")

for x in thisdict.keys():
    print(x)

print("\n")

for x, y in thisdict.items():
    print(x, ":", y)

print("\n")

mydict1 = thisdict.copy()
print(mydict1)

mydict2 = dict(thisdict)
print(mydict2)


myfamily = {
    "child1" : {
        "name" : "Ademi",
        "year" : 2006
    },
    "child2" : {
        "name" : "Karina",
        "year" : 2010
    },
    "child3" : {
        "name" : "Erkezhan",
        "year" : 2013
    }
}
print(myfamily)

child1 = {
    "name" : "Ademi",
    "year" : 2006
}
child2 = {
    "name" : "Karina",
    "year" : 2010
}
child3 = {
    "name" : "Erkezhan",
    "year" : 2013
}

myfamily = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
}
print(myfamily)
print(myfamily["child1"]["name"])

print("\n")

for x, obj in myfamily.items():
    print(x)

    for y in obj:
        print(y+":", obj[y])