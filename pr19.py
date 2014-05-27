def is_leap_year(n):
    if n % 400 == 0:
        return True
    if n % 100 == 0:
        return False
    if n % 4 == 0:
        return True
    return False

def is_valid_date(month, day, year):
    leap_year = is_leap_year(year)
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if leap_year:
        days_in_month[1] = 29
    return (day > 0 and day <= days_in_month[month - 1])


def day_of_week(month, day, year):
    """Uses Lewis Carroll's Algorithm for determining day of week"""
    leap_year = is_leap_year(year)
    centuries = year / 100
    years_left = year % 100
    century_item = 2 * (3 - centuries % 4)
    year_item = years_left / 12 + years_left % 12 + (years_left % 12) / 4
    months = [0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5]
    month_item = months[month - 1]
    day_item = day
    if leap_year and (month == 1 or month == 2):
        day_item -= 1
    return (century_item + year_item + month_item + day_item) % 7


def num_weekdays(start_year, end_year, desired_day):
    count = 0
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            days = days_in_month[month - 1] + 1
            for day in range(1, days):
                if day == 1 and day_of_week(month, day, year) == desired_day:
                    count += 1
    return count

print num_weekdays(1901, 2000, 0)