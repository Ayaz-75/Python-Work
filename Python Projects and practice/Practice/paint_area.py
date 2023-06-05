
def find_area(height, width, cover):
    area = (height * width) / cover
    return round(area)


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

print(f"you will need {find_area(test_h, test_w, coverage)} cans of paint")
