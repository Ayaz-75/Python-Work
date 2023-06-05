
condition=True
while condition:
    i=int(input("Enter the number"))

    if i<0:
        print("Number entered is negative ",i)
        break

    else:
        print("Enter number again")
        continue
    i+=1