import random
import string

print("\n\n")
print("\t\tRandon Password Generator\n\n")


def generate_password(length):
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example usage
password_length = 12
password = generate_password(password_length)
print("\t  ",f"Generated password: {password}\n\n")
