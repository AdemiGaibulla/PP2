list1 = ["orange", "mango", "kiwi", "pineapple", "banana"]
list1.sort()
print(list1)

list2 = [100, 50, 65, 82, 23]
list2.sort()
print(list2)

list3 = ["orange", "mango", "kiwi", "pineapple", "banana"]
list3.sort(reverse = True)
print(list3)

list4 = [100, 50, 65, 82, 23]
list4.sort(reverse = True)
print(list4)

def myfunc(n):
  return abs(n - 50)

list5 = [100, 50, 65, 82, 23]
list5.sort(key = myfunc)
print(list5)

list6 = ["banana", "Orange", "Kiwi", "cherry"]
list6.sort()
print(list6)

list7 = ["banana", "Orange", "Kiwi", "cherry"]
list7.sort(key = str.lower)
print(list7)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)