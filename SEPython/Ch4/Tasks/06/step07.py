school_marks = [3, 4, 4, 5, 3, 3, 5, 5, 5, 4, 3, 2, 4, 5, 2, 4, 5]
percent = school_marks.count(int(input())) / len(school_marks) * 100
print("{:.1f}".format(percent) + "%")
