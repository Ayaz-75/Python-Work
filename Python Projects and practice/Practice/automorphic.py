is_on = True
while is_on:
    number = int(input("Enter the number to be checked: "))
    st_num = number
    square = number ** 2
    count = 0
    num = 1

    while number > 0:
        count += 1
        number //= 10
    #    print(count)

    for i in range(count):
        num = num * 10

    l_digit = square % num
    if st_num == l_digit:
        print(st_num, "is Automorphism")
    else:
        print(st_num, "is not Automorphism")

    do_continue = input("Do you want to continue ? ")
    if do_continue == "yes":
        is_on = True
    else:
        is_on = False
        print("Good bye")
