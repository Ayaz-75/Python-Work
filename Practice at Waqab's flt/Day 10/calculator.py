import art
logo = art
print(logo.logo)


def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2


operations = {"+": add,
              "-": sub,
              "*": mul,
              "/": div,
              }


num1 = int(input("What is the first number: "))
for symbol in operations:
    print(symbol)
operation_symbol = input("Pick any of the operations above: ")
num2 = int(input("What is the second number: "))

result = operations[operation_symbol]
answer = result(num1, num2)
print(f"{num1} {operation_symbol} {num2} = {answer}")

should_end = False

while not should_end:
    if input("Do you want to continue operation on the last number: ") == "y".lower():
        num1 = answer
        operation_symbol = input("Pick another operation: ")
        num3 = int(input("What is another number: "))
        result = operations[operation_symbol]
        new_answer = result(num1, num3)

        print(f"{answer} {operation_symbol} {num3} = {new_answer}")

    else:
        should_end = True
        print(f"Final calculation is: {new_answer}")
        print(f"Good bye!")
