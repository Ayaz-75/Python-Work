MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0


def is_resource_sufficient(order_ingredients):
    """This function will check either resources are sufficient or not"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry not enough {item}")
            return False
        else:
            return True


def process_coins():
    """This function will process coins"""
    total = 0
    total += float(input("How many quarters: ")) * 0.25
    total += float(input("How many Dimes: ")) * 0.10
    total += float(input("How many Nickels: ")) * 0.05
    total += float(input("How many Pennies: ")) * 0.01
    return round(total, 2)


def is_transaction_successful(money_received, drink_cost):
    """This function will check either transaction is completed or not"""
    if money_received >= drink_cost:
        global money
        money += drink_cost
        if money_received > drink_cost:
            print(f"Here is your change: ${round(money_received - drink_cost, 2)}")
        return True
    else:
        print("Sorry not enough money! Money refunded")


def make_coffee(drink_name, order_ingredients):
    """This function will make coffee and detect the ingredients from resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Enjoy your {drink_name} ☕")


should_continue = True

while should_continue:
    user_order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_order == 'off':
        print("Have a good day! Bye")
        should_continue = False

    elif user_order == 'report':
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\n"
              f"Coffee: {resources['coffee']}g\nMoney: ${money}")

    else:
        order = MENU[user_order]
        if is_resource_sufficient(order['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, order['cost']):
                make_coffee(user_order, order['ingredients'])
