animalHabitats = {
    'Lion': 'Savannah',
    'Polar Bear': 'Arctic',
    'Kangaroo': 'Grasslands',
    'Elephant': 'Forests',
    'Penguin': 'Antarctica',
    'Wolf': 'Tundra',
    'Shark': 'Ocean',
    'Gorilla': 'Rainforest'
}
print()
print(animalHabitats)
print()
print("Habitat of third animal:", animalHabitats['Kangaroo'])
print()
animalHabitats['Penguin'] = 'Cold Coastal Regions'
print()
del animalHabitats['Shark']
print()
print("Last key-value pair:", list(animalHabitats.items())[-1])
print()