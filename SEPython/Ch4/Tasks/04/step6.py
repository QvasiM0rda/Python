import sys

values = [184.414, 174.12, 581, 145.98, 159.1, 824.24]
values += (float(n) for n in sys.stdin.read().splitlines())

print("%.3f" % (sum(values) / len(values)))
