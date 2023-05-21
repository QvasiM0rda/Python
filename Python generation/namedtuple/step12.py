from collections import namedtuple
import csv
from datetime import datetime


Meetings = namedtuple("Meetings", ["surname", "name", "meeting_date", "meeting_time"])
meetings = list()
mask = "%d.%m.%Y%H:%M"

with open("meetings.csv", encoding="utf-8") as file:
    data = csv.DictReader(file)
    for row in data:
        meetings.append(Meetings(*row.values()))

meetings = sorted(meetings, key=lambda m: datetime.strptime(m.meeting_date + m.meeting_time, mask))

for meeting in meetings:
    print(meeting.surname, meeting.name)
