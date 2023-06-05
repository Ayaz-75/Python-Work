
def is_divisible(x, y):
    if x % y == 0:
        return True
    else:
        return False


print(is_divisible(6, 3))


# we can also write this function as:
def is_div(x, y):
    return x % y == 0  # this directly returns the boolean


print(is_div(6, 4))


if is_div(6, 4):
    print("X is divisible by Y")

else:
    print("X is not divisible by Y")
