# welcome to the prime number checker

def prime_checker(number):
    for i in range(2, number):
        if number % i == 0:
            return "not prime"
        else:
            return "prime"


num = int(input("Enter number: "))
print(prime_checker(number=num))
