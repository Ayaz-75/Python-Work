import random
i=random.randint(1,5)

condition=True
while condition:
    a=int(input("Enter number"))

    if a==i:
        print("You guessed it")
        break
    else:
        print("Try again")
        continue