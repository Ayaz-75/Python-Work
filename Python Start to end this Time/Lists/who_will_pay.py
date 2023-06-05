import random
names_string = input("Give me everybody's names, separated by comma: ")
names_list = names_string.split(",")
random_index = random.randint(0, (len(names_list)-1))
who_will_pay = names_list[random_index]
print(f"{who_will_pay} will pay the bill today")
