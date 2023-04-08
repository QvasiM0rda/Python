from datetime import datetime, timedelta

def fill_up_missing_dates(dates):
    dates = sorted(datetime.strptime(d, '%d.%m.%Y') for d in dates)
    start, end = min(dates), max(dates)
    new_dates =[]
    while start <= end:
        new_dates.append(start.strftime('%d.%m.%Y'))
        start += timedelta(days=1)
    return sorted(new_dates)
