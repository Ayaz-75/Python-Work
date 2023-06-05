import random
import art
from game_data import data
print(art.logo)


def format_account(account):
    account_name = account['name']
    account_desc = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_desc} from {account_country}"


def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == 'b'

account_2 = random.choice(data)
score = 0

is_game_over = False
while not is_game_over:
    account_1 = account_2
    account_2 = random.choice(data)

    name_1_followers = account_1['follower_count']
    name_2_followers = account_2['follower_count']

    if account_1 == account_2:
        account_2 = random.choice(data)

    print(f"Compare A: {format_account(account_1)}")
    print(art.vs)
    print(f"Compare B: {format_account(account_2)}")

    guess = input("Who has more followers type 'A' or 'B': ").lower()

    a_follower_count = account_1['follower_count']
    b_follower_count = account_2['follower_count']

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"You are right!!!! Score: {score}")
    else:
        print(f"Sorry you are wrong!!!! Final score is: {score}")
        is_game_over = True

