from collections import defaultdict


def wins(pairs):
    winners = defaultdict(set)
    for pair in pairs:
        winners[pair[0]].add(pair[1])
    return winners


result = wins([('Тимур', 'Артур'), ('Тимур', 'Дима'), ('Дима', 'Артур')])

for winner, losers in sorted(result.items()):
    print(winner, '->', *sorted(losers))


result = wins([('Артур', 'Дима'), ('Артур', 'Тимур'), ('Артур', 'Анри'), ('Дима', 'Артур')])

for winner, losers in sorted(result.items()):
    print(winner, '->', *sorted(losers))