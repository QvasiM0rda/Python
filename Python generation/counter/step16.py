import sys
from collections import Counter

students = Counter()
for line in sys.stdin.readlines():
    student, grade = line.strip().split()
    students[student] = int(grade)
print(students.most_common()[-2][0])