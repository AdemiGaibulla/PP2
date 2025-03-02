import os

mylist = list(map(str, input("Enter items: ").split()))

with open (r'C:\Users\Адемi\OneDrive\Рабочий стол\pp2\PP2\TSIS6\dir-and-files\mbox.txt', 'w') as file:
    for item in mylist:
        file.write(item+" ")

        