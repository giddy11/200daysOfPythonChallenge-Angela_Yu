from art import logo, clear

print(logo)
print("Welcome to the secret auction program.")
my_dict = {}



def add_new_person(name, bid_amount):
    my_dict[name] = bid_amount

play_again = True

while play_again:
    name = input("What is your name?: ")
    bid_amount = int(input("What's your bid?: $"))
    add_new_person(name, bid_amount)

    print(my_dict)

    other_bidders = input("Are there any other bidders? Type y/n...").lower()

    if other_bidders == "n":
        break;

    clear()

max_value = max(my_dict.values())
max_key = max(my_dict, key=my_dict.get)

print(f"The winner is {max_key} with a bid of ${max_value}.")