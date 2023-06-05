

new_dictionary = {}
should_continue = True
while should_continue:
    user_name = input("Enter your name: ")
    user_bid = int(input("Enter bidding Price: "))
    new_dictionary[user_name] = user_bid

    ask = input("is there any other bidder: ")
    if ask == "no":
        should_continue = False
        highest_bid = 0
        winner = ""
        for bid in new_dictionary:
            bid_amount = new_dictionary[bid]
            if bid_amount > highest_bid:
                highest_bid = bid_amount
                winner = bid
        print(f"the winner is {winner} with bidding price {highest_bid}$")

