def encrypt(text, key):
    """
    Encrypts text using columnar transposition cipher with the given key.
    """
    # Remove spaces and convert to uppercase for consistency
    text = text.replace(" ", "").upper()
    
    # Calculate dimensions of the matrix
    num_columns = len(key)
    num_rows = -(-len(text) // num_columns)  # Ceiling division
    
    # Pad the text with 'X' if needed
    padding = (num_rows * num_columns) - len(text)
    text += 'X' * padding
    
    # Create the matrix
    matrix = []
    for i in range(num_rows):
        row = list(text[i * num_columns : (i + 1) * num_columns])
        matrix.append(row)
    
    # Get the order of columns based on the key
    order = sorted(range(len(key)), key=lambda k: key[k])
    
    # Read off the columns in the order determined by the key
    ciphertext = ''
    for i in order:
        for row in matrix:
            ciphertext += row[i]
    
    return ciphertext

def decrypt(ciphertext, key):
    """
    Decrypts text encrypted with columnar transposition cipher using the given key.
    """
    num_columns = len(key)
    num_rows = -(-len(ciphertext) // num_columns)
    
    # Get the order of columns based on the key
    order = sorted(range(len(key)), key=lambda k: key[k])
    inverse_order = [0] * len(order)
    for i, pos in enumerate(order):
        inverse_order[pos] = i
    
    # Create an empty matrix
    matrix = [['' for _ in range(num_columns)] for _ in range(num_rows)]
    
    # Fill the matrix column by column according to the key order
    pos = 0
    for i in order:
        for row in range(num_rows):
            if pos < len(ciphertext):
                matrix[row][i] = ciphertext[pos]
                pos += 1
    
    # Read off the matrix row by row
    plaintext = ''
    for row in matrix:
        plaintext += ''.join(row)
    
    return plaintext

def main():
    while True:
        print("\nTransposition Cipher")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '3':
            break
            
        if choice in ['1', '2']:
            text = input("Enter the text: ")
            key = input("Enter the key (word or phrase): ")
            
            if choice == '1':
                result = encrypt(text, key)
                print(f"\nEncrypted text: {result}")
            else:
                result = decrypt(text, key)
                print(f"\nDecrypted text: {result}")
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
