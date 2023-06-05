# Usman Ashraf9:33 AM
wh_1 = {
    "apples": 300,
    "organes": 400,
    "bananas": 500,
}

wh_2 = {
    "mangoes": 100,
    "organes": 300,
    "watermelon": 400
}

wh_3 = {
    "bananas": 200,
    "mangoes": 400,
}

# aggregate_whs() should return something like the following:
# {"apples":300, "mangoes":500, "bananas":700, "oranges": 700, "watermelon":400}

def aggregate_whs(w1, w2,w3):
    # write your code here
    combined_ = [w1,w2,w3]
    new_dict = {}
    count = 0
    for item in combined_:
        if item not in new_dict:
            new_dict[item] = item
            count += 1

        
    for fruits in new_dict:
        print(f"{fruits}: {count}")
    

    
    

aggregate_whs(wh_1, wh_2, wh_3)
