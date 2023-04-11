from datetime import datetime

mask = '%d.%m.%Y'
eldest = datetime.strptime('31.12.9999', mask)
eldest_name = ''
eldest_count = 1
for _ in range(int(input())):
    *name, birthday = input().split()
    name = ' '.join(name)
    birthday = datetime.strptime(birthday, mask)
    if birthday < eldest:
        eldest = birthday
        eldest_name = name
        eldest_count = 1
    elif birthday == eldest:
        eldest_count += 1

print(eldest.strftime(mask), end=' ')
if eldest_count > 1:
    print(eldest_count)
else:
    print(eldest_name)
