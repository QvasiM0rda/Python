import sys

athletes = ['Иванов', 'Ильин', 'Петров', 'Зинько', 'Сидоров', 'Васильев', 'Литвинов']
athletes[:3] = sys.stdin.read().split()
