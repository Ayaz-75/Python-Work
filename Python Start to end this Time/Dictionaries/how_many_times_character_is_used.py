

def is_used(new_string):

    new_dictionary = {}

    for char in new_string:
        if char not in new_dictionary:
            new_dictionary[char] = 1

        else:
            new_dictionary[char] += 1

    return new_dictionary


input_string = input("Enter your string:")
print(is_used(input_string))
