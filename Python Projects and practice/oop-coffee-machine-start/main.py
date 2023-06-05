from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
my_menu = Menu()


is_game_on = True
while is_game_on:
    my_menu.get_items()
    choice = input(f"What would you like? (espresso/latte/cappuccino): ")
    if choice == 'off':
        is_game_on = False

    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()

    else:
        drink = my_menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
