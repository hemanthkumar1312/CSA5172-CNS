import math

# Define the Playfair cipher alphabet (excluding 'j')
alphabet = 'abcdefghiklmnopqrstuvwxyz'

# Define the function to generate all possible keys
def generate_keys():
    keys = []
    for letter1 in alphabet:
        for letter2 in alphabet:
            if letter1 != letter2:
                keys.append(letter1 + letter2)
    return keys

# Calculate the number of possible keys and the exponent for 2
num_keys = len(generate_keys())
exponent = math.log2(num_keys)

# Print the result
print(f"The Playfair cipher has approximately 2^{exponent:.2f} possible keys.")
