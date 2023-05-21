import csv

with open("titanic.csv", encoding="utf-8") as file:
    data = csv.DictReader(file, delimiter=";")
    
    survivors = list(row for row in data if row["survived"] == "1"
                     and int(float(row["age"])) < 18)

survivors = sorted(survivors, key=lambda survivor: survivor["sex"], reverse=True)
for survivor in survivors:
    print(survivor["name"])
    