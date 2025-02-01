import string
import random


def random_password(length):
    if length < 4:
        raise ValueError("Password minimum length 4 ")

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    characters = string.punctuation

    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(characters)
    ]
    print(password)
    all_characters = lowercase + uppercase + digits + characters
    password += random.choice(all_characters)
    print(password)
    random.shuffle(password)
    print(password)
    return "".join(password)


if __name__ == "__main__":
    while True:
        try:
            num = int(input("Please enter number how long you need your password:").strip())
            passkeys = random_password(num)
            print(f"You password is {passkeys}")
            break
        except ValueError as e:
            print("An error occurred", e)
