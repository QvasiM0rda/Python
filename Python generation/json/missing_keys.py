import json

with open("people.json", encoding="utf-8") as input_file,\
        open("updated_people.json", "w", encoding="utf-8") as output_file:
    json_data = json.load(input_file)
    keys_set = set()
    for json_object in json_data:
        keys_set = keys_set.union(set(json_object.keys()))

    output_data = list()
    for json_object in json_data:
        if json_object.keys() != keys_set:
            for key in keys_set.difference(set(json_object.keys())):
                json_object[key] = None
        output_data.append(json_object)
    json.dump(output_data, output_file)
