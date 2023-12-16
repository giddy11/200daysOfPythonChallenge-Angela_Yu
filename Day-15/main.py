from data import resources, MENU, profit

money = 0
water_resource = resources["water"]
milk_resource = resources["milk"]
coffee_resource = resources["coffee"]


def print_report():
    print(f"""
Water: {water_resource}ml
Milk: {milk_resource}ml
Coffee: {coffee_resource}g
Money: ${profit}
""")


def process_coins():
    no_of_quarters = float(input("How many quarters: ")) * 0.25
    no_of_dimes = float(input("How many dimes: ")) * 0.10
    no_of_nickels = float(input("How many nickels: ")) * 0.05
    no_of_pennies = float(input("How many pennies: ")) * 0.01

    dollar_conversion = round(no_of_quarters + no_of_dimes + no_of_nickels + no_of_pennies, 2)
    return dollar_conversion


def check_resources_sufficiency(tea_type):
    global  water_resource, milk_resource, coffee_resource
    tea_type_water = MENU[tea_type]["ingredients"]["water"]
    tea_type_milk = MENU[tea_type]["ingredients"]["milk"]
    tea_type_coffee = MENU[tea_type]["ingredients"]["coffee"]

    if water_resource >= tea_type_water and milk_resource >= tea_type_milk and coffee_resource >= tea_type_coffee:
        water_resource -= tea_type_water
        milk_resource -= tea_type_milk
        coffee_resource -= tea_type_coffee
        return 1
    else:
        return -1


while True:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "report":
        print_report()
    elif user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
        resource = check_resources_sufficiency(user_choice)
        if resource == 1:
            dollar = process_coins()
            if dollar == MENU[user_choice]["cost"]:
                profit += MENU[user_choice]["cost"]
                print(f"Here is your {user_choice}, Enjoy!")
            elif dollar > MENU[user_choice]["cost"]:
                profit += MENU[user_choice]["cost"]
                balance = dollar - MENU[user_choice]["cost"]
                print(f"Here is ${balance} in change.\nHere is your {user_choice} 😁, Enjoy!")
            else:
                print(f"Sorry that's not enough money. Money refunded.")
        else:
            print("Sorry there is not enough resource")
    elif user_choice == "x":
        break
