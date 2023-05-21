import sys

revenue = [178, 351, 0, 764, 514, 0,
           411, 145, 0, 245, 441, 0]

revenue[2::3] = (int(m) for m in sys.stdin.read().splitlines())

print(sum(revenue[:3]), sum(revenue[3:6]), sum(revenue[6:9]), sum(revenue[9:]))