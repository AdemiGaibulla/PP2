set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

set3 = set1 & set2
print(set3)

set1.intersection_update(set2)
print(set1)

set4 = {"apple", 1,  "banana", 0, "cherry"}
set5 = {False, "google", 1, "apple", 2, True}
set6 = set4.intersection(set5)
print(set6)

print("")

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)
print(set3)

set3 = set1 - set2
print(set3)

set1.difference_update(set2)
print(set1)

print("")

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)
print(set3)

set3 = set1 ^ set2
print(set3)

set1.symmetric_difference_update(set2)
print(set1)