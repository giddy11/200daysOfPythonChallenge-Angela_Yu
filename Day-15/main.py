from data import resources, MENU

profit = 0


def print_report():
    """User needs to know the available resources"""
    print(f"""
Water: {resources["water"]}ml
Milk: {resources["milk"]}ml
Coffee: {resources["coffee"]}g
Money: ${profit}
""")


def process_coins():
    """This does the conversion of the various coins and returns the dollar conversion"""
    no_of_quarters = float(input("How many quarters: ")) * 0.25
    no_of_dimes = float(input("How many dimes: ")) * 0.10
    no_of_nickels = float(input("How many nickels: ")) * 0.05
    no_of_pennies = float(input("How many pennies: ")) * 0.01

    dollar_conversion = round(no_of_quarters + no_of_dimes + no_of_nickels + no_of_pennies, 2)
    return dollar_conversion


def resource_allocation(order_ingredients):
    """After a resource has be spent, it needs to be updated here"""
    for x in order_ingredients:
        resources[x] -= order_ingredients[x]


def check_resources_sufficiency(order_ingredients):
    """For a user to make purchase, there has to be confirmation of sufficient resources"""
    for x in order_ingredients:
        if order_ingredients[x] > resources[x]:
            print(f"Sorry there is not enough {x}")
            return -1

    return 1


def transaction(money_received, receipt_cost, user_selection):
    """Transaction of the purchase, and if there's change for the user, it is returned to the user"""
    global profit
    if money_received == receipt_cost:
        profit += receipt_cost
        print(f"Here is your {user_selection}, Enjoy!")
    elif money_received > receipt_cost:
        profit += receipt_cost
        balance = round(dollar - receipt_cost, 2)
        print(f"Here is ${balance} in change.\nHere is your {user_selection} 😁, Enjoy!")
    else:
        print(f"Sorry that's not enough money. Money refunded.")


while True:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "report":
        print_report()
    elif user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
        ingredient = MENU[user_choice]
        resource = check_resources_sufficiency(ingredient["ingredients"])
        if resource == 1:
            resource_allocation(ingredient["ingredients"])
            dollar = process_coins()
            menu_cost = MENU[user_choice]["cost"]
            transaction(dollar, menu_cost, user_choice)

    elif user_choice == "x":
        break
