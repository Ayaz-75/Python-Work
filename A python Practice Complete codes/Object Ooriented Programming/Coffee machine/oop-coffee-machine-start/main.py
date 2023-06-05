from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

user_input = input("What would you like? (espresso/latte/cappuccino):  ").lower()
if user_input == "off":
    exit()

elif user_input == "report":
    coffee_maker.report()

else:
    coffee_maker.is_resource_sufficient(menu.find_drink(user_input))
    