from datetime import datetime

def get_time_and_records(text: list) -> tuple:
    pattern = '%d.%m.%Y; %H:%M'
    text = text.split('\n')
    time = datetime.strptime(text[0], pattern)
    return time, text


with open('diary.txt', encoding='utf-8') as file:
    records = file.read().split('\n\n')

diary = [get_time_and_records(record) for record in records]
diary = sorted(diary, key=lambda r: r[0])

for record in diary:
    print(*record[1], sep='\n', end='\n\n')
