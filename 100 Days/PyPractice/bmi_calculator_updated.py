weight = float(input("Enter your weight in kgs: "))
height = float(input("Enter your height in m: "))
bmi = weight / (height ** 2)
# print(bmi)
if bmi <= 18:
    print("Underweight")
elif 25 <= bmi <= 30:
    print("Overweight")