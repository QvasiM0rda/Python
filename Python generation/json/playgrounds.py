import csv
import json

with open("playgrounds.csv", encoding="utf-8") as input_file,\
     open("addresses.json", "w", encoding="utf-8") as output_file:

    cvs_data = csv.DictReader(input_file, delimiter=";")
    adm_areas = dict()
    for playground in cvs_data:
        area, district = playground["AdmArea"], playground["District"]
        adm_areas.setdefault(area, dict())
        adm_areas[area].setdefault(district, list())
        adm_areas[area][district].append(playground["Address"])

    json.dump(adm_areas, output_file, ensure_ascii=False)
