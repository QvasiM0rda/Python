from datetime import datetime, timedelta

mask = '%d.%m.%Y'

current_date = datetime.strptime(input(), mask)
current_year = current_date.year
seven_days = current_date + timedelta(days=7)

youngest = datetime.strptime('01.01.0001', mask)
youngest_name = 'Дни рождения не планируются'

for _ in range(int(input())):
    *name, birthday = input().split()
    name = ' '.join(name)
    birthday = datetime.strptime(birthday, mask)
    current_year_birthday = birthday.replace(year=current_year)

    if current_year_birthday < current_date:
        current_year_birthday = current_year_birthday.replace(year=current_year + 1)

    if birthday > youngest:
        youngest = birthday
        if current_date < current_year_birthday <= seven_days:
            youngest_name = name

print(youngest_name)
