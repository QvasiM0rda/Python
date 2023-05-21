import json

with open("food_services.json", encoding="utf-8") as input_file:
    food_services = json.load(input_file)

    type_objects = dict()

    for fs in food_services:
        obj = [fs["Name"], fs["SeatsCount"]]
        type_objects.setdefault(fs["TypeObject"], obj)
        type_objects[fs["TypeObject"]] = max(type_objects[fs["TypeObject"]], obj, key=lambda o: o[1])

type_objects = dict(sorted(type_objects.items(), key=lambda to: to[0]))

for k, v in type_objects.items():
    print(k, ": ", v[0], ", ", v[1], sep="")
