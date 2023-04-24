import calendar
from datetime import datetime

year = int(input())

for month in range(1, 13):
    week = 2 + int(calendar.weekday(year, month, 1) > 3)
    third_thursday = calendar.monthcalendar(year, month)[week][3]
    print(datetime(year, month, third_thursday).strftime('%d.%m.%Y'))
