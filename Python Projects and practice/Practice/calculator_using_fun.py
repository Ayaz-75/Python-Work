"""-------------------------Calculator using functions-------------------------"""
print('''
 ______________
|   ________   |                _            _       _                 
|  | Python |  |       ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ ___ 
|  """"""""""  |      / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__/ __|
|  [M|#|C][-]  |     | (_| (_| | | (__| |_| | | (_| | || (_) | |  \__ )
|  [7|8|9][+]  |      \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|  |___/
|  [4|5|6][x]  |
|  [1|2|3][%]  |
|  [.|O|:][=]  |
"--------------"

''')


def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


first_number = float(input("what is first number: "))
operation = input("pick the operation \n+ \n- \n* \n/ \n: ")
second_number = float(input("what is second number: "))
result = 0
if operation == "+":
    result += (add(first_number, second_number))
    print(f"{first_number} {operation} {second_number} =  {result}")
elif operation == "-":
    result += (sub(first_number, second_number))
    print(f"{first_number} {operation} {second_number} =  {result}")
elif operation == "*":
    result += (mul(first_number, second_number))
    print(f"{first_number} {operation} {second_number} =  {result}")
elif operation == "/":
    result += (div(first_number, second_number))
    print(f"{first_number} {operation} {second_number} =  {result}")

final_result = result
should_continue = True
while should_continue:
    ask = input(f"type y co continue calculating with {final_result}: ")

    if ask == "y":
        new_num = int(input("Enter a new number: "))
        next_operation = input("Enter operation: ")
        if next_operation == "+":
            final_result += new_num
            print(final_result)
        elif next_operation == "-":
            final_result -= new_num
            print(final_result)
        elif next_operation == "*":
            final_result *= new_num
            print(final_result)
        elif next_operation == "/":
            final_result /= new_num
            print(final_result)

    else:
        should_continue = False
        print(f"Final result = {final_result}")
