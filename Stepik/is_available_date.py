from datetime import datetime

def get_date_time(dates):
    mask = '%d.%m.%Y'
    dates = [datetime.strptime(''.join(d), mask) for d in dates.split('-')]
    if len(dates) > 1:
        start, end = [d.day for d in dates]
        print(start, end)


def is_available_date(booked_dates, date_for_booking):
    for bd in booked_dates:
        print(get_date_time(bd))


dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021'
print(is_available_date(dates, some_date))
