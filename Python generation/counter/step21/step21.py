import csv
import json
from collections import Counter


def get_products_from_file(filename: str) -> Counter:
    with open(filename, encoding="utf-8") as data:
        products = Counter()
        data.readline()
        for row in data.readlines():
            prod, *amnt = row.strip().split(",")
            products[prod] = sum(int(n) for n in amnt)
    return products


total_products = Counter()
for file in ["quarter1.csv", "quarter2.csv", "quarter3.csv", "quarter4.csv"]:
    total_products += get_products_from_file(file)

with open("prices.json", encoding="utf-8") as json_file:
    json_data = json.load(json_file)
    for product, amount in total_products.items():
        total_products[product] = amount * json_data[product]

print(total_products.total())
