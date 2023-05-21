import csv

with open("student_counts.csv", encoding="utf-8") as file:
    data = csv.DictReader(file)
    classes = list(data)
    columns = ["year"] + sorted(data.fieldnames[1:],
                                key=lambda c: (int(c.split("-")[0]), c.split("-")[1]))

with open("sorted_student_counts.csv", "w", encoding="utf-8", newline="") as output:
    writer = csv.DictWriter(output, fieldnames=columns)
    writer.writeheader()
    writer.writerows(classes)
