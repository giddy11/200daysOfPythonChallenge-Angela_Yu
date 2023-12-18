from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

turn_on = True
coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()
menu_item = MenuItem("nutri", 50, 0, 30, 1.5)

all_items_available = menu.get_items()

while turn_on:
    choice = input(f"What would you like? {all_items_available}: ").lower()
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        turn_on = False
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
