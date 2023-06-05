# Write a python program to print the last item in given list
'''x = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
z = [110, 220, 330, 440, 550, 660, 770, 880, 990]
# print("List x: ", x[-1])
# print("List y: ", y[-1])
# print("List z: ", z[-1])
# ---------------------Reverse a list -----------------------
# print(x[::-1])


# --------------------- Difference between 1st and last item of list -------------------------
diff = z[-1] - z[0]
# print("Difference is: ", diff)

sum_s = 0
for i in range(len(x)):
    sum_s += x[i]

# print(sum_s)

# ---------------------- Largest and smallest number in list ----------------------------
number = x[0]
for i in range(len(x)):
    if number > x[i]:
        number = x[i]
print("Highest value in list is: ", number)
'''
# ---------------------- Take list as input ---------------------------
'''a = []
sum_s = 0
for i in range(10):
    a.append(int(input("Enter number: ")))
    sum_s += a[i]
print(a)
print(sum_s)
'''

# ---------------------- find the length of list and square the length of list ------------------------

'''y = ["Ayaz", "Aaqib Ali", "Ayoob", "Zahoor"]
length_of_str = 0
for i in range(len(y)):
    length_of_str += len(y[i])

square = length_of_str ** 2
print("Length of List: ", length_of_str)
print("Square of lengths: ", square)
'''

# ------------------- Fill the list with random numbers --------------------
'''import random

arr = []
for i in range(10):
    arr.append(random.randint(i, 10))
print(arr)
'''

# ----------- Take a number as input and append the reverse if its digits into a new list ------------
'''num = int(input("Enter the number: "))
a = []
while num > 0:
    sep = num % 10
    a.append(sep)
    num //= 10

print(a)
'''
# ----------------------- take a list and print only integers present in it --------------------------
'''x = ["a", 12, "dy", 14.3, 17, 21, "aaq"]
y = []
for i in range(len(x)):
    if type(x[i]) == int:
        print(x[i])
        y.append(x[i])

print(y)
'''
'''
str_sentence = "I love Python for no reason"
new_str = str_sentence.split()
print(new_str)
'''

# --------------------- Return true if the identical letters occur in the string ------------------------
'''user_input = input("Enter numbers: ").split()
sum_s = 0
avg = 0
for i in range(0, len(user_input)):
    user_input[i] = int(user_input[i])
    sum_s += user_input[i]
avg = sum_s / len(user_input)
print(sum_s)
print(avg)'''

# ----------------------- Add Even numbers ------------------------
'''sum_s = 0
for i in range(101):
    if i % 2 == 0:
        sum_s += i
print(sum_s)
'''
# -------------------------------- FizzBuzz Game -------------------------------
'''for i in range(1, 20):

    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")

    if i % 3 == 0:
        print("Fizz")

    elif i % 5 == 0:
        print("Buzz")

    else:
        print(i)
'''

# ----------------------------- Random Password Generator ----------------------------
'''import random
password = []
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
           'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]

how_many_letters = int(input("How many Letters ?: "))

how_many_numbers = int(input("How many numbers ?: "))

how_many_symbols = int(input("How many Symbols ?: "))

let_range = how_many_letters
num_range = how_many_numbers
sym_range = how_many_symbols

for pas in range(let_range):
    password.append(random.choice(letters))

for pas in range(num_range):
    password.append(random.choice(numbers))

for pas in range(sym_range):
    password.append(random.choice(symbols))

random.shuffle(password)

password_string = " ".join(map(str, password))

print(password_string)'''

# ------------------------------ Functions in Python ------------------------------

# ------------------ Function to check if the order is eligible for Shipping ----------------

'''def is_order_eligible():
    criteria = 100
    shopping_bill = int(input("What is your bill sir ?:"))
    if shopping_bill > criteria:
        print("You are eligible for Shipping sir")
    else:
        print("Sorry sir you are not Eligible for Shipping")


is_order_eligible()'''

# ----------------------- Hours to minutes Function Program ---------------------------
'''def hours_to_seconds(hours):
    seconds = hours * 60
    print(f"There are {seconds} seconds in {hours} hours")


hours_to_seconds(5)'''

