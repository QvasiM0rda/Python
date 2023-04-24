import calendar

from datetime import date

def get_days_in_month(year, month):
    month = list(calendar.month_name).index(month)
    days_in_month = calendar.monthrange(year, month)[1] + 1
    return [date(year, month, day) for day in range(1, days_in_month)]


print(get_days_in_month(2021, 'February'))
