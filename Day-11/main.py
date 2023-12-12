from art import logo
import random

cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]

def SumList(list):
    sum = 0
    for x in list:
        sum += x
    return sum

user_play_option = input("Do you want to play a game of BlackJack? y/n... ")
if user_play_option == "y":
    print(logo)

    user_cards = [random.choice(cards), random.choice(cards)]
    computer_cards = [random.choice(cards), random.choice(cards)]
    print("Your cards: {}".format(user_cards))
    print("Computer's first card: {}".format(user_cards[0]))

    user_get_card = "y"
    while user_get_card == input("Type y to get another card, type n to pass: "):
        user_cards.append(random.choice(cards))
        print("Your final hand: {}".format(user_cards))
        print("Computer final hand: {}".format(computer_cards))

    user_sum = SumList(user_cards)
    print(user_sum)



    # if user_get_card == "y":
    #     user_cards.append(random.choice(cards))
    #     print("Your final hand: {}".format(user_cards))
    #     print("Computer final hand: {}".format(computer_cards))

    #     user_sum = SumList(user_cards)
    #     print(user_sum)
