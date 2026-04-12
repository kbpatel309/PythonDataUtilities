try:
    with open("messy_data.txt", 'r') as file:
        content = file.read() # Read the whole thing
        words = content.split() # Turn the text into a list of words

        long_words = [] # This is your empty storage container

        for word in words:
            # THE SCALPEL: Strip away common punctation from the edges
            clean_word = word.strip(".,!?\"'")
            if len(clean_word) > 7:
                long_words.append(clean_word)

        print(f"--- INVESTIGATION COMPLETE: {len(long_words)} COMPLEX WORDS FOUND")
        print(long_words)
except FileNotFoundError:
    print("Error: File not found.")