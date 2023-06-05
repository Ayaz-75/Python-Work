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


def is_resource_sufficient(drink):
    drink_ingredients = MENU[drink]['ingredients']
    for item in drink_ingredients:
        if drink_ingredients[item] <= resources[item]:
            return True
        else:
            print(f"Sorry not enough resources view report to see the resources")
        return
    return


def process_coins():
    total = 0
    total += int(input("How many quarters: ")) * 0.25
    total += int(input("How many dimes: ")) * 0.10
    total += int(input("How many nickles: ")) * 0.05
    total += int(input("How many pennies: ")) * 0.01
    return total.__round__(2)


def is_transaction_successful():
    global money
    drink = user_order
    total_coins = process_coins()
    if is_resource_sufficient(drink):
        if total_coins >= MENU[drink]['cost']:
            drink_ingredients = MENU[drink]['ingredients']
            for item in drink_ingredients:
                resources[item] -= drink_ingredients[item]

            print(f"Here is your change {(total_coins-MENU[drink]['cost']).__round__(2)} enjoy your {drink} ☕ ")
            money += MENU[drink]['cost']
    return resources




should_off = False

while not should_off:
    user_order = input("What would you like? (espresso/latte/cappuccino):  ").lower()
    if user_order == "off":
        print("Goodbye!")
        should_off = True



    elif user_order == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: {money}$")

    else:
        is_transaction_successful()
