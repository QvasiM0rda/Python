class Filter:
    def __init__(self, predicate=None):
        self.predicate = bool if predicate is None else predicate


    def __call__(self, iterable):
        return list(filter(self.predicate, iterable))


more_than_five = Filter()
numbers = [13, 1, 0, 4, 10, 10, 7]

print(more_than_five(numbers))