# ------------------------- Area of triangle ---------------------------

'''def area_of_triangle(base, height):
    area = (base * height) / 2
    return area


input_base = int(input("what is the base of triangle ? "))
input_height = int(input("What is the height of triangle ? "))


print(area_of_triangle(input_base, input_height))'''

# -------------------------- Function to know if number is even or odd ------------------------------

'''def is_number_even_or_odd(num):
    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is odd")


number = int(input("Enter the number to be checked: "))

is_number_even_or_odd(number)
'''

# ---------------------- Exponent Function program ----------------------------

'''
def ex_po(num):
    return num ** 2


input_num = int(input("Enter number: "))
print(ex_po(input_num))
'''

# ---- Program to return True if sum of two numbers is greater than 100 if not then return False


'''def ret_result(num1, num2):
    sum_s = num1 + num2
    if sum_s > 100:
        return True
    else:
        return False


num_1 = int(input("Enter 1st number: "))
num_2 = int(input("Enter 2nd number: "))

print(ret_result(num_1, num_2))'''

# Program to find either number is divisible with 100 or not it gives true if it is divisible false if not


'''def check_divisibility(num):
    if num % 100 == 0:
        return True
    else:
        return False


print(check_divisibility(770))'''

# ---------------program to find the sum of integers given in string form --------------------


'''def return_sum(st_dta):
    tk_str = st_dta.split()
    sum_s = 0
    for i in range(len(tk_str)):
        sum_s += int(tk_str[i])
    return sum_s


input_string = input("Enter the string: ")
print(return_sum(input_string))'''

# --------------- Program to return number if it falls in lower or upper range ---------------------


'''def return_if_falls(num, limit_1, limit_2):
    for num1 in range(limit_1, limit_2):

        if limit_1 < num < limit_2:
            return num

        elif num <= limit_1:
            return limit_1

        elif num >= limit_2:
            return limit_2

        else:
            print("Not a valid number")


user_input = int(input("Enter the number to be checked: "))
print(return_if_falls(user_input, 11, 22))
'''

# -------- Python program to check two numbers can be added subtracted multiplied or Divided ----------
'''def check_operations(num1, num2):
    if num1 + num2 > 0:
        return True
    elif num1 - num2 > 0 or num2 - num1 > 0:
        return True
    elif num1 * num2 > 0 or num2 * num1 > 0:
        return True
    elif num1 / num2 > 0 or num2 / num1 > 0:
        return True

    else:
        return False


first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

print(check_operations(first_number, second_number))'''


# ------------------- Level points challenge program using function ---------------------

'''def collect_all_points():
    total_points = easy_level_points + medium_level_points + hard_level_points
    return total_points


easy_level_points = (int(input("How many times easy level is being played ?:")))*5
medium_level_points = (int(input("How many times easy level is being played ?:")))*10
hard_level_points = (int(input("How many times easy level is being played ?:")))*20

print("Total points after playing the all rounds are: ", collect_all_points())'''

# program to print numbers from 1 to 50 if number is multiple of 3 print not, 5 print but both print not-but


'''def check_multiple():
    for i in range(1, 50):
        if i % 3 == 0 and i % 5 == 0:
            print("NotBut")
        elif i % 3 == 0:
            print("Not")
        elif i % 5 == 0:
            print("But")
        else:
            print(i)


check_multiple()'''

# --------------------- Program to remove indices of the List --------------------

'''def remove_indices():
    list_1.remove(list_1[1])
    return list_1


list_1 = ["Ayaz", "Ayoob", "Aaqib", "Zahoor"]
print(remove_indices())
'''

# ------------ Write a function to return a sorted list -----------------


'''list_1 = [3, 2, 6, 1, 9, 5, 8]
string_ex = ' cfghilmnoprstuy'.split()


def return_sorted_list(list_s):
    list_s.sort(reverse=True)
    return list_1


print(return_sorted_list(list_1))
print(string_ex)
string_ex.sort()'''


# ---------------- function to reverse the words in List ------------------
list_1 = ["Apple", "Ball", "Cat"]
for i in range(len(list_1)):
    list_1[i] = list_1[::i]
    print(list_1[i])
