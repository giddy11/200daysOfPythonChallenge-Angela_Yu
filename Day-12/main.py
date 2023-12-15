from art import logo, goodbye
from random import randint

attempts = 0
computer = 0
guess = 0
play_again = "y"
word_choice = ""

def CheckNumber(guess):
    global computer
    if guess < computer and attempts != 1:
        print("Too Low\nGuess again")
        return 0
    elif guess > computer and attempts != 1:
        print("Too High\nGuess again")
        return 0
    elif guess == computer:
        print(f"You got it!! The answer is {guess}")
        return 1
    
def SetDifficulty():
    global word_choice, attempts
    word_choice = input("""
I'm thinking of a number between 1 and 100.
Choose a difficulty.
Type 'easy' or 'hard' : """).lower()

    if word_choice == "easy":
        attempts = 10
    elif word_choice == "hard":
        attempts = 5



def playGame():
    print(logo)
    global guess, computer, attempts, play_again
    computer = randint(1,100)
    print(computer)
    SetDifficulty()

    while attempts != 0:

        guess = int(input(f"""
    You have {attempts} attempts remaining to guess the number.
    Make a guess: """))

        res = CheckNumber(guess)
        if res == 1:
            break    
            
        attempts -= 1

    if attempts == 0:
        print("You've ran out of guesses, you lose.")

    play_again = input("Do you want to play again? y/n...")

while play_again == "y":
    playGame()

print(goodbye)