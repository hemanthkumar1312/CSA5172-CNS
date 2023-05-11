keyMatrix = [[0] * 3 for i in range(3)]
 
# Generate vector for the message
messageVector = [[0] for i in range(3)]
 
# Generate vector for the cipher
cipherMatrix = [[0] for i in range(3)]
 
# Following function generates the
# key matrix for the key string
def getKeyMatrix(key):
    k = 0
    for i in range(3):
        for j in range(3):
            keyMatrix[i][j] = ord(key[k]) % 65
            k += 1
 
# Following function encrypts the message
def encrypt(messageVector):
    for i in range(3):
        for j in range(1):
            cipherMatrix[i][j] = 0
            for x in range(3):
                cipherMatrix[i][j] += (keyMatrix[i][x] *
                                       messageVector[x][j])
            cipherMatrix[i][j] = cipherMatrix[i][j] % 26
 
def HillCipher(message, key):
 
    # Get key matrix from the key string
    getKeyMatrix(key)
 
    # Generate vector for the message
    for i in range(3):
        messageVector[i][0] = ord(message[i]) % 65
 
    # Following function generates
    # the encrypted vector
    print(encrypt(messageVector))
