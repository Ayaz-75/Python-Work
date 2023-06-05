
MINIMUM_VOUCHER_VALUE = 12
MAXIMUM_VOUCHER_VALUE = 48


'''
The program should:
• Input the name of the currency, number of vouchers sold and the price of each voucher.
• Award a percentage discount according to the number of vouchers ordered (round to 2 
  decimal places).
• Calculate and display the final cost and any other suitable information.

'''

discount_percent = 0

name_of_currency = input("What is the name of currency: ")
number_of_voucher_sold = int(input("What is the number of voucher sold: "))

if 71 < number_of_voucher_sold < 100:
    discount_percent = 10

elif 41 < number_of_voucher_sold < 70:
    discount_percent = 7.5

elif 20 < number_of_voucher_sold < 40:
    discount_percent = 5

else:
    discount_percent = 0


total_percentage = (discount_percent / number_of_voucher_sold) * 100
print(total_percentage)

