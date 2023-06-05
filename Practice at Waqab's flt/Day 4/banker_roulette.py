import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
random_index = random.randint(0, len(names)-1)
# print(random_index)

who_will_pay = names[random_index]

print(f"{who_will_pay} will pay the bill today")
