import json
import csv

with open("students.json", encoding="utf-8") as input_file,\
     open("data.csv", "w", encoding="utf-8", newline="") as output_file:

    students = json.load(input_file)
    names_and_phones = list()
    for student in students:
        if int(student["age"]) >= 18 and int(student["progress"]) >= 75:
            names_and_phones.append({"name": student["name"], "phone": student["phone"]})

    names_and_phones = sorted(names_and_phones, key=lambda s: s["name"])

    writer = csv.DictWriter(output_file, fieldnames=["name", "phone"])
    writer.writeheader()
    writer.writerows(names_and_phones)
