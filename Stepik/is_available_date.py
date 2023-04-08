from datetime import datetime

def from_string_to_date(dates):
    mask = '%d.%m.%Y'
    dates = [datetime.strptime(d, mask) for d in dates.split('-')]
    if len(dates) > 1:
        start, end = map(datetime.timestamp, dates)
        while start < end - 86400:
            start += 86400
            dates.append(datetime.fromtimestamp(start))
    return dates


def is_available_date(booked_dates, date_for_booking):
    booked = []
    for bd in booked_dates:
        for d in from_string_to_date(bd):
            booked.append(d)
    for dfb in from_string_to_date(date_for_booking):
        if dfb in booked:
            return False
    return True
