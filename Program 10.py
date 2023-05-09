text = prepare_text(text)
    
    ciphertext = ""
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        a_pos, b_pos = matrix.index(a), matrix.index(b)
        a_row, a_col = a_pos // 5, a_pos % 5
        b_row, b_col = b_pos // 5, b_pos % 5
        if a_row == b_row:
            a_col = (a_col + 1) % 5
            b_col = (b_col + 1) % 5
        elif a_col == b_col:
            a_row = (a_row + 1) % 5
            b_row = (b_row + 1) % 5
        else:
            a_col, b_col = b_col, a_col
        ciphertext += matrix[a_row * 5 + a_col] + matrix[b_row * 5 + b_col]
    return ciphertext

def decrypt(ciphertext, key):
    
    matrix = generate_matrix(key)
    
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        a, b = ciphertext[i], ciphertext[i+1]
        a_pos, b_pos = matrix.index(a), matrix.index(b)
        a_row, a_col = a_pos // 5, a_pos % 5
        b_row, b_col = b_pos // 5, b_pos % 5
        if a_row == b_row:
            a_col = (a_col - 1) % 5
            b_col = (b_col - 1) % 5
        elif a_col == b_col:
            a_row = (a_row - 1) % 5
            b_row = (b_row - 1) % 5
        else:
            a_col, b_col = b_col, a_col
        plaintext += matrix[a_row * 5 + a_col] + matrix[b_row * 5 + b_col]
    return plaintext


plaintext = "must see you over cadogan west coming at once"
key = "MFHIKUNOPQZVWXYELARGDSTBC"
ciphertext = encrypt(plaintext, key)
print(ciphertext)  
decrypted_plaintext = decrypt(ciphertext, key)
print(decrypt)
