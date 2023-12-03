from store import bank
from art import logo

def EncodedMessage(user_input, length, n):
    encoded_message = ""
    for i in range(length):
        if user_input[i] in bank:
            position = bank.index(user_input[i])
            desired_position = position + n
            new_letter = bank[desired_position]
            encoded_message += new_letter
        else:
            encoded_message += user_input[i]

    return encoded_message


def DecodedMessage(user_input, length, n):
    decoded_message = ""
    for i in range(length):
        if user_input[i] in bank:
            position = bank.index(user_input[i])
            desired_position = position - n
            new_letter = bank[desired_position]
            decoded_message += new_letter
        else:
            decoded_message += user_input[i]

    return decoded_message

play_again = True

while play_again:
    print(logo)

    user_input = input("Type your message:\n")
    user_choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # in case a user enters a shift that is out of range
    shift %= 134

    length_of_user_input = len(user_input)
    length_of_bank = len(bank)

    if user_choice == "encode":
        res = EncodedMessage(user_input, length_of_user_input, shift)
        print(f"Here's the encoded result: \n{res}")

    elif user_choice == "decode":
            res = DecodedMessage(user_input, length_of_user_input, shift)
            print(f"Here's the decoded result: \n{res}")
    else:
        print("Wrong input")

    play_again = input("Do you want to go again? y/n\n").lower()
    if play_again == "n":
        play_again = False
        print("Goodbye")