def throw_party(*guests, **details):
    """
    Plans a party with a list of guests and various details.
    
    *guests: All positional arguments will be collected into a tuple.
    **details: All keyword arguments will be collected into a dictionary.
    """
       
    # --- 1. Handle the *guests (tuple) ---
    print("\n--- Guest List ---")
    if not guests:
        print("It's a solo party!")
    else:
        for i, guest in enumerate(guests, 1):
            print(f"{i}. {guest}")
            
    # --- 2. Handle the **details (dictionary) ---
    print("\n--- Party Details ---")
    if not details:
        print("No details provided yet. It's a mystery party!")
    else:
        # .items() lets you loop through the key and value
        for key, value in details.items():
            # Clean up the key for printing
            friendly_key = key.replace('_', ' ').capitalize()
            print(f"{friendly_key}: {value}")

# --- Let's try calling it! ---

print("--- EXAMPLE 1: With guests and details ---")
throw_party(
    "Alice", "Bob", "Charlie", "JC",                  # These will go into *guests list
    location="The Community Center",           # These will go into **details
    time="8:00 PM",
    food="Pizza and Tacos",
    theme="80s Night",
    master = "JC"
)
print("\n\n--- EXAMPLE 2: Just guests ---")
throw_party("Dr. Who", "Sarah Jane")           # **details will be an empty dict

print("\n\n--- EXAMPLE 3: Just details ---")
throw_party(                                  # *guests will be an empty tuple
    host="The Doctor",
    reason="Saved the world, again."
)