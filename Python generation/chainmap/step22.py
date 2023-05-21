import json
from collections import ChainMap

with open("zoo.json", encoding="utf-8") as input_file:
    chainmap_zoo = ChainMap(*json.load(input_file))

print(sum(chainmap_zoo.values()))
