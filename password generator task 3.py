import random

# Prompt user for input
length = int(input("Enter the length of the password: "))
use_letters = int(input("Enter 1 if you want to use letters, 0 otherwise: "))
use_digits = int(input("Enter 1 if you want to use digits, 0 otherwise: "))
use_symbols = int(input("Enter 1 if you want to use symbols, 0 otherwise: "))

# Define character sets
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
symbols = '!@#$%^&*()_+-='

# Create a list of character sets to use
char_sets = []
if use_letters == 1:
    char_sets.append(letters)
if use_digits == 1:
    char_sets.append(digits)
if use_symbols == 1:
    char_sets.append(symbols)

# Generate the password
password = []
for i in range(length):
    # Choose a random character set to use
    char_set = random.choice(char_sets)
    # Choose a random character from the set
    char = random.choice(char_set)
    # Add the character to the password
    password.append(char)

# Shuffle the password to ensure randomness
random.shuffle(password)

# Convert the password list to a string
password = ''.join(password)

# Print the generated password
print("Generated password:", password)
print("Total length:", len(password))
