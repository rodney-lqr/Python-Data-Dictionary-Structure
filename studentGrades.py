studentsGrades = {
    "Alice": 'A',
    "Bob": 'B',
    "Charlie": 'B+',
    "David": 'A-',
    "Eve": 'D'
}
print()
print(studentsGrades["Alice"])
print()
studentsGrades["Bob"] = "A"
print(studentsGrades["Bob"])
print()
del studentsGrades["Eve"]

last_key = list(studentsGrades.keys())[-1]
print(last_key, studentsGrades[last_key])
print()