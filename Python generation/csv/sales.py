import csv

with open('sales.csv', encoding='utf-8') as file:
    sales = csv.reader(file, delimiter=";")
    next(sales)
    print(*[sale[0] for sale in sales if int(sale[1]) > int(sale[2])], sep="\n")
