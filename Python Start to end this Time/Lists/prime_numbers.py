'''
Write down all of the numbers from 0 to the limit
Cross out 0 and 1 because they are not prime

'''
num = int(input("Enter the number: "))

for number in range(2, num):
    for item in range(2, number):
        if number % item == 0:
            break

    else:
        print(number)
