import csv

with open('deniro.csv', encoding='utf-8') as file:
    deniro = list(csv.reader(file))
    
col = int(input()) - 1
for film in sorted(deniro, key=lambda f: int(f[col]) if f[col].isdigit() else f[col]):
    print(*film, sep=',')
