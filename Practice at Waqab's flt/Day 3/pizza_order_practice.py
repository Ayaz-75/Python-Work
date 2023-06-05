print("\n\n----------------------Welcome to the pizza deliveries--------------------------")

size = input("What size pizza do you want: S, M, L\n").lower()
add_pepperoni = input("Do you want pepperoni: Y / N\n").lower()
extra_cheese = input("Do you want extra cheese: Y / N\n").lower()

total_bill = 0

if size == "s":
    total_bill += 15
elif size == "m":
    total_bill += 20
elif size == "l":
    total_bill += 25

if add_pepperoni == "y":
    if size == 's':
        total_bill += 2
    else:
        total_bill += 3


if extra_cheese == "y":
    total_bill += 1


print(f"Your total bill is: {total_bill}")


# small = 15
# medium = 20
# large = 25
#
#
#
# if size == "s":
#     if add_pepperoni == 'y':
#         if extra_cheese == 'y':
#             total_bill = small + 2 + 1
#             print(f"Your bill is: {total_bill}")
#     else:
#         total_bill = small
#         print(f"Your bill is: {total_bill}")
#
# if size == "m":
#     if add_pepperoni == 'y':
#         if extra_cheese == 'y':
#             total_bill = medium + 2 + 1
#             print(f"Your bill is {total_bill}")
#     else:
#         total_bill = medium
#         print(f"Your bill is: {total_bill}")
#
#
# if size == "l":
#     if add_pepperoni == 'y':
#         if extra_cheese == 'y':
#             total_bill = large + 2 + 1
#             print(f'Your bill is: {total_bill}')
#     else:
#         total_bill = large
#         print(f"Your bill is: {total_bill}")
