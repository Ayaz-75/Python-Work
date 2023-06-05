
# try:
#     file = open('a_file.txt')
#     file.read()
#     a = {"key": "value"}
#     print(a["sdfsdf"])
# except FileNotFoundError:
#     file = open('a_file.txt', 'w')
#     file.write('Something')
#
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
#
# else:
#     content = file.read()
#     print(content)
#
# finally:
#     raise KeyError("This is the error which i made")
#


height = float(input("Enter height: "))
weight = float(input("Enter weight: "))


if height > 2.5:
    raise ValueError("Human height can not exceed 2.5 meters")

print(weight / height ** 2)
