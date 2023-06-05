

# counts = {}
# 
# while len(counts) < 5:
#     user_input = input("Enter string: ")
#     if user_input not in counts:
#         counts[user_input] = 1
# 
#     else:
#         counts[user_input] += 1
# 
# 
# 
# print(counts)


'''
Exercise 136: Reverse Lookup

Write a function named ```reverseLookup``` that finds all of the ```keys in a dictionary```
that ```map``` to a specific value. The function will take the dictionary and the value to
search for as its only parameters. It will return a (possibly empty) list of keys from
the dictionary that map to the provided value.

Include a main program that demonstrates the reverseLookup function as part
of your solution to this exercise. Your program should create a dictionary and then
show that the reverseLookup function works correctly when it returns multiple
keys, a single key, and no keys. Ensure that your main program only runs when
the file containing your solution to this exercise has not been imported into another
program.

'''

new_dictionary = {"A": 1,
                  "B": 2,
                  "C": 2,
                  "D": 2,
                  "E":1}

def reverseLookup(data, value):
    keys = []
    for key in data:
        if data[key] == value:
            keys.append(key)

    return keys



print(reverseLookup(new_dictionary, 1))
