from art import logo
import random
import os, time

cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]
user_at_fault = 0
computer_at_fault = 0
user_play_option = "y"

def clear(): 
    os.system('clear')

def SumList(list):
    sum = 0
    check_for_11 = 0
    for x in list:
        sum += x
        if x == 11:
            check_for_11 = 11
            print(check_for_11)
    return sum

while user_play_option == input("Do you want to play a game of BlackJack? y/n... "):
    clear()
    print(logo)

    user_cards = [random.choice(cards), random.choice(cards)]
    computer_cards = [random.choice(cards)]
    print("Your cards: {}".format(user_cards))
    print("Computer's first card: {}".format(user_cards[0]))

    user_get_card = "y"
    user_sum = 0
    while user_get_card == input("Type y to get another card, type n to pass: ") and user_sum <= 21:
        user_cards.append(random.choice(cards))
        print("Your cards: {}".format(user_cards))
        user_sum = SumList(user_cards)
        if user_sum > 21:
            user_at_fault = 1
            break
    user_sum = SumList(user_cards)

    # user_sum = 15
    


    computer_sum = 0
    while computer_sum < user_sum and user_at_fault == 0:
        computer_cards.append(random.choice(cards))
        print("Computer's cards: {}".format(computer_cards))
        computer_sum = SumList(computer_cards)
        if computer_sum > 21:
            computer_at_fault = 1
            break

    computer_sum = SumList(computer_cards)

    # computer_at_fault = 1
    # computer_sum = 15
    
    print("Your final hand: {}".format(user_cards))
    print("Computer final hand: {}".format(computer_cards))

    if user_sum == computer_sum:
        print("Draw")
    elif (user_sum > computer_sum or computer_at_fault == 1) and (user_sum <= 21 and user_at_fault == 0):
        print("You win")
    elif computer_sum > user_sum or computer_sum <= 21:
        print("Computer wins")