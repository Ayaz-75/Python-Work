"""
Exercise 5-2.
Fermat’s Last Theorem says that there are no positive integers a, b, and c such that
a^n + b^n = c^n

for any values of n greater than 2.

1. Write a function named check_fermat that takes four parameters—a, b, c and n
—and checks to see if Fermat’s theorem holds. If n is greater than 2 and

a^n + b^n = c^n

the program should print, “Holy smokes, Fermat was wrong!”, Otherwise the pro‐
gram should print, “No, that doesn’t work.”

# ##################################################################################
'''
2. Write a function that prompts the user to input values for a, b, c and n, converts
them to integers, and uses check_fermat to check whether they violate Fermat’s
theorem.
'''
"""

# Both examples are done in one program
# a = 5
# b = 2
# print(math.pow(a, b))


def check_fermat(a, b, c, n):
    cn = c ** n  # math.pow(c, n) this performs the same as this expression does
    an = a ** n  # math.pow(a, n) this performs the same as this expression does
    bn = b ** n  # math.pow(b, n) this performs the same as this expression does

    if n > 2 and (cn == an + bn):
        print("Holy smokes, Fermat was wrong!")

    else:
        print("Fermat was right")


i_a = int(input("What should be the value of a: "))
i_b = int(input("What should be the value of b: "))
i_c = int(input("What should be the value of b: "))
i_n = int(input("What should be the value of b: "))

check_fermat(i_a, i_b, i_c, i_n)
