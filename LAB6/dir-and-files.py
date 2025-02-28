import os
# 1

path = input("Enter path: ")

print("Dirs:", [name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))])
print("Files:", [name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))])
print("All:", os.listdir(path))

# 2

path = input("Enter path: ")

print("Exists:", os.access(path, os.F_OK))
print("Readable:", os.access(path, os.R_OK))
print("Writable:", os.access(path, os.W_OK))
print("Executable:", os.access(path, os.X_OK))

# 3

path = input("Enter path: ")

if os.path.exists(path):
    print("Path exists")
    print("name:", os.path.basename(path))
    print("Dir:", os.path.dirname(path))
else:
    print("doesn\'t exist")

# 4
file_path = input("Enter file path: ")

with open(file_path, 'r') as file:
    lines = file.readlines()

print("Number of lines:", len(lines))

# 5
data = ["apple", "banana", "cherry"]
file_path = input("Enter output file path: ")

with open(file_path, 'w') as file:
    for item in data:
        file.write(f"{item}\n")

# 6
import string, os

for letter in string.ascii_uppercase:
    filename = f"{letter}.txt"
    with open(filename, 'w') as file:
        file.write(f"This is file {filename}\n")
print("Files created:", os.listdir('.'))

# 7
source_path = input("Enter source file path: ")
destination_path = input("Enter destination file path: ")

with open(source_path, 'r') as source, open(destination_path, 'w') as destination:
    destination.write(source.read())

print(f"Content copied from {source_path} to {destination_path}")

# 8
source_path = input("Enter source file path: ")
destination_path = input("Enter destination file path: ")

with open(source_path, 'r') as source, open(destination_path, 'w') as destination:
    destination.write(source.read())

print(f"Content copied from {source_path} to {destination_path}")
