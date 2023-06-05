from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

is_on = True
while is_on:
    options = menu.get_items()
    user_order = input(f"What would you like? ({options}): ").lower()
    if user_order == "off":
        print("Good bye.!")
        is_on = False
    elif user_order == "report":
        coffee_maker.report()
        money_machine.report()

    else:
        drink = menu.find_drink(user_order)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
