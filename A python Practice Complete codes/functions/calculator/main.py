from art import logo
print(logo)
print()

# addition Function
def add(n1, n2):
    return n1 + n2


# Subtraction Function
def sub(n1, n2):
    return n1 - n2


# multiplication Function
def mul(n1, n2):
    return n1 * n2


# Division Function
def div(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/":div,
}


def calculator():

    num1 = float(input("Enter the first number: "))
    for oper in operations:
        print(oper)
    operation_choice = input("Choose the operation: ")
    num2 = float(input("Enter the second number: "))

    calculation_function = operations[operation_choice]
    answer = calculation_function(num1, num2)

    print(f"{num1} {operation_choice} {num2} = {answer}")


    should_continue = input("Do you want to perform operation on result ? ").lower()
    should_end = False
    while not should_end:
        if should_continue == "yes":
            for oper in operations:
                print(oper)
            operation_choice = input("Choose the operation: ")
            new_number = float(input("Enter new number: "))

            answer_2 = calculation_function(answer, new_number)

            print(f"{answer} {operation_choice} {new_number} = {answer_2}")
        elif should_continue == "no":
            should_end = True
        else:
            return "Invalid operation"

calculator()
















#     result = 0
#     if operation_choice == "+":
#         add = operations["+"]
#         result = add(num1, num2)
#         print(f"{num1} {operation_choice} {num2} = {result}")

#     elif operation_choice == "+":
#         sub = operations["-"]
#         result = sub(num1, num2)
#         print(f"{num1} {operation_choice} {num2} = {result}")

#     elif operation_choice == "*":
#         mul = operations["*"]
#         result = mul(num1, num2)
#         print(f"{num1} {operation_choice} {num2} = {result}")

#     elif operation_choice == "/":
#         div = operations["/"]
#         result = div(num1, num2)
#         print(f"{num1} {operation_choice} {num2} = {result}")

#     else:
#         print("Invalid operation!")


# calculator()


# shoul_continue = input("Do you want to continue calculation with result: ")
# if shoul_continue == "yes":
#     new_number = float(input("Enter new number to perform calculation on: "))
#     for oper in operations:
#         print(oper)
#     operation_choice = input("Choose the operation: ")



    


# multiply = operations["*"]
# print(multiply(5, 6))
# addition = add(5, 6)
# subtraction = sub(5, 6)
# multiplication = mul(5, 6)
# division = div(5, 6)

# print(addition)
# print(subtraction)
# print(multiplication)
# print(division)
