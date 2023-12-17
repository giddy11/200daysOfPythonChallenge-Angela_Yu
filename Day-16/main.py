from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


andrew = CoffeeMaker()
order = Menu()

order.find_drink("latte")

andrew.report()
andrew.make_coffee(order)
