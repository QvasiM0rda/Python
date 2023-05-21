import csv

domains = dict()
with open("data.csv", encoding="utf-8") as file:
    data = list(csv.reader(file))[1:]
    for *_, email in data:
        email = email.split('@')[1]
        domains[email] = domains.get(email, 0) + 1

domains = sorted(domains.items(), key=lambda item: (item[1], item[0]))

with open("domain_usage.csv", "w", encoding="utf-8", newline='') as output:
    writer = csv.writer(output)
    writer.writerow(["domain", "count"])
    writer.writerows(domains)