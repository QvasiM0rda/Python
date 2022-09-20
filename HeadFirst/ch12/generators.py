data = [ 1, 2, 3, 4, 5, 6, 7, 8 ]
evens = [num for num in data if not num % 2]

data = [ 1, 'one', 2, 'two', 3, 'three', 4, 'four']
words = [num for num in data if isinstance(num, str)]

data = list('So long and thanks for all the fish'.split())
title = [word.title() for word in data]
