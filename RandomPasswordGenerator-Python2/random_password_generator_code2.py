import random
import string

def generate_password(length=12):
    symbols = string.punctuation
    digits = string.digits
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase

    all_characters = symbols + digits + lowercase_letters + uppercase_letters
    password = ''.join(random.choice(all_characters) for i in range(length))
    return password

if __name__ == "__main__":
    length = int(input("Enter password length: "))
    if length < 8:
        print("Password length should be at least 8 characters.")
    else:
        password = generate_password(length)
        print("Generated Password:", password)
