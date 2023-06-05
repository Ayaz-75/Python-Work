# -------------- Happy number ----------------
number = 7

addition_of_squares = 0
while addition_of_squares != 1:
    addition_of_squares = 0
    while number > 0:
        sep_digits = number % 10
        digits_squares = sep_digits ** 2
        addition_of_squares += digits_squares
        number //= 10
    number = addition_of_squares
    number //= 10

print(addition_of_squares)
