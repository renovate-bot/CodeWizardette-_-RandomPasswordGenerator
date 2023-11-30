import random
import string

def generate_passwords(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    passwords = set()

    with open("passwords.txt", "w") as file:
        count = 0
        while count < 100000:
            password = ''.join(random.choice(characters) for i in range(length))
            if password not in passwords:
                passwords.add(password)
                file.write(password + "\n")

                count += 1
                if count % 10000 == 0:
                    print(f"{count} pass saved.")

    print("All pass saved.")

length = int(input("input pass length: "))

generate_passwords(length)
