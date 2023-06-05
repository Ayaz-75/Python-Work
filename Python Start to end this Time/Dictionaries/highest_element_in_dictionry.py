

new_dictionary = {}

bidding_is_continue = True

while bidding_is_continue:
    input_name = input("Wat is your name: ")
    input_data = int(input("What is his bid: "))

    new_dictionary[input_name] = input_data
    any_other = input("Is there any other bidder: ")
    if any_other == 'no':
        bidding_is_continue = False
        print(new_dictionary)


def highest_element():
    highest_num = 0
    winner = ""
    for item in new_dictionary:
        if new_dictionary[item] > highest_num:
            highest_num = new_dictionary[item]
            winner = item
    return f"Winner is {winner} at {highest_num}$ pocket money"


print(highest_element())

