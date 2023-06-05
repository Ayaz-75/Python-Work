def format_name(f_name, l_name):

    if f_name == "" and l_name == "":
        return "no data given"
    f_name = f_name.title()
    l_name = l_name.title()
    return f"Formatted named: {f_name} {l_name}"


print(format_name("", ""))

