from collections import Counter

words = Counter(len(word) for word in input().split())
for length, amount in sorted(words.items(), key=lambda i: i[1]):
    print(f"Слов длины {length}: {amount}")
