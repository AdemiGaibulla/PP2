import os

def list_directories(path):
    directories = []
    for i in os.listdir(path):
        if os.path.isdir(os.path.join(path, i)):
            directories.append(i)
    return directories

def list_files(path):
    files = []
    for i in os.listdir(path):
        if os.path.isfile(os.path.join(path, i)):
            files.append(i)
    return files

def list_both(path):
    return os.listdir(path)

path = input("Enter the path: ")

print("Directories:", list_directories(path))
print("Files:", list_files(path))
print("All directories, files:", list_both(path))
