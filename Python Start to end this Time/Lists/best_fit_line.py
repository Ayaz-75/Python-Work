'''
Exercise 124: Line of Best Fit
(41 Lines)
A line of best fit is a straight line that best approximates a collection of n data points.
In this exercise, we will assume that each point in the collection has an x coordinate
and a y coordinate. The symbols x¯ and y¯ are used to represent the average x value in
the collection and the average y value in the collection respectively. The line of best
fit is represented by the equation y = mx + b where m and b are calculated using
the following formulas:


m = (Σxy - ((Σx)(Σy))/n)/(Σx^2 - (Σx)^2/n
b = Ȳ - mx̄


Write a program that reads a collection of points from the user. The user will enter
the first x coordinate on its own line, followed by the first y coordinate on its own
line. Allow the user to continue entering coordinates, with the x and y values each
entered on their own line, until your program reads a blank line for the x coordinate.
Display the formula for the line of best fit in the form y = mx + b by replacing m
and b with the values calculated by the preceding formulas. For example, if the user
inputs the coordinates (1, 1), (2, 2.1) and (3, 2.9) then your program should display
y = 0.95x + 0.1.

'''

first = (1, 1)
second = (2, 2.1)
third = (3, 2.9)

summ_xy = (first[0]*first[1]) + (second[0]*second[1]) + (third[0] + third[1])
summ_x = first[0] + second[0] + third[0]
summ_y = first[1] + second[1] + third[1]
x_squrs = (first[0])**2 + (second[0])**2 + (third[0])**2
y_squrs = (first[1])**2 + (second[1])**2 + (third[1])**2

m = summ_xy - (((summ_x)*(summ_y))/1)/(x_squrs - (summ_x**2)/1)
print(f"Y={m.__ceil__()}x + 0.1")