
def prime_checker(num):
    is_prime = True
    for number in range(2, num):
        if num % number == 0:
            is_prime = False

    if is_prime:
        print(f"{num} is prime")

    else:
        print(f"{num} is not prime")


enter_number = int(input("Enter the number to be checked: "))
prime_checker(enter_number)
