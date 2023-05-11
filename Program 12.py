def hill_encrypt(message, key):
    
    message = message.replace(" ", "").lower()
    
        
    
    if len(message) % 2 != 0:
        
        message += 'x'
    
    
    pairs = [message[i:i+2] for i in range(0, len(message), 2)]
    
    
    numerical_values = [ord(ch) - ord('a') for pair in pairs for ch in pair]
    
    
    encrypted_values = []
    for i in range(0, len(numerical_values), 2):
        x = numerical_values[i]
        y = numerical_values[i+1]
        encrypted_x = (key[0][0] * x + key[0][1] * y) % 26
        encrypted_y = (key[1][0] * x + key[1][1] * y) % 26
        encrypted_values.extend([encrypted_x, encrypted_y])
    
    
    encrypted_message = ''.join(chr(value + ord('a')) for value in encrypted_values)
    
    return encrypted_message



key = [[9, 4], [5, 7]]


message = "meet me at the usual place at ten rather than eight oclock"


encrypted_message = hill_encrypt(message, key)


print("Encrypted message:", encrypted_message)
