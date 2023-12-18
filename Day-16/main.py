from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


andrew = CoffeeMaker()
order = Menu()
my_cash = MoneyMachine()
menu = MenuItem("nutri", 50, 0, 30, 1.5)

"""Check if te drink is available"""
latte = order.find_drink("latte")
all_items_available = order.get_items()
print(all_items_available)
# print(latte)

"""Check for the cost of each item"""
andrew.report()

"""check if latte drink is sufficient"""
is_latte_sufficient = andrew.is_resource_sufficient(latte)
# print(is_latte_sufficient)


# my_cash.report()
# my_cash.make_payment(latte.cost)
# andrew.make_coffee(latte)
# andrew.report()
