import random
import string
print("=== Password Generator ===")
length = input("Enter password length: ")
if length.isdigit() and int(length) > 0:
    length = int(length)
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for _ in range(length):
        password = password + random.choice(chars)
    print("Your new password is:", password)
else:
    print("Please enter a valid number")
