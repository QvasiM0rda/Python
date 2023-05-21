from collections import Counter

data = Counter('aksjaskfjsklfjdslkfjajfopewtoieqpwdpqworiiqjskanvmcxbmpewrqopkqwlmdzczmxvmvlnjpjqpkqzxvmbowiqeorewi')

data.min_values = lambda: [char for char in data.items() if char[1] == min(data.values())]
data.max_values = lambda: [char for char in data.items() if char[1] == max(data.values())]
