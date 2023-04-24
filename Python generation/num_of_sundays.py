from datetime import date

def num_of_sundays(year):
    last_day = date(year, 12, 31)
    return date.strftime(last_day, '%U')


print(num_of_sundays(2021))

year = 2000
print(num_of_sundays(year))

print(num_of_sundays(768))
