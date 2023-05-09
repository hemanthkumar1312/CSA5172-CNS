def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def is_valid(a, b):
    return gcd(a, 26) == 1 and gcd(b, 26) == 1

def encrypt(a, b, plaintext):
    ciphertext = ""
    for p in plaintext:
        if p.isalpha():
            # convert plaintext letter to number (A=0, B=1, ..., Z=25)
            p_num = ord(p.upper()) - ord('A')
            # apply encryption function
            c_num = (a * p_num + b) % 26
            # convert ciphertext number back to letter
            c = chr(c_num + ord('A'))
        else:
            c = p
        ciphertext += c
    return ciphertext

# Example usage
a = 3
b = 5
plaintext = "hemanthkumar"
if is_valid(a, b):
    ciphertext = encrypt(a, b, plaintext)
    print("Plaintext: ", plaintext)
    print("Ciphertext:", ciphertext)
else:
    print("Invalid values of a and/or b")
