from collections import Counter


def scrabble(symbols, word):
    symbols = Counter(symbols.lower())
    word = Counter(word.lower())
    return len(word - symbols) == 0


print(scrabble('gEEkBEE', 'beegeek'))