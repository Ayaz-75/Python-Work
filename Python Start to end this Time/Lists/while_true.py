
count = 0
should_continue = True
while should_continue:
    user_input = input("Enter the number: ")
    
    if user_input == "stop":
        should_continue = False
    else:
        count += int(user_input)
        continue
    
print("Sum of numbers: ", count)
