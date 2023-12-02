import os, time


def display_word(blanks):
    print((blanks))

count = 0

def update_word(chosen_word, blanks, guess_letter, length):
    # length = len(chosen_word)
    global count
    count = 0

    for i in range(length):
        if guess_letter == chosen_word[i]:
            blanks[i] = guess_letter
            count = 1

        if count == 1 and i == (length - 1):
            return 1
        if count != 1 and i == (length - 1):
            return 0
        
def clear(seconds = 0): 
    time.sleep(seconds)
    os.system('clear')