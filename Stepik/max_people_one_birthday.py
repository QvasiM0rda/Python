from datetime import datetime, timedelta

mask = '%d.%m.%Y'
employees = dict()
max_employees = 0
for _ in range(int(input())):
    *name, birthday = input().split()
    name = ' '.join(name)
    birthday = datetime.strptime(birthday, mask)
    employees.setdefault(birthday, [])
    employees[birthday].append(name)
    max_employees = max(max_employees, len(employees[birthday]))

for birthday, people in sorted(employees.items()):
    if len(people) == max_employees:
        print(birthday.strftime(mask))
