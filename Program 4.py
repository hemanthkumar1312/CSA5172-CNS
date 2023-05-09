"""from textwrap import wrap
n = "abcdefghijklmnopqrstuvwxyz"
s = input("enter the plain text:")
key = input("Enter key content:")
b = []
for i in range(len(key)):
    k = key[i]
    b.append(k)
li = [*set(b)]
for i in range(len(li)):
    for j in range(len(li)):
        if ord(li[i]) < ord(li[j]):
           li[i], li[j] = li[j], li[i]
li1 = []
for i in range(len(n)):
    m = n[i]
    li1.append(m)
for i in range(len(li)):
    l = n.find(li[i])
    li1.remove(n[l])
for i in range(len(li1)):
    key = key + li1[i]
print(key)
z = wrap(key,5)
print(z)
# alpha_matrix = [list(key[i:i+5]) for i in range(0, 26, 5)] 
alpha_matrix = []
for i in range(0, 26, 5):
    temp_list = list(key[i: i+5])
    alpha_matrix.append(temp_list)
print('\n')
for sub_list in alpha_matrix:
    print(*sub_list)
alpha_matrix[i][j]
alpha_matrix[0][j]
alpha_matrix[i][0]
"""
import string

def generate_matrix(key):
    """
    Generates a 5x5 matrix of letters using the given keyword.
    """
    key = key.lower().replace("j", "i")
    alphabet = string.ascii_lowercase.replace("j", "")
    key_set = set(key)
    matrix = []
    for c in key:
        if c not in matrix:
            matrix.append(c)
    for c in alphabet:
        if c not in key_set and c not in matrix:
            matrix.append(c)
    matrix = [matrix[i:i+5] for i in range(0, 25, 5)]
    return matrix

def encrypt(plaintext, key):
    """
    Encrypts the plaintext using the given key and returns the ciphertext.
    """
    plaintext = plaintext.lower().replace("j", "i").replace(" ", "")
    matrix = generate_matrix(key)
    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        a = plaintext[i]
        b = plaintext[i+1] if i+1 < len(plaintext) else "x"
        if a == b:
            b = "x"
        a_row, a_col = get_position(matrix, a)
        b_row, b_col = get_position(matrix, b)
        if a_row == b_row:
            a_col = (a_col + 1) % 5
            b_col = (b_col + 1) % 5
        elif a_col == b_col:
            a_row = (a_row + 1) % 5
            b_row = (b_row + 1) % 5
        else:
            a_col, b_col = b_col, a_col
        ciphertext += matrix[a_row][a_col] + matrix[b_row][b_col]
    return ciphertext

def decrypt(ciphertext, key):
    """
    Decrypts the ciphertext using the given key and returns the plaintext.
    """
    matrix = generate_matrix(key)
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        a = ciphertext[i]
        b = ciphertext[i+1]
        a_row, a_col = get_position(matrix, a)
        b_row, b_col = get_position(matrix, b)
        if a_row == b_row:
            a_col = (a_col - 1) % 5
            b_col = (b_col - 1) % 5
        elif a_col == b_col:
            a_row = (a_row - 1) % 5
            b_row = (b_row - 1) % 5
        else:
            a_col, b_col = b_col, a_col
        plaintext += matrix[a_row][a_col] + matrix[b_row][b_col]
    plaintext = plaintext.replace("x", "")
    return plaintext

def get_position(matrix, letter):
    """
    Returns the position of the given letter in the matrix.
    """
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == letter:
                return i, j
    return -1, -1


# Example usage
key = 'apple'
plaintext = 'hemanth'
ciphertext = encrypt(plaintext, key)
print("!encryption!")
print(ciphertext)
print("!decryption!")
print(plaintext)
