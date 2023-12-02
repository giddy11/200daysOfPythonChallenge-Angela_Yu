import random
from hangman_functions import update_word, display_word, clear
from hangman_words import word_list
from hangman_art import logo, stages

def StartGame():
        trials = 7
        list_of_guessed_letters = []


        print(logo)

        # a random word is picked
        # chosen_word = random.choice(word_list)
        chosen_word = "nige"
        print(chosen_word)
        # get the length of the word
        length_of_word = len(chosen_word)

        # fill it with blanks
        store = []
        for i in range(length_of_word):
            store.append("-")

        blanks = ["-"] * (length_of_word)

        while trials > 0:
            blanked_words = "".join(blanks)
            display_word(blanked_words)

            clear(5)

            if "-" not in blanks:
                print("You win.")
                break
            guess_letter = input("\nGuess a letter: ").lower()

            latest = update_word(chosen_word, blanks, guess_letter, length_of_word)

            if latest == 0:
                print(f"You guessed {guess_letter}, that's not in the word. You lose a life")
                print(stages[trials - 1])
                trials -= 1

            if guess_letter in list_of_guessed_letters:
                 print(f"You've already guessed {guess_letter}")
            
            list_of_guessed_letters.append(guess_letter)
            

            
            if trials == 0:
                 print("You lose")                  

StartGame()