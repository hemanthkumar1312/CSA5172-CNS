import random

def generate_key(length):
    # Generate a random key of the given length
    key = [random.randint(0, 25) for i in range(length)]
    return key

def encrypt_vigenere_one_time_pad(plaintext, key):
    # Convert the plaintext to lowercase and remove spaces and punctuation
    plaintext = ''.join([c.lower() for c in plaintext if c.isalpha()])
    # Pad the key with zeros if it is shorter than the plaintext
    key = key + [0] * (len(plaintext) - len(key))
    # Encrypt the plaintext using the key
    ciphertext = ''
    for i in range(len(plaintext)):
        shift = key[i]
        ciphertext += chr((ord(plaintext[i]) - ord('a') + shift) % 26 + ord('a'))
    return ciphertext

# Example usage:
plaintext = 'Meet me at the park at noon'
key = generate_key(len(plaintext))
ciphertext = encrypt_vigenere_one_time_pad(plaintext, key)

print('Plaintext:', plaintext)
print('Key:', key)
print('Ciphertext:', ciphertext)
