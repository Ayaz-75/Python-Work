
def is_prime(num):
    for number in range(2, num):
        if num % number == 0:
            return "Not Prime"

    return "Prime"


print(is_prime(18))

