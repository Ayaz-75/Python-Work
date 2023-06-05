MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 100,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5
    },
    "capuccino": {
        "ingredients": {
            "water": 250,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 3
    },

}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(ordered_drink):
    for item in ordered_drink:
        if ordered_drink[item] >= resources[item]:
            print(f"sorry not sufficient {item}")
            return False
        else:
            resources[item] -= ordered_drink[item]
    return True


def insert_coin():
    print(f"Insert coins !")
    total = int(input("How many quarters ? ")) * 0.25
    total += int(input("How many dimes ? ")) * 0.10
    total += int(input("How many nickels ? ")) * 0.05
    total += int(input("How many pennies ? ")) * 0.01

    if total > drink['cost']:
        print(f"here is your {user_choice} and here is your {(total - drink['cost']).__round__(2)}$ enjoy")
        global profit
        profit += drink['cost']

    else:
        print(f"sorry not enough money money refunded")


is_machine_on = True
while is_machine_on:
    user_choice = input("What would you like ? Espresso/Latte/capuccino: ").lower()
    if user_choice == "off":
        print(f"Goodbye Sir have a nice day!")
        is_machine_on = False

    elif user_choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Money: {profit}$")

    else:
        drink = MENU[user_choice]
        if is_resource_sufficient(drink['ingredients']):
            insert_coin()
