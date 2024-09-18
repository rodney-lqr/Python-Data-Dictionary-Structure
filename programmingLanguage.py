
programmingLanguages = {
    'Python': 'Guido van Rossum',
    'Java': 'James Gosling',
    'C': 'Dennis Ritchie',
    'JavaScript': 'Brendan Eich',
    'C++': 'Bjarne Stroustrup',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf'
}
print()
print(programmingLanguages)
print()
print("Developer of fourth language:", programmingLanguages['JavaScript'])
print()
programmingLanguages['Ruby'] = 'Matz'
print()
del programmingLanguages['Java']
print()
print("Last key-value pair:", list(programmingLanguages.items())[-1])
print()