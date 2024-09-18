universityCourses = {
    'Harvard': 'Law',
    'MIT': 'Computer Science',
    'Stanford': 'Business',
    'Oxford': 'Philosophy',
    'Cambridge': 'Engineering',
    'Caltech': 'Physics',
    'Yale': 'Political Science',
    'Princeton': 'Mathematics'
}
print()
print(universityCourses)
print()
print("Course of third university:", universityCourses['Stanford'])
print()
universityCourses['Cambridge'] = 'Artificial Intelligence'
print()
del universityCourses['Yale']
print()
print("Last key-value pair:", list(universityCourses.items())[-1])
print()