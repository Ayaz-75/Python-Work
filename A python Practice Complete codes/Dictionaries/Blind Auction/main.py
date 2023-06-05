from art import logo
print(logo)
print("Welcome to the Blind auction game")
print()

bids = {}


should_ask = True

while should_ask:
    
    your_name = input("Enter your name: \n").title()
    your_bid = int(input("Enter your bidding Price: \n"))

    bids[your_name] = your_bid
    is_other_bidder = input("is there any other bidder ?\n")

    if is_other_bidder == "no":
        should_ask = False


print(bids)

winner = ""
highest_bid = 0
for bidder in bids:
    bid = bids[bidder]
    if bid > highest_bid:
        highest_bid = bid
        winner = bidder
    

print(f"Highest bidder is {bidder} With bidding price: ${highest_bid}")
