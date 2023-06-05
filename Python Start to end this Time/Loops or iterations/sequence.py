"""
The condition for this loop is n != 1, so the loop will continue until n is 1, which
makes the condition false.
Each time through the loop, the program outputs the value of n and then checks
whether it is even or odd. If it is even, n is divided by 2. If it is odd, the value of n is
replaced with n*3 + 1. For example, if the argument passed to sequence is 3, the
resulting values of n are 3, 10, 5, 16, 8, 4, 2, 1.
"""


def sequence(n):
    while n != 1:
        print(n)
        if n % 2 == 0:
            n = n / 2
        else:
            n = n * 3 + 1


sequence(3)
