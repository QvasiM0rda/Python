from datetime import datetime

def get_date_time(dates):
    mask = '%d.%m.%Y'
    dates = [datetime.strptime(''.join(d), mask) for d in dates.split('-')]
    if len(dates) > 1:
        dates = get_dates_between_two_date(dates)
    return dates


def is_available_date(booked_dates, date_for_booking):
    booked = []
    for bd in booked_dates:
        for d in get_date_time(bd):
            booked.append(d)
    for_booking = get_date_time(date_for_booking)
    print(booked)
    

dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021'
print(is_available_date(dates, some_date) == True)

'''04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021-04.11.2021'
print(is_available_date(dates, some_date) == False)

dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '06.11.2021'
print(is_available_date(dates, some_date) == False)

dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '12.11.2021'
print(is_available_date(dates, some_date) == False)

dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '09.11.2021'
print(is_available_date(dates, some_date) == False)

dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '15.11.2021'
print(is_available_date(dates, some_date) == False)

dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '17.11.2021'
print(is_available_date(dates, some_date) == False)

dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '22.11.2021-25.11.2021'
print(is_available_date(dates, some_date) == True)

dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '01.11.2021-04.11.2021'
print(is_available_date(dates, some_date) == False)

dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '02.11.2021-05.11.2021'
print(is_available_date(dates, some_date) == False)

dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '10.11.2021-14.11.2021'
print(is_available_date(dates, some_date) == False)

dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '03.11.2021-05.11.2021'
print(is_available_date(dates, some_date) == False)

dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '09.11.2021-10.11.2021'
print(is_available_date(dates, some_date) == False)

dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '06.11.2021-08.11.2021'
print(is_available_date(dates, some_date) == False)

dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '14.11.2021-22.11.2021'
print(is_available_date(dates, some_date) == False)

dates = ['14.09.2022-14.10.2022']
some_date = '20.09.2022'
print(is_available_date(dates, some_date) == False)

dates = ['14.09.2022-14.10.2022']
some_date = '14.11.2022'
print(is_available_date(dates, some_date) == True)

dates = ['14.09.2022-14.10.2022']
some_date = '15.11.2022-16.11.2022'
print(is_available_date(dates, some_date) == True)

dates = ['14.09.2022-14.10.2022']
some_date = '14.09.2022-22.09.2022'
print(is_available_date(dates, some_date) == False)

dates = ['02.11.2021', '05.11.2021-09.11.2021']
some_date = '04.11.2021'
print(is_available_date(dates, some_date) == True)
'''
