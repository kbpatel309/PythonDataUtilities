import json
import os

# This is our "Database" File
DATABASE_FILE = "historical_events.json"

def save_event(name, date, sign, nakshatra):
    # 1. Create a data object
    event_data = {
        "event_name": name,
        "date": date,
        "astrology": {
            "zodiac_sign": sign, # English name
            "nakshatra": nakshatra
        }
    }

    # 2. Load existing data if the file exists
    if os.path.exists(DATABASE_FILE):
        with open(DATABASE_FILE, "r") as f:
            all_events = json.load(f)
    else:
        all_events = []

    # 3. Add the new event and save
    all_events.append(event_data)
    with open(DATABASE_FILE, "w") as f:
        json.dump(all_events, f, indent=4)

    print(f"Successfully archived: {name}")

# Example: Logging a Geopolitical Event
save_event("Meiji Restoration", "1868-01-03", "Sagittarius", "Mula")
save_event("Fall of Berlin Wall", "1989-11-09", "Aquarius", "Shatabhisha")

# How to explain this in an interview
# "I built a lightweight Data Persistence Layer to archive historical research data. I utilized the JSON format
# for its interoperability and implemented a logic flow that handles I/O operations, including checking for
# existing file paths and appending new records without overwriting historical data. This allowed me to build
# a structured dataset for long-term pattern analysis.""

# Potential interview question: How do you handle "data persistence"?
# "I implemented a JSON-based storage system for my research data. I chose JSON because it is language-agnostic
# and provides a clear schema for nested information. I built a 'Check-and-Append' logic to ensure Data Integrity,
# allowing me to build a growing library of historical events without risk of data loss. This allowed me to move
# from simple scripts to a persistent database that supports long-term trend analysis."



