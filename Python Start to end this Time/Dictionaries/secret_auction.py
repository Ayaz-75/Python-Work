
print("Welcome to the Secret Auction")

bidding_finished = False
new_dictionary = {}


def highest_bidder(bid_r):
    highest_bid = 0
    winner = ''
    for bidder in bid_r:
        if bid_r[bidder] > highest_bid:
            highest_bid = bid_r[bidder]
            winner = bidder

    print(f"Winner is {winner} with bidding price {bid_input}$")


while not bidding_finished:
    name_input = input("Who is bidding: ")
    bid_input = float(input("What is your bid: "))
    new_dictionary[name_input] = bid_input
    any_other_bidder = input("is there any other bidder: ")
    if any_other_bidder == 'no':
        bidding_finished = True
        highest_bidder(new_dictionary)

    elif any_other_bidder == 'yes':
        continue
