

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


# print(is_leap_year(2020))

def days_in_month(year, month):
    month_days = [30, 28, 31, 30, 31, 30, 30, 30, 31, 30, 30, 30]

    if is_leap_year(year):
        month_days[1] += 1
        return f"{month + 1} has {month_days[month]} days"
    else:
        return f"{month + 1} month has {month_days[month]} days"


print(days_in_month(2021, 2-1))
