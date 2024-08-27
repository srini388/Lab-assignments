import string
import os

# 1. Encrypt the string using Caesar cipher
def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    shift = shift % 26  # Normalize the shift amount to be within 0-25
    
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            encrypted_text += chr(start + (ord(char) - start + shift) % 26)
        else:
            encrypted_text += char  # Non-alphabetic characters are not encrypted
    
    return encrypted_text

# 2. Modify the Caesar cipher to shift based on user choice
def get_shift_from_user():
    while True:
        try:
            shift = int(input("Enter the shift amount (integer): "))
            return shift
        except ValueError:
            print("Invalid input. Please enter an integer.")

def validate_input(text):
    if not text.isalpha():
        raise ValueError("Input should contain only alphabetic characters.")
    return text.lower()

def main():
    # 1 & 2. Encrypt the string with Caesar cipher and shift based on user choice
    user_text = input("Enter the text to encrypt: ")
    user_text = validate_input(user_text)
    shift = get_shift_from_user()
    encrypted_text = caesar_cipher_encrypt(user_text, shift)
    
    print("Encrypted text:", encrypted_text)
    
    # 3. Convert cipher text into uppercase characters and split into groups of 5
    upper_text = encrypted_text.upper()
    grouped_text = ' '.join(upper_text[i:i+5] for i in range(0, len(upper_text), 5))
    print("Uppercase and grouped text:", grouped_text)

    # 4. Find the histogram for each character
    def char_histogram(text):
        histogram = {}
        for char in text:
            if char.isalpha():
                if char in histogram:
                    histogram[char] += 1
                else:
                    histogram[char] = 1
        return histogram
    
    histogram = char_histogram(user_text)
    print("Character Histogram:", histogram)

    # 5. Read the contents from a file
    def read_file(file_path):
        if not os.path.exists(file_path):
            print(f"File {file_path} does not exist.")
            return ""
        with open(file_path, 'r') as file:
            return file.read()

    # 6. Encrypt the contents from a file
    def encrypt_file_contents(file_path, shift):
        text = read_file(file_path)
        return caesar_cipher_encrypt(text, shift)
    
    file_path = input("Enter the file path to read and encrypt: ")
    file_contents = read_file(file_path)
    if file_contents:
        encrypted_file_contents = caesar_cipher_encrypt(file_contents, shift)
        print("Encrypted file contents:", encrypted_file_contents)
        # Optionally write the encrypted contents to a new file
        with open('encrypted_file.txt', 'w') as file:
            file.write(encrypted_file_contents)
        print("Encrypted contents saved to 'encrypted_file.txt'.")

    # 7. Validation of user input
    # This functionality is included in the `validate_input` function above.

    # 8. Check if two given strings are anagrams
    def are_anagrams(str1, str2):
        return sorted(str1) == sorted(str2)
    
    string1 = input("Enter the first string to check for anagrams: ").replace(" ", "").lower()
    string2 = input("Enter the second string to check for anagrams: ").replace(" ", "").lower()
    print("Are anagrams:", are_anagrams(string1, string2))

    # 9. Check if a given string is a palindrome
    def is_palindrome(text):
        text = ''.join(char.lower() for char in text if char.isalpha())
        return text == text[::-1]

    palin_text = input("Enter a string to check if it is a palindrome: ")
    print("Is palindrome:", is_palindrome(palin_text))

    # 10. Check if a substring is present in a given string
    def is_substring_present(text, substring):
        return substring in text

    main_text = input("Enter the main text: ")
    sub_text = input("Enter the substring to check: ")
    print("Is substring present:", is_substring_present(main_text, sub_text))

    # 11. Explore string module
    def explore_string_module():
        print("Lowercase characters:", string.ascii_lowercase)
        print("Uppercase characters:", string.ascii_uppercase)
        print("All characters:", string.ascii_letters)
        print("Digits:", string.digits)
        print("Punctuation symbols:", string.punctuation)
        print("Total number of punctuation symbols:", len(string.punctuation))

    explore_string_module()

if __name__ == "__main__":
    main()

