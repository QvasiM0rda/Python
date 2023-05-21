from collections import ChainMap


def get_all_values(chainmap: ChainMap, key) -> set:
    return {dictionary[key] for dictionary in chainmap.maps if key in dictionary}


c = ChainMap({'name': 'Anri'}, {'name': 'Arthur', 'age': 20}, {'name': 'Timur', 'age': 29})
r = get_all_values(c, 'age')

print(*sorted(r))
