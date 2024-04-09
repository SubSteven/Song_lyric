import time

# Lyrics snippet from "When I Was Your Man" by Bruno Mars
lyrics_snippet = """
Take you to every party 'cause all you wanted to do was dance
Now my baby's dancing
But she's dancing with another man
"""

# Function to simulate letter-by-letter display in order
def display_letters_in_order(lyrics):
    for line in lyrics.strip().split('\n'):
        for letter in line:
            print(letter, end='', flush=True)  # Print each letter without a newline
            time.sleep(0.1)  # Adjust the delay as needed for the desired effect
        print()  # Move to the next line
        time.sleep(1.5)  # Adjust the delay between lines as needed

# Run the function with the lyrics snippet
display_letters_in_order(lyrics_snippet)
