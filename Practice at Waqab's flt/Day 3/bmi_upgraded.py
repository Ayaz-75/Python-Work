weight = input("Enter weight in kg: ")
height = input("Enter height in m: ")
bmi = round(int(weight)/ float(height) ** 2, 2)

if bmi < 18.5:
    print(f"Your BMI is {bmi} you are underweight")

elif 18.5 < bmi < 25:
    print(f"Your BMI is {bmi} you are Normal in weight")

elif 25 < bmi < 30:
    print(f"Your BMI is {bmi} you are overweight")

elif 30 < bmi < 35:
    print(f"Your BMI is {bmi} you are obese")

else:
    print(f"Your BMI is {bmi} you are clinically obese")

