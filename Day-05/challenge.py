print("Welcome to the PyPassword Generator!")

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password_list = []

no_of_letters = int(input("How many letters would you like in your password?\n"))
no_of_symbols = int(input("How many symbols would you like?\n"))
no_of_nos = int(input("How many numbers would you like?\n"))

#get the random selection for letters
for letter in range(no_of_letters):
    password_list.append(random.choice(letters))

#get the random selection for numbers
for number in range(no_of_nos):
    password_list.append(random.choice(numbers))

#get the random selection for symbols
for symbol in range(no_of_symbols):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

new_password = "".join(password_list)
print(f"Here is your password: {new_password}")