'''
Exercise 128: Count the Elements

Python’s standard library includes a method named count that determines how
many times a specific value occurs in a list. In this exercise, you will create a new
function named countRange. It will determine and return the number of elements
within a list that are ```greater``` than or equal to some ```minimum``` value and ```less```
than some ```maximum``` value. Your function will take three parameters: the list, the minimum
value and the maximum value. It will return an integer result greater than or equal to
0. Include a main program that demonstrates your function for several different lists,
minimum values and maximum values. Ensure that your program works correctly
for both lists of integers and lists of floating-point numbers.

'''

def CountItems():
    my_list = [1, 2, 9, 4, 5, 6, 17, 8, 9, 33, 22]
    new_list = []
    mini_mum = my_list[0]
    maxi_mum = mini_mum

    count = 0
    for item in my_list:
        count += 1
        if mini_mum > item:
            mini_mum = item
        elif maxi_mum < item:
            maxi_mum = item

    for item in my_list:
        if item > mini_mum and item < maxi_mum:
            new_list.append(item)
    return new_list

    # print(mini_mum)
    # print(maxi_mum)


print(CountItems())
