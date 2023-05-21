import csv
import json

with open("exam_results.csv", encoding="utf-8") as input_file:
    students = csv.DictReader(input_file)
    best_scores = dict()

    for student in students:
        student["best_score"] = int(student.pop("score"))

        best_scores.setdefault(student["email"], student)
        best_scores[student["email"]] = max(best_scores[student["email"]], student,
                                            key=lambda stud: (stud["best_score"], stud["date_and_time"]))

    best_scores = list(sorted(best_scores.values(), key=lambda bs: bs["email"]))

with open("best_scores.json", "w", encoding="utf-8") as output_file:
    json.dump(best_scores, output_file, indent=3)
