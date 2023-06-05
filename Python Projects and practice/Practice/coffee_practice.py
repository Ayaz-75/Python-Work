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
            "water": 200,
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


def is_resource_sufficient(ordered_ingredients):
    for items in ordered_ingredients:
        if ordered_ingredients[items] >= resources[items]:
            print(f"Sorry not enough {items}")
            return False

        else:
            for item in resources:
                resources[item] -= ordered_ingredients[item]
            return True


def process_coins():
    print(f"Please insert Coins !")
    total = int(input("How many quarters: ")) * 0.25
    total += int(input("How many dimes: ")) * 0.10
    total += int(input("How many nickles: ")) * 0.05
    total += int(input("How many dimes: ")) * 0.01
    if total >= drink['cost']:
        print(f"Here is your '{user_choice}' and here is your {(total - drink['cost']).__round__(2)}$ in change")
        global profit
        profit += drink['cost']
    else:
        print("Sorry not enough money!")


is_game_on = True

while is_game_on:
    user_choice = input(f"“What would you like? (espresso('cost': 2$)/latte('cost': 2.5$)/cappuccino('cost': 3$)): ")
    if user_choice == 'off':
        print(f"Sorry to see u going! have a nice day Goodbye")
        is_game_on = False

    elif user_choice == 'report':
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"Money: {profit}$")

    else:
        drink = MENU[user_choice]

        if is_resource_sufficient(drink['ingredients']):
            process_coins()
