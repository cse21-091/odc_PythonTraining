import random

# Lists of possible characters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Group12 Password Generator!")

while True:
    num_passwords = int(input("How many passwords would you like to generate?\n"))
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input("How many symbols would you like?\n"))
    nr_numbers = int(input("How many numbers would you like?\n"))

    total_chars = nr_letters + nr_symbols + nr_numbers

    # Check if the total number of characters is within the desired range
    if total_chars < 8 or total_chars > 16:
        print("The total number of characters (letters + symbols + numbers) must be between 8 and 16. Please choose again.")
    else:
        break

for _ in range(num_passwords):
    pwd = []

    # Generate random letters
    for char in range(1, nr_letters + 1):
        pwd += random.choice(letters)

    # Generate random numbers
    for char in range(1, nr_numbers + 1):
        pwd.append(random.choice(numbers))

    # Generate random symbols
    for char in range(1, nr_symbols + 1):
        pwd += random.choice(symbols)

    # Shuffle the characters randomly
    random.shuffle(pwd)

    password = ""

    # Convert the list of characters into a string
    for char in pwd:
        password += char

    # Print the generated password
    print(password)
