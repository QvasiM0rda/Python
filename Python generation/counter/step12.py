from collections import Counter

words = Counter(word.lower() for word in input().split())
print(words.most_common(1)[0][0])
