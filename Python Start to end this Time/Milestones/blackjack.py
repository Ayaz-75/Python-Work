import random

print(" ------------------ Welcome to the blackjack Game --------------------")
print('''
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_|
                       _/ |                
                      |__/                 
''')

# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


user_card = []
computer_card = []

for _ in range(2):
    user_card.append(deal_card())
    computer_card.append(deal_card())


def calculate_score(cards):
    return sum(cards)
