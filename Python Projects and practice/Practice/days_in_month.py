def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


user_year = int(input("Enter year: "))
user_month = int(input("Enter month: "))


def days_in_mont(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 30, 31, 30, 30, 30]

    if is_leap_year(year):
        month_days[month] += 1
        return month_days[month]

    else:
        return month_days[month]


days = days_in_mont(user_year, user_month-1)
print(days)
