import csv


def condense_csv(filename, id_name):
    with open(filename, encoding="utf-8") as file:
        data = csv.reader(file)
        objects = dict()
        condensed = list()
        for name, prop, val in data:
            if name not in objects.values() and len(objects) > 0:
                condensed.append(objects)
                objects = dict()
            objects[id_name] = name
            objects[prop] = val
        condensed.append(objects)
    columns = objects.keys()
    
    with open("condensed.csv", "w", encoding="utf-8", newline='') as output:
        writer = csv.DictWriter(output, fieldnames=columns)
        writer.writeheader()
        writer.writerows(condensed)


condense_csv("data.csv", "object")
