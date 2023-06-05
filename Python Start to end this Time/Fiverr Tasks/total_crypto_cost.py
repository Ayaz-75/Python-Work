'''
Write a program to process orders for a shop which sells vouchers for cryptocurrency
Each voucher has a minimum value of £12.00 up to a maximum of £48.00. Each transaction can
only be for a single type of cryptocurrency.
The maximum number of vouchers which can be sold in any one transaction is 100. There is no
minimum quantity.


The program should:
• Input the name of the currency, number of vouchers sold and the price of each voucher.
• Award a percentage discount according to the number of vouchers ordered (round to 2
decimal places).
• Calculate and display the final cost and any other suitable information.
The discount will be awarded as follows:


Vouchers bought      Discount %

Between 71 and 100      10
Between 41 and 70       7.5
Between 20 and 40       5
Less than 20            none


Program Design – Main Steps
1. Get user inputs (must include input validation where possible)
2. Calculate discount percentage
3. Calculate actual discount
4. Calculate final cost
5. Display final cost & other info

'''


def inputs_cnp(curr, num_of_voucher_sold, price_of_voucher):
    discount_percent = 0
    discount = 0
    final_cost = 0
    if num_of_voucher_sold <= 100 and (12 < price_of_voucher < 48):

        if 71 <= num_of_voucher_sold <= 100:
            discount_percent += ((price_of_voucher * 10) / 100)

        elif 41 <= num_of_voucher_sold <= 70:
            discount_percent += ((price_of_voucher * 7.5) / 100)

        elif 20 <= num_of_voucher_sold <= 40:
            discount_percent += ((price_of_voucher * 5) / 100)

        else:
            discount_percent = 0

        final_cost = (price_of_voucher * num_of_voucher_sold) - discount_percent
        discount = ((price_of_voucher * num_of_voucher_sold) - final_cost) * num_of_voucher_sold

    return f"Discount: {discount_percent}%, \nTotal Discount: £{discount.__round__(2)}, \nFinal cost: £{final_cost}"


currency = input("What is the currency you are working with ? ")
vouchers_sold = int(input("How many vouchers are sold ? "))
voucher_price = float(input("What is the price of each voucher ? "))


print(inputs_cnp(currency, vouchers_sold, voucher_price))
