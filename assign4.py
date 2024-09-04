# Reverse the content of the string
def reverse_string(s):
    reversed_str = ''
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

# Basic string compression using counts of repeated characters
def compress_string(s):
    compressed_str = ''
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed_str += s[i - 1] + str(count)
            count = 1
    compressed_str += s[-1] + str(count)
    return compressed_str

# Caesar cipher decryption
def decrypt_caesar_cipher(cipher_text, shift):
    decrypted_text = ''
    for char in cipher_text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                decrypted_text += chr((ord(char) - shift_amount - ord('a')) % 26 + ord('a'))
            else:
                decrypted_text += chr((ord(char) - shift_amount - ord('A')) % 26 + ord('A'))
        else:
            decrypted_text += char
    return decrypted_text

# Shift cipher brute force decryption
def brute_force_caesar(cipher_text):
    for shift in range(26):
        print(f"Shift {shift}: {decrypt_caesar_cipher(cipher_text, shift)}")

# Find k value for Affine cipher
def find_affine_key(cipher_text, plain_text):
    def mod_inverse(a, m):
        a = a % m
        for x in range(1, m):
            if (a * x) % m == 1:
                return x
        raise ValueError("No modular inverse found")

    def affine_decrypt(c, a, b):
        a_inv = mod_inverse(a, 26)
        return ''.join([chr((a_inv * (ord(c) - ord('A') - b)) % 26 + ord('A')) for c in cipher_text])

    for a in range(1, 26):
        for b in range(26):
            decrypted_text = affine_decrypt(cipher_text, a, b)
            if decrypted_text == plain_text:
                return a, b
    return None

# Encrypt and decrypt using Atbash cipher
def atbash_cipher(text):
    encrypted_text = ''
    decrypted_text = ''
    for char in text:
        if char.isalpha():
            if char.islower():
                encrypted_text += chr(219 - ord(char))  # 'a' + 'z' = 219
                decrypted_text += chr(219 - ord(char))
            else:
                encrypted_text += chr(155 - ord(char))  # 'A' + 'Z' = 155
                decrypted_text += chr(155 - ord(char))
        else:
            encrypted_text += char
            decrypted_text += char
    return encrypted_text, decrypted_text

# Encrypt and decrypt using Affine cipher
def affine_cipher_encrypt(plaintext, a, b):
    return ''.join([chr((a * (ord(char) - ord('A')) + b) % 26 + ord('A')) for char in plaintext.upper() if char.isalpha()])

def affine_cipher_decrypt(ciphertext, a, b):
    def mod_inverse(a, m):
        a = a % m
        for x in range(1, m):
            if (a * x) % m == 1:
                return x
        raise ValueError("No modular inverse found")

    a_inv = mod_inverse(a, 26)
    return ''.join([chr((a_inv * (ord(char) - ord('A') - b)) % 26 + ord('A')) for char in ciphertext.upper() if char.isalpha()])

# Main function to execute all tasks
def main():
    print("1. Reverse the content of the string")
    s = input("Enter a string to reverse: ")
    print("Reversed string:", reverse_string(s))

    print("\n2. Basic string compression")
    s = input("Enter a string for compression: ")
    print("Compressed string:", compress_string(s))

    print("\n3. Caesar cipher decryption")
    cipher_text = input("Enter the Caesar cipher text: ")
    shift = int(input("Enter the shift value: "))
    print("Decrypted text:", decrypt_caesar_cipher(cipher_text, shift))

    print("\n4. Caesar cipher brute force decryption")
    cipher_text = input("Enter the Caesar cipher text for brute force decryption: ")
    brute_force_caesar(cipher_text)

    print("\n5. Find k value for Affine cipher")
    cipher_text = input("Enter the Affine cipher text: ")
    plain_text = input("Enter the corresponding plain text: ")
    result = find_affine_key(cipher_text, plain_text)
    if result:
        a, b = result
        print(f"Affine cipher key found: a = {a}, b = {b}")
    else:
        print("No valid key found.")

    print("\n6. Atbash cipher encryption and decryption")
    text = input("Enter text for Atbash cipher: ")
    encrypted, decrypted = atbash_cipher(text)
    print(f"Encrypted text: {encrypted}")
    print(f"Decrypted text: {decrypted}")

    print("\n7. Affine cipher encryption and decryption")
    plaintext = input("Enter plaintext for Affine cipher encryption: ")
    a = int(input("Enter a (key1) for Affine cipher: "))
    b = int(input("Enter b (key2) for Affine cipher: "))
    encrypted = affine_cipher_encrypt(plaintext, a, b)
    decrypted = affine_cipher_decrypt(encrypted, a, b)
    print(f"Encrypted text: {encrypted}")
    print(f"Decrypted text: {decrypted}")

if __name__ == "__main__":
    main()

