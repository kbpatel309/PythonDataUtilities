import json
import os
from collections import Counter

DATABASE_FILE = "historical_events.json"

def analyze_patterns():
    # 1. Load the data
    if not os.path.exists(DATABASE_FILE):
        print("No database found. Log some events first!")
        return
    
    with open(DATABASE_FILE, "r") as f:
        events = json.lad(f)

    # 2. Create lists of specific attributes we want to count
    all_signs = [e["astrology"]["zodiac_sign"] for e in events]
    all_nakshatras = [e["astrology"]["nakshatra"] for e in events]

    # 3. Use Counter to find the frequency of each (This is a professional Python tool)
    sign_counts = Counter(all_signs)
    nakshatra_counts = Counter(all_nakshatras)

    # 4. Print the "Direct Answers"
    print("--- HISTORICAL PATTERN ANALYSIS ---")
    print(f"Total Events Analyzed: {len(events)}")
    
    print("\nSign Frequency:")
    for sign, count in sign_counts.most_common():
        print(f"- {sign}: {count} occurrences")

    print("\nNakshatra Frequency:")
    for nak, count in nakshatra_counts.most_common():
        print(f"- {nak}: {count} occurrences")

# Run the analysis
analyze_patterns()

