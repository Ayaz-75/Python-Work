# welcome to the paint area calculator
width = float(input("Enter width: "))
height = float(input("Enter height: "))
coverage = int(input("Enter coverage: "))


def calc_area(h, w, c):
    return round((h * w) / c)


print(calc_area(h=height, w=width, c=coverage))
