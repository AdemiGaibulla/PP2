import os 

file = open(r'C:\Users\Адемi\OneDrive\Рабочий стол\pp2\PP2\TSIS6\dir-and-files\mbox.txt')
count = 0

for line in file:
    count += 1

print("Line count:", count)
