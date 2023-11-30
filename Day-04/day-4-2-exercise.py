import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Angela, Ben, Jenny, Michael, Chloe
print(names)
names_length = len(names)
ran_num = random.randint(0, names_length - 1)


# print(f"{names[ran_num]} is going to buy the meal today!")

# With random.choice the code will look like
ran_choice = random.choice(names)
print(f"{ran_choice} is going to buy the meal today!")
