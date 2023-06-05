"""Functions with Outputs"""


'''def change_case(f_name, l_name):
    full_name = f_name + l_name
    return full_name.title()


print(change_case("ayaz", " lakho"))'''

# -------------------------------- using return only ------------------------------------


'''def format_name(f_name, l_name):
    formatted_f = f_name.title()
    formatted_l = l_name.title()

    if formatted_f == "" or formatted_l == "":
        return "you have not provided any value"

    else:
        return formatted_f + formatted_l


first_name = input("what is your first name?: ")
last_name = input("what is your last Name?: ")

print(format_name(first_name, last_name))'''

A = 12
B = 15

c = A
while c > 0:
    print(c - 1)
    c -= 1

