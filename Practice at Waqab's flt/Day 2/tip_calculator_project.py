print("\n\n\n--------------Welcome to the tip calculator---------------")


total_bill = float(input("What is the total bill: "))
tip_percent = int(input("What percentage of tip would you like to give 10/12/15: "))
total_people = int(input("How many people to split the bill: "))

total_tip = (total_bill + (total_bill*tip_percent/100)) / total_people

print(f"Each person has to pay: {round(total_tip, 2)}")
