

def empty_or_not(dic):
    for item in dic:
        if item not in dic:
            return False
        else:
            return True


new_dict = {"A": 1,
            "B": 2}
print(empty_or_not(new_dict))

