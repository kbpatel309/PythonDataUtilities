# We define this at the top so it's easy to change if we ever needed more precision
NAKSHATRA_WIDTH = 360 / 27

def get_nakshatra(total_degree):
    # The 27 Nakshatras (I'll start the list, you can finish it later!)
    nakshatras = [
        "Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashira", "Ardra",
        "Punarvasu", "Pushya", "Ashlesha", "Magha", "Purva Phalguni", "Uttara Phalguni",
        "Hasta", "Chitra", "Swati", "Vishakha", "Anuradha", "Jyeshtha",
        "Mula", "Purva Ashadha", "Uttara Ashadha", "Shravana", "Dhanishta", "Shatabhisha",
        "Purva Bhadrapada", "Uttara Bhadrapada", "Revati"
    ]

    # Data Normalization: Ensure input is within 0-359
    normalized_degree = total_degree % 360

    # Logic: How many '13.33' chunks fit into the degree?
    index = int(normalized_degree // NAKSHATRA_WIDTH)

    return {
        "nakshatra": nakshatras[index],
        "index": index + 1 # +1 because humans start counting at 1, not 0
    }

# Test it with a degree
print(get_nakshatra(0)) # Should be Ashwini
print(get_nakshatra(140)) # Let's see where the 140 degree Leo lands