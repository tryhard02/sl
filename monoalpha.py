import random
import string

def generate_key():
    alphabet = list(string.ascii_uppercase)
    shuffled = alphabet.copy()
    random.shuffle(shuffled)
    return dict(zip(alphabet, shuffled))

def encrypt(plaintext, key):
    return ''.join(key.get(c.upper(), c) for c in plaintext)

def decrypt(ciphertext, key):
    rev_key = {v: k for k, v in key.items()}
    return ''.join(rev_key.get(c.upper(), c) for c in ciphertext)

def main():
    key = generate_key()
    print("Generated key:", key)
    while True:
        choice = input("Enter 'e' for encryption, 'd' for decryption, or 'q' to quit: ").lower()

        if choice == 'q':
            break
        elif choice == 'e':
            plaintext = input("Enter the plaintext to encrypt: ")
            ciphertext = encrypt(plaintext, key)
            print(f"Encrypted text: {ciphertext}")
        elif choice == 'd':
            ciphertext = input("Enter the ciphertext to decrypt: ")
            plaintext = decrypt(ciphertext, key)
            print(f"Decrypted text: {plaintext}")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
