'''
Exercise 137: Two Dice Simulation

In this exercise you will simulate 1,000 rolls of two dice. Begin by writing a function that 
simulates rolling a pair of six-sided dice. Your function will not take any parameters. It will
return the total that was rolled on two dice as its only result.
Write a main program that uses your function to simulate rolling two six-sided
dice 1,000 times. As your program runs, it should count the number of times that
each total occurs. Then it should display a table that summarizes this data. Express
the frequency for each total as a percentage of the number of rolls performed. Your
program should also display the percentage expected by probability theory for each
total. Sample output is shown below.

`````Total Simulated Expected Percent Percent`````

2 |  2.90   |2.78
___  _____  ______
3 |  6.90   |5.56
___  _____  ______
4 |  9.40   |8.33
___  _____  ______
5 |  11.90  |11.11
___  _____  ______
6 |  14.20  |13.89
___  _____  ______
7 |  14.20  |16.67
___  _____  ______
8 |  15.00  |13.89
___  _____  ______
9 |  10.50  |11.11
___  _____  ______
10|  7.90   |8.33
___  _____  ______
11|  4.50   |5.56
___  _____  ______
12|  2.60   |2.78
 
'''
import random

NUM_RUNS = 1000
total_dice = 6

def twoDice():
    d1 = random.randrange(1, total_dice)
    d2 = random.randrange(1, total_dice)


    return d1 + d2


# twoDice()

# Simulate many rolls and display the result
def main():
# Create a dictionary of expected proportions
    expected = {2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36, \
    7: 6/36, 8: 5/36, 9: 4/36, 10: 3/36, \
    11: 2/36, 12: 1/36}
    # Create a dictionary that maps from the total of two dice to the number of occurrences
    counts = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, \
    8: 0, 9: 0, 10: 0, 11: 0, 12: 0}

    # Simulate NUM RUNS rolls, and count each roll
    for i in range(NUM_RUNS):
        t = twoDice()
        counts[t] = counts[t] + 1


    # Display the simulated proportions and the expected proportions
    print("Total Simulated Expected")
    print("          Percent     Percent")
    for i in sorted(counts.keys()):
        print("%5d %11.2f %8.2f" % \
        (i, counts[i] / NUM_RUNS * 100, expected[i] * 100))



main()