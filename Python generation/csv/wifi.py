import csv

districts = dict()
with open("wifi.csv", encoding="utf-8") as file:
    data = list(csv.reader(file, delimiter=";"))[1:]
    for _, district, _, wifi_count in data:
        districts[district] = districts.get(district, 0) + int(wifi_count)

districts = dict(sorted(districts.items(), key=lambda item: (-item[1], item[0])))

for district, number_of_access_points in districts.items():
    print(f"{district}: {number_of_access_points}")
