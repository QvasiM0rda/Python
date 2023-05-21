import csv
from datetime import datetime

mask = "%d/%m/%Y %H:%M"

with open("name_log.csv", encoding="utf-8") as log:
    name_log = list(csv.reader(log))
    columns = name_log.pop(0)
    users = dict()
    
    for username, email, dtime in name_log:
        dtime = datetime.strptime(dtime, mask)
        users.setdefault(email, ["", datetime.strptime("01/01/0001 00:00", mask)])
        if dtime > users[email][1]:
            users[email] = [username, dtime]

users = dict(sorted(users.items(), key=lambda item: item[0]))

with open("new_name_log.csv", "w", encoding="utf-8", newline="") as output:
    writer = csv.writer(output)
    writer.writerow(columns)
    for user, values in users.items():
        writer.writerow([values[0], user, values[1].strftime(mask)])
