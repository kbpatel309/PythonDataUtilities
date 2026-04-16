# TEMPLATE: Open a file safely
try:
    with open('filename.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("File not found.")

# TEMPLATE: Create an write an intelligence report
try:
    # 1. READ THE MESSY DATA
    with open("messy_data.txt", 'r') as file:
        content = file.read() # Read the whole thing
        words = content.split() # Turn the text into a list of words

        # 2. ANALYZE AND TALLY (The Engine)
        word_counts = {}

        for word in words:
            clean_word = word.strip(".,!?\"'").lower()

            if len(clean_word) > 7:
                if clean_word in word_counts:
                    # We've seen it before, add 1
                    word_counts[clean_word] = word_counts[clean_word] + 1
                else:
                    # First time seeing it, start the tally at 1
                    word_counts[clean_word] = 1

        # 3. SORT THE DATA (Highest to Lowest)
        sorted_report = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)

        # 4. GENERATE THE PHYSICAL ASSET
        # The 'w' tells Python: "If this file doesn't exist, create it. If it does, overwrite it."
        with open('intelligence_report.txt', 'w') as report:
            report.write("--- FREQUENCY ANALYSIS: TOP 5 TARGETS ---\n\n")

            for found_word, tally in sorted_report[:5]:
                # The \n is crucial here. It acts as the "Enter" key, forcing a new line
                report.write(f"TARGET: {found_word.upper()} | FREQUENCY: {tally}\n")

        # Give yourself a visual confirmation in the terminal
        print("--- SUCCESS: 'intelligence_report.txt' has been generated in your folder.")

except FileNotFoundError:
    print("Error: The file 'messy_data.txt' was not found.")

