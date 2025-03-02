import os

path = input("Enter the path: ")

if os.path.exists(path):
    if os.access(path, os.W_OK):
        os.remove(path)
        print("File deleted")
    else:
        print("File isn't writable")
else:
    print("File doesn't exist")