import os

string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for letter in string:
    file_path = os.path.join(r"C:\Users\Адемi\OneDrive\Рабочий стол\pp2\PP2\TSIS6\dir-and-files\letters", f"{letter}.txt")
    with open(file_path, 'w') as file:
        file.write(f"This is {letter}.txt file")

