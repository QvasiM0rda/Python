import csv
from collections import Counter


with open("name_log.csv", encoding="utf-8") as file:
    emails = Counter(user["email"] for user in csv.DictReader(file))

for email, count in sorted(emails.items()):
    print(f"{email}: {count}")
