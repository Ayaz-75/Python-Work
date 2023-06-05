
def factorial():
    x = 1

    i = 5
    while i > 0:
        x *= i
        i -= 1

    return x


print(f"Factorial is {factorial()}")
