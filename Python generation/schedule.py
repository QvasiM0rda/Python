from datetime import datetime, timedelta

mask = '%H:%M'
hour_begin = datetime.strptime(input(), mask)
hour_end = datetime.strptime(input(), mask)
class_time = timedelta(minutes=45)
break_time = timedelta(minutes=10)
while hour_begin < hour_end:
    if hour_begin + class_time <= hour_end:
        print(hour_begin.strftime(mask),
              (hour_begin + class_time).strftime(mask),
              sep=' - ')
    hour_begin += class_time + break_time
