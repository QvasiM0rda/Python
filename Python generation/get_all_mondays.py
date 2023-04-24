import calendar

from datetime import date

def get_all_mondays(year):
    mondays = []
    for month in range(1, 13):
        days_in_month = calendar.monthrange(year, month)[1] + 1
        for day in range(1, days_in_month):
            if calendar.weekday(year, month, day) == 0:
                mondays.append(date(year, month, day))
            
    return mondays


print(get_all_mondays(2021))
