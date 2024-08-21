import os
import random
import math
from collections import Counter

def string_operations():
    print("\n--- String Operations ---")
    
    # 1. Find the length of the string
    s = "example"
    length = len(s)
    print(f"1. Length of the string: {length}")

    # 2. Slice the string as per your choice
    sliced = s[2:5]  # Example slice from index 2 to 4
    print(f"2. Sliced string: {sliced}")

    # 3. Concatenate two strings
    s1 = "Hello"
    s2 = "World"
    concatenated = s1 + " " + s2
    print(f"3. Concatenated string: {concatenated}")

    # 4. Convert into lowercase and uppercase
    s = "HeLLo WoRLD"
    lower_case = s.lower()
    upper_case = s.upper()
    print(f"4. Lowercase: {lower_case}")
    print(f"   Uppercase: {upper_case}")

    # 5. Convert uppercase into lowercase
    s = "HELLO"
    converted = s.lower()
    print(f"5. Converted to lowercase: {converted}")

    # 6. Convert the character into Unicode (ASCII values)
    char = 'A'
    unicode_value = ord(char)
    print(f"6. Unicode (ASCII) value of '{char}': {unicode_value}")

    # 7. Convert Unicode (ASCII values) into character
    unicode_value = 65
    char = chr(unicode_value)
    print(f"7. Character for Unicode (ASCII) value {unicode_value}: {char}")

    # 8. Check whether the given "substring" exists in the string
    s = "hello world"
    substring = "world"
    exists = substring in s
    print(f"8. Substring '{substring}' exists in the string: {exists}")

    # 9. Replace the character 'k' with 'h'
    s = "kook"
    replaced = s.replace('k', 'h')
    print(f"9. String after replacing 'k' with 'h': {replaced}")

    # 10. Pad the string with "x" at the end
    s = "hello"
    padded = s.ljust(10, 'x')
    print(f"10. Padded string: {padded}")

    # 11. Remove leading and trailing whitespace or specified characters from the string
    s = "   hello   "
    trimmed = s.strip()
    print(f"11. String after stripping whitespace: '{trimmed}'")

    s = "###hello###"
    trimmed = s.strip('#')
    print(f"    String after stripping '#': '{trimmed}'")

    # 12. Split the given string into groups of five characters
    s = "abcdefghijklmnopqrstuvwxy"
    split_strings = [s[i:i+5] for i in range(0, len(s), 5)]
    print(f"12. String split into groups of 5: {split_strings}")

    # 13. Count the total number of words
    s = "This is an example sentence."
    word_count = len(s.split())
    print(f"13. Total number of words: {word_count}")

    # 14. Find the frequency of each character in the string
    s = "hello"
    frequency = Counter(s)
    print(f"14. Character frequency: {frequency}")

def file_operations():
    print("\n--- File Operations ---")

    # 15. Get the file name from the user
    file_name = input("Enter the file name: ")

    # 16. Check if the file exists or not
    exists = os.path.isfile(file_name)
    print("16. File exists" if exists else "    File does not exist")

    if exists:
        # 17. Read the contents from the file
        with open(file_name, 'r') as file:
            content = file.read()
        print("17. File content:")
        print(content)

        # 18. Reverse the contents from the file
        reversed_content = content[::-1]
        print("18. Reversed content:")
        print(reversed_content)

        # 19. Write into the file
        with open(file_name, 'a') as file:
            file.write("\nAppended text.")
        print("19. Text appended to file.")

def math_operations():
    print("\n--- Math Operations ---")

    # 20. Convert Frequency into percentage
    s = "example string for frequency"
    frequency = Counter(s)
    total_chars = len(s)
    percentages = {char: (count / total_chars) * 100 for char, count in frequency.items()}
    print(f"20. Character frequencies as percentages: {percentages}")

    # 21. Perform modular arithmetic operation
    a = 10
    b = 3
    modular_result = a % b
    print(f"21. Modular arithmetic result of {a} % {b}: {modular_result}")

    # 22. Find the prime numbers
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def prime_numbers_in_range(start, end):
        return [num for num in range(start, end + 1) if is_prime(num)]

    # Check if a given number is prime
    number = 29
    print(f"22. {number} is prime: {is_prime(number)}")

    # Print prime numbers within a range
    start = 10
    end = 50
    print(f"    Prime numbers between {start} and {end}: {prime_numbers_in_range(start, end)}")

    # 23. Check if the given two numbers are co-prime
    def are_coprime(x, y):
        return math.gcd(x, y) == 1

    num1 = 15
    num2 = 28
    print(f"23. Numbers {num1} and {num2} are co-prime: {are_coprime(num1, num2)}")

    # 24. Find the factors for the given number
    def find_factors(n):
        factors = [i for i in range(1, n + 1) if n % i == 0]
        return factors

    number = 36
    print(f"24. Factors of {number}: {find_factors(number)}")

    # 25. Generate 10 random numbers
    random_numbers = [random.randint(1, 100) for _ in range(10)]
    print(f"25. 10 random numbers: {random_numbers}")

if __name__ == "__main__":
    string_operations()
    file_operations()
    math_operations()

