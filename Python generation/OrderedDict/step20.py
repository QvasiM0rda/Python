from collections import OrderedDict


def custom_sort(ordered_dict: OrderedDict, by_values=False) -> None:
    for key, _ in sorted(ordered_dict.items(), key=lambda od: od[by_values]):
        ordered_dict.move_to_end(key)


data = OrderedDict(Dustin=29, Anabel=17, Brian=40, Carol=16)
custom_sort(data)

print(data)

data = OrderedDict(Earth=3, Mercury=1, Mars=4, Venus=2)
custom_sort(data, by_values=True)

print(*data.items())
