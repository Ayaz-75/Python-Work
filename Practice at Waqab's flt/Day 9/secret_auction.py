print(f"\n\nWelcome to the secret auction game 🙋‍♂️🙋‍♂️🙋‍♂️")




is_game_end = False
new_dictionary = {}

def find_highest_bidder(bids):
    highest_bid = 0
    winner = ""
    for bidder in bids:
        bid_amount = bids[bidder]
        if bid_amount > highest_bid:
            highest_bid = bidder
            winner += bidder[highest_bid]
    print(f"The winner is: {winner} with ${highest_bid}")
while not is_game_end:

    name = input("What is your name ? \n")
    bid = int(input("What's your bid ?\n"))
    others = input("Is there any other bidder in the room ?\n")
    new_dictionary[name] = bid
    if others == "no":
        find_highest_bidder(new_dictionary)
        is_game_end = True

# print(new_dictionary)
