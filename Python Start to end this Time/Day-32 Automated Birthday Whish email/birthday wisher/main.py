##################### Normal Starting Project ######################
import datetime as dt
import smtplib
import random
import pandas as pd
now = dt.datetime.now()
today_day = now.day
today_month = now.month

today = (today_month, today_day)
print("Today: ", today)

data = pd.read_csv('birthdays.csv')

birthdays_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        content = letter_file.read()
        content = content.replace("[NAME]", birthday_person['name'])
    print(content)

# 4. Send the letter generated in step 3 to that person's email address.
# HINT 1: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
# HINT 2: Remember to call .starttls()
# HINT 3: Remember to login to your email service with email/password. Make sure your security setting is set to allow less secure apps.
# HINT 4: The message should have the Subject: Happy Birthday then after \n\n The Message Body.

my_email = "your email"
my_password = "your password"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="lakho75@yahoo.com",
        msg=f"Subject: Happy birthday\n\n {content}"
    )


print("Mail has been sent successfully! have a nice day!")
