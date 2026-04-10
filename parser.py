# THE MISSION: Just open and read the first line.

try:
    with open('messy_data.txt', 'r') as file:
        first_line = file.readline()
        print("--- MISSION SUCCESS: FIRST LINE DETECTED ---")
        print(first_line)
except FileNotFoundError:
    print("ERROR: The file 'messy_data.txt' wasn't found in this folder.")

    