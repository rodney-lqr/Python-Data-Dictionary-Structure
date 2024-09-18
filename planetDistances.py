planetDistances = {
    'Mercury': 57.9,
    'Venus': 108.2,
    'Earth': 149.6,
    'Mars': 227.9,
    'Jupiter': 778.5,
    'Saturn': 1433.5,
    'Uranus': 2871.0,
    'Neptune': 4497.1
}
print()
print(planetDistances)
print()
print("Distance of third planet:", planetDistances['Earth'])
print()
planetDistances['Jupiter'] = 780.0
print()
del planetDistances['Uranus']
print()
print("Last key-value pair:", list(planetDistances.items())[-1])
print()