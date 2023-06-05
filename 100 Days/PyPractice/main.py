# welcome to the tip calculator


total_bill = float(input("Enter the total bill: "))
tip_percent = int(input("How much tip do you want to give 10, 12 or 15: "))
total_bill_after_tip = total_bill + (total_bill * tip_percent / 100)
people = int(input("How many persons are there to split bill in:"))
total_tip = round(total_bill_after_tip / people, 2)
print("Everyone have to pay:", total_tip)