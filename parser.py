try:
    with open("messy_data.txt", 'r') as file:
        content = file.read() # Read the whole thing
        words = content.split() # Turn the text into a list of words

        # 1. THE ANALYSIS ENGINE (The Dictionary)
        word_counts = {}

        for word in words:
            # 2. THE SCALPEL: Strip away common punctation from the edges
            clean_word = word.strip(".,!?\"'").lower()

            if len(clean_word) > 7:
                # 3. THE TALLY LOGIC
                if clean_word in word_counts:
                    # We've seen it before, add 1
                    word_counts[clean_word] = word_counts[clean_word] + 1
                else:
                    # First time seeing it, start the tally at 1
                    word_counts[clean_word] = 1

        # 4. PRINTING THE REPORT
        print(f"--- FREQUENCY ANALYSIS REPORT" )
        for found_word, tally in word_counts.items():
            print(f"{found_word}: {tally}")
            
except FileNotFoundError:
    print("Error: File not found.")