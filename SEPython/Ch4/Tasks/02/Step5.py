import sys

cities = ["Прага", "Вена", "Санкт-Петербург"]

new_cities = sys.stdin.read().splitlines()
print(cities + new_cities)