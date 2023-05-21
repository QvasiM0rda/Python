from collections import Counter

books = Counter(b for b in input().split())

total = 0

for buyer in range(int(input())):
    book, price = input().split()
    if books[book] > 0:
        total += int(price)
        books[book] -= 1
print(total)