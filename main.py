import random
import string

def generate_passwords(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    passwords = []

    with open("passwords.txt", "w") as file:
        count = 0
        while count < 100000:
            password = ''.join(random.choice(characters) for i in range(length))
            if password not in passwords:
                passwords.append(password)
                file.write(password + "\n")

                count += 1
                if count % 10000 == 0:
                    print(f"{count} pass saved.")

    print("All pass saved.")

#password length 
length = int(input("input pass length: "))

# pass export .txt save
generate_passwords(length)
