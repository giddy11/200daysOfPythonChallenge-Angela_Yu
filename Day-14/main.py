from random import randint
from art import logo, vs
from game_data import data
import os

is_answer_correct = True
compareA = 0
compareB = 0
current_score = 0


def clear():
    os.system('cls')


def get_both_compare_values():
    global compareA, compareB
    while compareA == compareB:
        compareA = randint(0, 49)
        compareB = randint(0, 49)
        # below for testing
        # compareA = 3
        # compareB = 4


def check_followers():
    global compareA, compareB
    if data[compareA]["follower_count"] >= data[compareB]["follower_count"]:
        return "a"
    else:
        return "b"


while is_answer_correct:
    print(logo)
    get_both_compare_values()
    print(f"Compare A: {data[compareA]["name"]}, a {data[compareA]["description"]}, from {data[compareA]["country"]}.")
    print(vs)
    print(f"Compare B: {data[compareB]["name"]}, a {data[compareB]["description"]}, from {data[compareB]["country"]}.")

    compareOptions = input("Who has more followers? Type 'A' or 'B': ").lower()

    if compareOptions == check_followers():
        current_score += 1
        clear()
        print(f"You're right! Current Score: {current_score}")
    else:
        clear()
        print(logo)
        is_answer_correct = False
        print(f"Sorry, that's wrong. Final Score: {current_score}")
