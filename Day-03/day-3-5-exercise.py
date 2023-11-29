# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
name1 = "Kanye West"
name2 = "Kim Kardashian"
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
compareT = (name1 + name2).lower().count("t")
compareR = (name1 + name2).lower().count("r")
compareU = (name1 + name2).lower().count("u")
compareE = (name1 + name2).lower().count("e")

compareL = (name1 + name2).lower().count("l")
compareO = (name1 + name2).lower().count("o")
compareV = (name1 + name2).lower().count("v")
compare_E = (name1 + name2).lower().count("e")

totalTrue = compareT + compareR + compareU + compareE
totalLove = compareL + compareO + compareV + compare_E

love_score = int(f"{totalTrue}{totalLove}")

if (love_score < 10 or love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40 and love_score <= 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")