from collections import namedtuple
import pickle

Animal = namedtuple('Animal', ['name', 'family', 'sex', 'color'])

with open("data.pkl", mode="rb") as pickle_file:
    for animal in pickle.load(pickle_file):
        for field, value in zip(Animal._fields, animal):
            print(f'{field}: {value}')
        print()
