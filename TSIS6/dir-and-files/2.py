import os

def  check_for_access(path):
    exists = os.path.exists(path)
    readable = os.path.access(path, os.R_OK)
    writable = os.path.access(path, os.W_OK)
    executable = os.path.access(path, os.X_OS)

    return exists, readable, writable, executable

path = input("Enter the path: ")

exists, readable, writable, executable = check_for_access(path)
print(f"Exists: {exists}, Readable: {readable}, Writable: {writable}, Executable: {executable}")