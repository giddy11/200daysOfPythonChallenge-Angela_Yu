from art import logo, goodbye
from functions import Print_Result
import functions

print(logo)

user_continue = "y"
calculate_again = True

while calculate_again:
        
    functions.user_first_input = int(input("What's the first number?: "))
    functions.user_op_choice = input("+ - * /\nPick an operator: ")
    functions.user_second_input = int(input("What's the next number?: "))
    Print_Result()   

    while user_continue == "y":
            user_continue = input(f"Continue calculating with {functions.res}? y/n...").lower()
            if user_continue == "n":
                    break
            user_op_choice = input("+ - * /\nPick an operator: ")
            user_second_input = int(input("What's the next number?: "))
            Print_Result()
    
    user_continue_calculating = input(f"Do you want to switch off the Calculator? y/n...").lower()
    if user_continue_calculating == "y":
           print(goodbye)
           break