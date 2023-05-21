import json
from datetime import time

with open("pools.json", encoding="utf-8") as input_file:
    data = json.load(input_file)
    max_size_pool = list()

    for pool in data:
        start, end = pool["WorkingHoursSummer"]["Понедельник"].split("-")
        start, end = start.split(":"), end.split(":")
        start = time(hour=10) >= time(hour=int(start[0]), minute=int(start[1])) <= time(hour=12)
        end = time(hour=int(end[0]), minute=int(end[1])) >= time(hour=12)

        if start and end:
            max_size_pool.append((pool["Address"], int(pool["DimensionsSummer"]["Length"]),
                                  int(pool["DimensionsSummer"]["Width"])))

    pool = max(max_size_pool, key=lambda p: (p[1], p[2]))
    print(pool[1], 'x', pool[2], sep='')
    print(pool[0])
