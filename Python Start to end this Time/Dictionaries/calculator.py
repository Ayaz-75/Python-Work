
print('''
 _____________________
|  _________________  |
| |    PYTHONISTA   | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________| ''')


# Addition of two numbers
def ad(n1, n2):
    return n1 + n2


# subtraction
def sub(n1, n2):
    return n1 - n2


# multiplication
def mul(n1, n2):
    return n1 * n2


# division
def div(n1, n2):
    return n1 / n2


operations = {

    "+": ad,
    "-": sub,
    "*": mul,
    "/": div

}


def calculator():
    should_continue = True

    num1 = float(input("Enter first number: "))
    for item in operations:
        print(item)

    while should_continue:
        operator = input("Pick the operator: ")
        num2 = float(input("Enter second number: "))

        calculation = operations[operator]
        answer = calculation(num1, num2)
        print(f"{num1} {operator} {num2} = {answer}")

        again = input("Do you want to continue operation on result: ")

        if again == "yes":
            num1 = answer

        else:
            should_continue = False
            print(f"{answer} is final result \nGood bye have a nice day!")


calculator()
