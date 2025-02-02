def unique(list):
    new_list = []
    for x in list:
        if x not in new_list:
            new_list.append(x)
    return new_list

list = list(map(int, input("Enter numbers: ").split()))
print("Unique elements:",unique(list))