word = input()
borders = '+' + '-' * (len(word) + 2) + '+'
print(borders)
print(f'| {word} |')
print(borders)