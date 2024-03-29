from collections import ChainMap


def deep_update(chainmap, key, value):
    for dictionary in chainmap.maps:
        if key in dictionary:
            dictionary[key] = value
    chainmap.setdefault(key, value)


# TEST_1:
chainmap = ChainMap({'city': 'Moscow'}, {'name': 'Arthur'}, {'name': 'Timur'})
deep_update(chainmap, 'name', 'Dima')

print(chainmap)

# TEST_2:
chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
deep_update(chainmap, 'age', 20)

print(chainmap)

# TEST_3:
chainmap = ChainMap({})
deep_update(chainmap, 'city', 'Moscow')

print(chainmap)

# TEST_4:
chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur', 'age': 29}, {'name': 'Anri', 'age': 20}, {'name': 'Dima', 'age': 20})
deep_update(chainmap, 'age', 29)

print(chainmap)

# TEST_5:
chainmap = ChainMap({})

print(deep_update(chainmap, 'city', 'Moscow'))

# TEST_6:
chainmap = ChainMap({'name': 'Tanya'}, {'name': 'Arthur'}, {'name': 'Timur'})

deep_update(chainmap, 'name', 'Dima')

print(chainmap)