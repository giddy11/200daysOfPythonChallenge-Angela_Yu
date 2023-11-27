position = input('''
Welcome to Treasure Island.
Your mission is to find the treasure.
You're at a cross road. Where do you want to go? Type "left" or "right"
''')

if (position == "left"):
    decision = input('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim to swim across.\n')

    if (decision == "wait"):
        color = input('You arrived at the island unarmed. There is a house with 3 doors. One red, one yellow and one blue. which color do you choose?\n')

        if (color == "red"):
            print("It's a room full of fire. Game Over.")