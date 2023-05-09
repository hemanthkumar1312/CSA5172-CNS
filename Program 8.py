import string

def generate_cipher_sequence(keyword):
    """
    Given a keyword, generates the cipher sequence by appending the unused letters in normal order
    to the keyword and returning the resulting string.
    """
    keyword = keyword.upper()
    unused_letters = ''.join([letter for letter in string.ascii_uppercase if letter not in keyword])
    return keyword + unused_letters

def encrypt(plaintext, keyword):
    """
    Encrypts a plaintext message using the given keyword and the generated cipher sequence.
    """
    cipher_sequence = generate_cipher_sequence(keyword)
    plaintext = plaintext.upper()
    ciphertext = ''
    for letter in plaintext:
        if letter in string.ascii_uppercase:
            index = string.ascii_uppercase.index(letter)
            ciphertext += cipher_sequence[index]
        else:
            ciphertext += letter
    return ciphertext

def decrypt(ciphertext, keyword):
    """
    Decrypts a ciphertext message using the given keyword and the generated cipher sequence.
    """
    cipher_sequence = generate_cipher_sequence(keyword)
    plaintext = ''
    for letter in ciphertext:
        if letter in string.ascii_uppercase:
            index = cipher_sequence.index(letter)
            plaintext += string.ascii_uppercase[index]
        else:
            plaintext += letter
    return plaintext

# Example usage
plaintext = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
keyword = "CIPHER"

# Encrypt the plaintext
ciphertext = encrypt(plaintext, keyword)
print("Ciphertext:")
print(ciphertext)

# Decrypt the ciphertext
decrypted_plaintext = decrypt(ciphertext, keyword)
print("Decrypted plaintext:")
print(decrypted_plaintext)
