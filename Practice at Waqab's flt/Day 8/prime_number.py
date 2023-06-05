def prime_checker(num):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False


    if is_prime:
        print("Prime number")

    else:
        print("Not a prime")

check = int(input("Enter number: "))
prime_checker(check)

