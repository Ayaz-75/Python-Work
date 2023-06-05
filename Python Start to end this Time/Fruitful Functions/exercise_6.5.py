"""
Exercise 6-5.
The greatest common divisor (GCD) of a and b is the largest number that divides
both of them with no remainder.
One way to find the GCD of two numbers is based on the observation that if r is the
remainder when a divided by b, then gcd(a, b) = gcd(b,r) . As a base case, we can
use gcd(a , 0) = a.
Write a function called gcd that takes parameters a and b and returns their greatest
common divisor.
Credit: This exercise is based on an example from Abelson and Sussman’s Structure
and Interpretation of Computer Programs (MIT Press, 1996)

"""
import math


def gc_d(a, b):
    result = math.gcd(a, b)
    return result


print(gc_d(9, 6))


# a = 10
# b = 4
# print(a % b)

