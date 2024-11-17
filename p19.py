"""
Problem 19:
1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""
def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def count_sundays():
    # Days in each month (non-leap year)
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    day_of_week = 2  # 1 Jan 1901 was a Tuesday (0 = Sunday, 1 = Monday, ...)
    count = 0

    for year in range(1901, 2001):
        for month in range(12):
            if day_of_week == 0:
                count += 1
            
            # Move to the first day of the next month
            day_of_week = (day_of_week + days_in_month[month]) % 7
            
            # Adjust for leap year
            if month == 1 and is_leap_year(year):
                day_of_week = (day_of_week + 1) % 7

    return count

print(count_sundays())
