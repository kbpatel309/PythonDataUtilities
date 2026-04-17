# 1. Read the File
try:
    with open('iraq_data.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found.")