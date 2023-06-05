

import random

input_string = input("Give me the all name seperated with comma! ").lower()
names_list = input_string.split(",")

random_index = random.randint(1, (len(names_list)-1))
random_name = names_list[random_index]
print(random_name)












# head = 1
# tail = 0

# random_choice = random.randint(0, 1)
# if random_choice == 1:
#     print("Head")

# else:
#     print("Tail")


