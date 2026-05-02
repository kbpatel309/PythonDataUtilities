def get_vedic_sign(total_degree):
    """
    Takes a total degree (0-360) and returns the Vedic Sign
    and the relative degree (0-30).
    """
    # 1. The Data Structure: A list of the 12 Vedic signs
    signs = [
        "Mesha", "Vrishabha", "Mithuna", "Karkata",
        "Simha", "Kanya", "Tula", "Vrishchika",
        "Dhanu", "Makara", "Kumbha", "Meena"
    ]

    try:
        # 2. Data Normalization: Ensure input is within 0-359
        # This handles a case where a user might input 370 degrees
        normalized_degree = total_degree % 360

        # 3. Categorical Mapping: Find which 30-degree "box" it falls into
        # // is floor division (e.g., 140 // 30 = 4)
        sign_index = int(normalized_degree // 30)

        # 4. Relative Offset: Find the degree within that sign
        # % is modulo (e.g., 140 % 30 = 20)
        relative_degree = normalized_degree % 30

        # 5. Return the result as a Dictionary for easy access
        return {
            "sign": signs[sign_index],
            "degree": round(relative_degree, 2),
            "full_string": f"{round(relative_degree, 2)}° {signs[sign_index]}"
        }
    
    except TypeError:
        return "Error: Please provide a valid number for the degree."
    
# --- TEST CASES ---
# You can run these to make sure your engine is working!
print(get_vedic_sign(140)) # Expected: 20° Simha
print(get_vedic_sign(45.5)) # Expected: 15.5° Vrishabha
print(get_vedic_sign(355)) # Expected: 25° Meena

# How to explain in an interview
# "I developed a utility to transform continuous longitudinal data into discrete categories. I implemented a mapping algorithm 
# using floor division and modulo arithmetic to normalize 360-degree coordinates into 30-degree segments. 
# I chose to return the data in a Dictionary format to ensure the 'Sign' and 'Relative Degree' remained coupled, 
# making the data easier for other parts of the application to consume."