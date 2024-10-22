#Product Cipher#####
import numpy as np

def createMatrix(key):
    key = ''.join(dict.fromkeys(key.upper().replace('J', 'I')))
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    matrix = list(key + ''.join(char for char in alphabet if char not in key))
    return np.array(matrix).reshape(5, 5)
def findPosition(matrix, char):
    positions = np.where(matrix == char)
    return positions[0][0], positions[1][0]
def playFairEncrypt(plain_text, key):
    matrix = createMatrix(key)
    print("Matrix:\n", matrix)

    space_positions = [i for i, char in enumerate(plain_text) if char == ' ']
    plain_text = plain_text.upper().replace('J', 'I').replace(' ', '')
    
    pairs = []
    i = 0
    while i < len(plain_text):
        a = plain_text[i]
        b = plain_text[i + 1] if i + 1 < len(plain_text) else 'X'
        
        if a == b:
            b = 'X'
            i -= 1
        
        pairs.append((a, b))
        print(f"Pair: ({a}, {b})")
        i += 2

    cipher_text = ''
    for a, b in pairs:
        row_a, col_a = findPosition(matrix, a)
        row_b, col_b = findPosition(matrix, b)

        if row_a == row_b:
            cipher_text += matrix[row_a, (col_a + 1) % 5] + matrix[row_b, (col_b + 1) % 5]
        elif col_a == col_b:
            cipher_text += matrix[(row_a + 1) % 5, col_a] + matrix[(row_b + 1) % 5, col_b]
        else:
            cipher_text += matrix[row_a, col_b] + matrix[row_b, col_a]

    for _ in space_positions:
        cipher_text = cipher_text[:_] + '#' + cipher_text[_:]

    print("Encrypted text pairs:")
    for i in range(0, len(cipher_text) - 1, 2):
        print(f"Pair: ({cipher_text[i]}, {cipher_text[i+1]})")
    
    return cipher_text
def playFairEncrypt(plain_text, key):
    matrix = createMatrix(key)
    print("Matrix:\n", matrix)

    space_positions = [i for i, char in enumerate(plain_text) if char == ' ']
    plain_text = plain_text.upper().replace('J', 'I').replace(' ', '')
    
    pairs = []
    i = 0
    while i < len(plain_text):
        a = plain_text[i]
        b = plain_text[i + 1] if i + 1 < len(plain_text) else 'X'
        
        if a == b:
            b = 'X'
            i -= 1
        
        pairs.append((a, b))
        print(f"Pair: ({a}, {b})")
        i += 2

    cipher_text = ''
    for a, b in pairs:
        row_a, col_a = findPosition(matrix, a)
        row_b, col_b = findPosition(matrix, b)

        if row_a == row_b:
            cipher_text += matrix[row_a, (col_a + 1) % 5] + matrix[row_b, (col_b + 1) % 5]
        elif col_a == col_b:
            cipher_text += matrix[(row_a + 1) % 5, col_a] + matrix[(row_b + 1) % 5, col_b]
        else:
            cipher_text += matrix[row_a, col_b] + matrix[row_b, col_a]

    for _ in space_positions:
        cipher_text = cipher_text[:_] + '#' + cipher_text[_:]

    print("Encrypted text pairs:")
    for i in range(0, len(cipher_text) - 1, 2):
        print(f"Pair: ({cipher_text[i]}, {cipher_text[i+1]})")
    
    return cipher_text

def playFairDecrypt(cipher_text, key):
    matrix = createMatrix(key)
    plain_text = ''
    i = 0

    while i < len(cipher_text):
        if cipher_text[i] == '#':
            plain_text += ' '
            i += 1
            continue
        
        a, b = cipher_text[i:i + 2]
        row_a, col_a = findPosition(matrix, a)
        row_b, col_b = findPosition(matrix, b)

        if row_a == row_b:
            plain_text += matrix[row_a, (col_a - 1) % 5] + matrix[row_b, (col_b - 1) % 5]
        elif col_a == col_b:
            plain_text += matrix[(row_a - 1) % 5, col_a] + matrix[(row_b - 1) % 5, col_b]
        else:
            plain_text += matrix[row_a, col_b] + matrix[row_b, col_a]
        
        i += 2
    
    return plain_text
key = input("Enter the key: ")
plain_text = input("Enter the plain text: ")

cipher_text = playFairEncrypt(plain_text, key)
print(f"Encrypted text: {cipher_text}")

decrypted_text = playFairDecrypt(cipher_text, key)
print(f"Decrypted text: {decrypted_text}")
