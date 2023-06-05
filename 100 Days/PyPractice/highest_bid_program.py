should_stop = False
bid_data = {}


def highest_bidder(bidder_record):
    highest_bid = 0
    for bidder in bidder_record:
        bid_amount = bidder_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"winner is {winner}")


while not should_stop:
    name = input("Enter name: ")
    price = float(input("Enter bid price: "))
    bid_data[name] = price
    should_continue = input("are there any other users: ")

    if should_continue == "no":
        should_stop = True
        highest_bidder(bid_data)
    elif should_stop == "yes":
        should_stop = False
