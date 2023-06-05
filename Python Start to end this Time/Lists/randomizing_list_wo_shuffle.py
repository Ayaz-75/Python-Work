'''
Randomize The elements of List without using builtin shuffle() function.
'''



from numpy import random

new_list = [1, 2, 3, 4, 5, 6, 7]
new_list1 = []
for item in new_list:
    random_choice = random.choice(new_list)
    if random_choice not in new_list1:
        new_list1.append(random_choice)
    
        # print(random_choice)

print(new_list1)