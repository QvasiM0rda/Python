import csv

companies = dict()
with open('salary_data.csv', encoding='utf-8') as file:
    salaries = list(csv.reader(file, delimiter=';'))[1:]
    
    for name, salary in salaries:
        companies[name] = companies.get(name, []) + [int(salary)]
        
for company, _ in sorted(companies.items(), key=lambda c: sum(c[1]) / len(c[1])):
    print(company)
