import random

from art import logo, vs
from game_data import data

print(logo)

def format_account(account):
    account_name = account['name']
    account_disc = account['description']
    account_country = account['country']

    return f"{account_name} {account_disc} {account_country}"


def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"

    else:
        return guess == "b"

        # if guess == "a":
        #     return True
        # else:
        #     return False


score = 0
should_end = False
account_2 = random.choice(data)

while not should_end:


    account_1 = account_2
    account_2 = random.choice(data)
    if account_2 == account_1:
        account_2 = random.choice(data)

    print(f"Compare A: {format_account(account_1)}")
    print(vs)
    print(f"Against B: {format_account(account_2)}")

    # Follower counts of both accounts
    follower_count_1 = account_1['follower_count']
    follower_count_2 = account_2['follower_count']

    # Ask user to guess who has more followers
    guess = input("Who has more followers 'A' or 'B': ").lower()
    is_correct = check_answer(guess, follower_count_1, follower_count_2)



    if is_correct:
        score += 1
        print(f"You are right! current score is: {score}")

    else:
        print(f"Sorry that's wrong answer final score is: {score}")
        should_end = True
