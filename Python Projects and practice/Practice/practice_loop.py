# ------------------- Factorial ---------------------

'''
number = int(input("Enter the number: "))
fact = 1
for i in range(1, number+1):

    fact *= i

print("Factorial of", number, "is: ", fact)

'''

# ------------------- Reverse String -------------------
import random

'''st_input = 'python'
rev = ""
for i in range(len(st_input)-1):
    rev = st_input[::-1]
print(rev)
'''

# ----------------- Reverse Number ----------------------

'''number = 12345

while number > 0:
    sep = number % 10
    print(sep, end="")
    number //= 10
'''

# ------------------ natural numbers from 10 t0 1 ------------------
'''number = 10
while number >= 1:
    print(number, end=" ")

    number -= 1
'''

# ------------------- 7 multiples of 7 -----------------------

'''for i in range(7+1):
    print(i*7, end=" ")
'''

# ------------------- Square of each number in Previous list ----------------------
'''list_1 = [1, 2, -3, 4, -5, 6, 7, -8, 9]
elements = []
for i in range(len(list_1)):
    elements.append(list_1[i]**2)
print(elements)
'''

# -------------------- Negative and positive separate from -------------------------
'''list_1 = [1, 2, -3, 4, -5, 6, 7, -8, 9]
l_1 = []
l_2 = []
for i in range(len(list_1)):
    if list_1[i] > 0:
        l_1.append(list_1[i])

    else:
        l_2.append(list_1[i])
print("Positive:", l_1, "Negative:", l_2)
'''

# ------------------------ Append types of elements to list ---------------------------
'''list_1 = [5, "Python", 45.75]
l_1 = []
for i in range(len(list_1)):
    l_1.append(type(list_1[i]))

print(l_1)
'''

# ------------------------ GREATEST common divisor -----------------------------------
'''x = 35
y = 20

while y > 0:
    x, y = y, x % y

print(x)
'''

# -------------------- Ask user for input until he/she presses q ------------------

'''num = 0
sums = 0

while num != "q":
    st_data = int(num)
    sums += st_data
    num = input("?")

print(sums)
'''
# ------------------- Sum of digits in number ------------------------
'''number = int(input("Enter the number: "))
sum_s = 0
while number > 0:
    sep = number % 10
    sum_s += sep
    number //= 10
print("Sum of digits of number:", sum_s)
'''

# ------------------ Reverse of Digits of a number --------------------
'''number = int(input("Enter the number: "))
sum_s = []
while number > 0:
    sep = number % 10
    sum_s.append(sep)
    print(sep, end="")
    number //= 10
print(sum_s)
'''

# ---------------------------- Prime number ------------------------------------

'''is_prime = True
number = int(input("?: "))
for i in range(2, number):
    if number % i == 0:
        is_prime = False
if is_prime:
    print("it is prime")
else:
    print("it is not prime")'''


names = ["ayaz", "aaqib", "ayoob"]
random_choice = random.choice(names)

user_guess = input("Guess a name: ")

if user_guess == random_choice:
    print(user_guess)
