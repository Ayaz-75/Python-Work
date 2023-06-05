'''
for i in range(6):
    for j in range(1, i+1):
        print(i*j, " ", end="")
    print()
'''
'''
for i in range(6):
    for j in range(7-i):
        print(" ", end="")
    for k in range(1, i+1):
        print("*", end="")
    print()
'''

'''
for i in range(1, 5+1):
    for j in range(1, 6-i):
        print("*", " ", end="")
    print()'''

'''for i in range(1, 7):
    for j in range(1, i):
        print(i-j, end="")
    print()'''

'''for i in range(6):
    for j in range(1, 6-i):
        print(j, end="")
    print()'''
'''for i in range(1, 6):
    for j in range(6-i):
        print(" ", " ", end="")
    for k in range(1, i+1):
        print(k, " ", end="")
    print()
'''
'''for i in range(1, 5):
    for j in range(1, 5):
        print(j, end="")
    print()
'''
'''for i in range(1, 6):
    for j in range(i):
        print(i, end="  ")
    for k in range(1, 6-i):
        print(k+i, end="  ")
    print()
    '''
'''for i in range(1, 9):
    for k in range(1, i+1):
        print(" ", end="")
    for j in range(8-i):
        print("* ", end="")
    print()
for i in range(1, 9):
    for k in range(8-i):
        print(" ", end="")
    for j in range(1, i+1):
        print("* ", end="")
    print()
'''
'''for i in range(1, 9):
    for k in range(8-i):
        print(" ", end="")
    for j in range(1, i+1):
        print("* ", end="")
    print()
for i in range(1, 9):
    for k in range(1, i+1):
        print(" ", end="")
    for j in range(8-i):
        print("* ", end="")
    print()
'''
'''for i in range(1, 10):
    for j in range(10 - i):
        print("*", end="")
    for k in range(1, i):
        print(" ", end="")
    for l in range(1, i):
        print(" ", end="")
    for m in range(10-i):
        print("*", end="")
    print()
'''
# python in pattern
'''string_py = "Python"
for i in range(len(string_py)+1):
    for j in range(i):
        print(string_py[j], end="")
    print()
'''
'''num = 65
for i in range(8):
    for k in range(8-i):
        print(" ", end="")
    for j in range(i):
        char = chr(num)
        print(char, end="")
        num += 1
    print()
'''
'''k = 1
for i in range(1, 5):
    for j in range(i):
        print(j+k, end=" ")
    k += i
    print()'''

'''for i in range(5):
    for j in range(5-i):
        print(" ", end="")
    for k in range(1, i):
        print("*", end="")
    for l in range(i):
        print("*", end="")
    print()
'''
'''str_py = input("Enter the string: ")
for i in range(len(str_py)+1):
    for j in range(len(str_py)-i):
        print(str_py[j], end="")

    for k in range(i):
        print(" ", end="")

    for m in range(i):
        print(" ", end="")

    for j in range(len(str_py)-i):
        print(str_py[j], end="")
    print()
'''

num = 65
for i in range(5):
    for j in range(i):
        st = chr(num)
        print(st, end="")
        num += 1
    num = 65
    print()
