"""

Exercise 7-3.
The mathematician Srinivasa Ramanujan found an infinite series that can be used to
generate a numerical approximation of 1/π:

1/π = (2 * sqrt(2)/9801) ∑ (4k)! (1103 + 26390k)/(k!)^4 *396^4k

Write a function called estimate_pi that uses this formula to compute and return an
estimate of π.

It should use while loop to compute terms of the summation until the last term is
smaller than 1e-15
(which is Python notation for 10−15).

You can check the result by comparing it to math.pi.

"""
