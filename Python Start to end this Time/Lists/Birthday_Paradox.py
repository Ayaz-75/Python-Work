'''
Exercise 10-8.
This exercise pertains to the so-called Birthday Paradox, which you can read about at
http://en.wikipedia.org/wiki/Birthday_paradox.

If there are 23 students in your class, what are the chances that two of you have the
same birthday?

You can estimate this probability by generating random samples of 23
birthdays and checking for matches.

Hint: you can generate random birthdays with
the randint function in the random module.

'''
import random


def random_bdays(n):
    """Returns a list of integers between 1 and 365, with length n.
    n: int
    returns: list of int
    """
    t = []
    for i in range(n):
        bday = random.randint(1, 365)
        t.append(bday)
    return t


print(random_bdays(2))
