import csv


def csv_column(filename):
    data = dict()
    with open(filename, encoding='utf-8') as file:
        rows = csv.DictReader(file)
        for row in rows:
            for key, value in row.items():
                data.setdefault(key, [])
                data[key].append(value)
    return data
    

print(csv_column('exam.csv'))
