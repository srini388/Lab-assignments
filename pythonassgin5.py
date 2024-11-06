import itertools
import string

# Function to perform brute force attack on a simple substitution cipher
def brute_force_decrypt(ciphertext):
    charset = string.ascii_lowercase
    print("Brute Force Decrypting:")
    
    for key_length in range(1, 6):  # Trying keys of length 1 to 5
        for key in itertools.product(charset, repeat=key_length):
            key = ''.join(key)
            decrypted_text = ''.join(chr((ord(c) - ord(key[i % key_length]) + 26) % 26 + ord('a')) for i, c in enumerate(ciphertext))
            print(f"Trying key: {key} -> Decrypted text: {decrypted_text}")

# Function to find modular inverse
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# Function to decrypt using Affine cipher
def affine_decrypt(ciphertext, a, b):
    decrypted_text = ""
    m = 26  # Size of the alphabet
    a_inv = mod_inverse(a, m)

    if a_inv is None:
        return "No modular inverse found for a."

    for char in ciphertext:
        if char.isalpha():
            y = ord(char) - ord('A')  # Convert char to number (0-25)
            x = (a_inv * (y - b)) % m
            decrypted_text += chr(x + ord('A'))  # Convert back to char
        else:
            decrypted_text += char

    return decrypted_text

# Rail Fence Cipher Encryption
def rail_fence_encrypt(plaintext, rails):
    rail = [['\n' for i in range(len(plaintext))] for j in range(rails)]
    
    direction_down = False
    row, col = 0, 0
    
    for char in plaintext:
        if row == 0 or row == rails - 1:
            direction_down = not direction_down
        
        rail[row][col] = char
        col += 1
        
        if direction_down:
            row += 1
        else:
            row -= 1
            
    cipher_text = ""
    for r in rail:
        cipher_text += "".join(r).replace('\n', '')
    
    return cipher_text

# Rail Fence Cipher Decryption
def rail_fence_decrypt(ciphertext, rails):
    rail = [['\n' for i in range(len(ciphertext))] for j in range(rails)]
    
    direction_down = None
    row, col = 0, 0
    
    # Mark the positions of rails with '*'
    for char in ciphertext:
        if row == 0:
            direction_down = True
        if row == rails - 1:
            direction_down = False
        
        rail[row][col] = '*'
        col += 1
        
        if direction_down:
            row += 1
        else:
            row -= 1
    
    index = 0
    for i in range(rails):
        for j in range(len(ciphertext)):
            if ((rail[i][j] == '*') and (index < len(ciphertext))):
                rail[i][j] = ciphertext[index]
                index += 1
    
    result = []
    row, col = 0, 0
    
    for i in range(len(ciphertext)):
        if row == 0:
            direction_down = True
        if row == rails - 1:
            direction_down = False
        
        if rail[row][col] != '*':
            result.append(rail[row][col])
            col += 1
        
        if direction_down:
            row += 1
        else:
            row -= 1
            
    return ''.join(result)

# Main execution block
if __name__ == "__main__":
    
    # Part 1: Brute Force Attack on Cipher Text
    print("=== Brute Force Attack ===")
    ciphertext_brute_force = "dvvkzecfssprkkve"
    brute_force_decrypt(ciphertext_brute_force)

    # Part 2: Affine Cipher Deciphering
    print("\n=== Affine Cipher Deciphering ===")
    affine_ciphertext = "XPALASXYFGFUKPXUSOGEUTKCDGFXANMGNVS"
    
    # Brute force search for keys (a and b)
    for a in range(1, 26):
        if gcd(a, 26) == 1:  # Check if 'a' is coprime with 26
            for b in range(0, 26):
                decrypted_message = affine_decrypt(affine_ciphertext, a, b)
                print(f"a={a}, b={b} -> Decrypted message: {decrypted_message}")

    # Part 3: Rail Fence Cipher Encryption
    print("\n=== Rail Fence Cipher Encryption ===")
    plaintext_rail_fence = "HELLO WORLD"
    rails_rail_fence = 3
    encrypted_message_rail_fence = rail_fence_encrypt(plaintext_rail_fence.replace(" ", ""), rails_rail_fence)
    print(f"Encrypted Message: {encrypted_message_rail_fence}")

    # Part 4: Rail Fence Cipher Decryption
    print("\n=== Rail Fence Cipher Decryption ===")
    ciphertext_rail_fence = encrypted_message_rail_fence
    decrypted_message_rail_fence = rail_fence_decrypt(ciphertext_rail_fence.replace(" ", ""), rails_rail_fence)
    print(f"Decrypted Message: {decrypted_message_rail_fence}")
