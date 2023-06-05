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

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry not enough {item}")
            return False

        else:
            return True

def process_coins():
    print(f"insert coins...!🤞")
    total = int(input("How many quarters: ")) * 0.25
    total += int(input("How many dimes: ")) * 0.1
    total += int(input("How many nickles: ")) * 0.05
    total += int(input("How many pennies: ")) * 0.01

    return total


def transaction_successful(received, cost_of_drink):
    if received >= cost_of_drink:
        global profit
        profit += cost_of_drink
        change = received - cost_of_drink
        print(f"Here is your change {change.__round__(2)}$")

        return True
    else:
        print("Sorry insufficient money....!!!!!!!!!!")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]

    print(f"Here is your {drink_name} ☕ enjoy!")



should_end = False

while not should_end:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        print("Good bye........👋👋👋👋👋👋👋")
        should_end = True

    elif choice == 'report':
        print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: "
              f"{profit}$")

    else:
        drink = MENU[choice]
        drink_cost = drink['cost']
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
            if transaction_successful(payment, drink_cost):
                make_coffee(choice, drink['ingredients'])
