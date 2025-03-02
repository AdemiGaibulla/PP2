import os

path = input("Enter the path")

if os.path.exists(path):
    filename = os.path.basename(path)
    directory_portion = os.path.dirname(path)
    print("Path exists: True", "\n", "filename:", filename, "\n", "directory portion:", directory_portion)
else:
    print("Path does not exist.")