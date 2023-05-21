from collections import defaultdict


def flip_dict(dict_of_lists: dict) -> defaultdict:
    flipped_dict = defaultdict(list)
    for key, values in dict_of_lists.items():
        for value in values:
            flipped_dict[value].append(key)
    return flipped_dict


print(flip_dict({'a': [1, 2], 'b': [3, 1], 'c': [2]}))

data = {'Arthur': ['cacao', 'tea', 'juice'], 'Timur': ['coffee', 'tea', 'juice'], 'Anri': ['juice', 'coffee']}

for key, values in flip_dict(data).items():
    print(f'{key}: {", ".join(values)}')
