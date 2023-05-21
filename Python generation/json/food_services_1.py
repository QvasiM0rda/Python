import json

with open("food_services.json", encoding="utf-8") as input_file:
    food_services = json.load(input_file)

    districts = dict()
    net_objects = dict()

    for food_service in food_services:
        districts.setdefault(food_service["District"], 0)
        districts[food_service["District"]] += 1

        if food_service["IsNetObject"] == "да":
            net_objects.setdefault(food_service["OperatingCompany"], 0)
            net_objects[food_service["OperatingCompany"]] += 1

print(*max(districts.items(), key=lambda district: district[1]), sep=": ")
print(*max(net_objects.items(), key=lambda net_object: net_object[1]), sep=": ")
