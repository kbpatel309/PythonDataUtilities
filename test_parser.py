# 1. Read the File
try:
    with open('iraq_data.txt', 'r') as file:
        content = file.read()
        print(content)

        words = {}

        # 2. ANALYZE AND TALLY (The Engine)
        word_counts = {} # Bucket 1: For the Themes (words longer than 8 letters)
        year_counts = {} # Bucket 2: For the Timeline (only 4 characters long and only consist of digits)

        for word in words:
            clean_word = word.strip(".,!?\"'").lower()

            # FILTER 1: High-complexity themes
            if len(clean_word) > 8:
                # Tally as a theme...
                if clean_word in word_counts:
                    word_counts[clean_word] += 1
                else:
                    word_counts[clean_word] = 1

            # FILTER 2: Potential Years
            # .isdigit() checks if the string is made of only numbers
            if len(clean_word) == 4 and clean_word.isdigit():
                # Tally as a date...
                if clean_word in year_counts:
                    year_counts[clean_word] += 1
                else:
                    year_counts[clean_word] = 1
        
        # 3. SORT THE DATA
        sorted_themes = sorted(word_counts.items(), key=lambda item:item[1], reverse=True)

        # Sort the years chronologically instead of by frequency
        # Sorting by item[0] sorts the key (the year itself) instead of the tally
        sorted_years = sorted(year_counts.items(), key=lambda item:item[0])

        # 4. GENERATE THE PHYSICAL ASSET
        

except FileNotFoundError:
    print("File not found.")