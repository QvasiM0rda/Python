from datetime import datetime, timedelta

def choose_plural(amount, declensions):
    declension = 2
    if amount % 100 not in (11, 12, 13, 14):
        if amount % 10 == 1:
            declension = 0
        elif amount % 10 in (2, 3, 4):
            declension = 1
    return f'{amount} {declensions[declension]}'


def get_days_hours_minutes(delta):
    days = delta.days if delta.days else ''
    hours = delta.seconds // 3600 if delta.seconds // 3600 else ''
    minutes = (delta.seconds // 60) % 60 if (delta.seconds // 60) % 60 else ''
    times = [days, hours, minutes]
    print(' и '.join(times))
    

mask = '%d.%m.%Y %H:%M'
release_date = datetime.strptime('08.11.2022 12:00', mask)
current_date = datetime.strptime(input(), mask)

days_before_release = release_date - current_date
get_days_hours_minutes(days_before_release)
#print(f'До выхода курса осталось: {get_days_hours_minutes(days_before_release)}')
