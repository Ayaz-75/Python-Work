# ------------------------- Replace one character with an other -----------------------
phrase = "i am a python developer"
rep_phrase = phrase.replace("a", "x")
print(rep_phrase)

# ------------------------- Cups bought --------------------------------
'''cups_in_weekdays = 6
cups_on_weekend = 1
cups_in_week = cups_in_weekdays + cups_on_weekend
cups_in_month = cups_in_week * 4
print("total cups in month: ", cups_in_month)
free_cups_in_month = cups_on_weekend * 4
print("Free cups in a month: ", free_cups_in_month)
'''


# only integers from list
'''def choose_only_integers(x):
    return [i for i in x if type(i) == int]


print(choose_only_integers([1, 'so', 2, 'too', 3, 'but', 4, 'soon', 5, 'every', 6, 'non', 7, 'right']))
'''
# ------------------------- program to print the adverbs of adjectives ---------------------------
'''list_1 = ["strong", "cute"]


for elements in list_1:
    print(elements+"ly")'''


# -------------------------- Program to print the numbers with additive inverse --------------------------------

'''print("Number", "Additive inverse")
for number in range(1, 20):
    if number + -number == 0:
        print(number, "      ", -number)
    else:
        pass
'''

# --------------- Take numbers and return their cubes ------------------
# def cubes_of_nums(num1, num2, num3):
'''sum_of_cubes = 0

for i in range(3):
    input_num = int(input("? "))
    cubes = input_num ** 3
    sum_of_cubes += cubes

print(sum_of_cubes)
'''

'''sum_of_cubes = 0
new_list = []
for i in range(3):
    input_num = int(input("? "))
    new_list.append(input_num)
    sum_of_cubes += new_list[i]**3
print(new_list)
print(sum_of_cubes)'''











