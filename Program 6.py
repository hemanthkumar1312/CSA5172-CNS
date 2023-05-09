import string

# The ciphertext we want to decrypt
ciphertext = "BUBUBBBBUUUBBUBUBUBUBUBUBUBUBUBBU"

# Define the alphabet
alphabet = string.ascii_uppercase

# Count the frequency of each letter in the ciphertext
freqs = {letter: ciphertext.count(letter) for letter in alphabet}

# Sort the letters by frequency
sorted_letters = sorted(freqs, key=freqs.get, reverse=True)

# Get the most frequent letter and the second most frequent letter
most_frequent = sorted_letters[0]
second_most_frequent = sorted_letters[1]

# Compute the key
a = (alphabet.index(most_frequent) - alphabet.index(second_most_frequent)) % 26
b = (alphabet.index(most_frequent) - 1) % 26

# Define the decryption function
def decrypt(ciphertext, a, b):
    plaintext = ""
    for c in ciphertext:
        if c in alphabet:
            # Decrypt the letter using the inverse affine transformation
            plaintext += alphabet[(a * (alphabet.index(c) - b)) % 26]
        else:
            # Leave non-alphabetic characters unchanged
            plaintext += c
    return plaintext

# Decrypt the ciphertext using the computed key
plaintext = decrypt(ciphertext, a, b)
print(plaintext)
