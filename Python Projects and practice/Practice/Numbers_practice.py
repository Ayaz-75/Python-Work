# ---------------- Armstrong Number ------------------

number = int(input("Enter the number to be checked: "))
num_store = number
cubes = 0
while number > 0:
    a = number % 10
    number //= 10

    cubes += a ** 3

if cubes == num_store:
    print(num_store, "is an armstrong number")
else:
    print(num_store, "is not an armstrong number")


