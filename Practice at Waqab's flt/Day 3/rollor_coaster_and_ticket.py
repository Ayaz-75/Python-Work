height = int(input("What is your height in cm: \n"))
age = int(input("What is yur age: "))

if height > 120:
    if age >= 18:
        print(f"You have to pay: $12")

    else:
        print(f"You have to pay: $7")

else:
    print(f"You can't ride the roller coaster")

