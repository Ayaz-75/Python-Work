

# def my_function():
#     return 3 * 2

# result = my_function()
# print(result)


def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "Your didn't provide valid inputs."
    return f"{f_name.title()} {l_name.title()}"


full_name = format_name(input("Enter your first name: "), input("Enter your last name: "))
print(full_name)
