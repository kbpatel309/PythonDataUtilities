# 1. Read the File
try:
    with open('iraq_data.txt', 'r') as file:
        content = file.read()
        print(content)

        words = {}

        for word in words:
            clean_word = word.strip(".,!?\"'").lower()

            # FILTER 1: High-complexity themes
            if len(clean_word) > 8:
                # Tally as a theme...

            # FILTER 2: Potential Years
            if len(clean_word) == 4 and clean_word.isdigit():
                # Tally as a date...
                

except FileNotFoundError:
    print("File not found.")