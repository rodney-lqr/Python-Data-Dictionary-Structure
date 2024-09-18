plantTypes = {
    'Rose': 'Shrub',
    'Oak': 'Tree',
    'Basil': 'Herb',
    'Sunflower': 'Flower',
    'Pine': 'Tree',
    'Cactus': 'Succulent',
    'Tulip': 'Flower',
    'Mint': 'Herb'
}
print()
print(plantTypes)
print()
print("Type of fifth plant:", plantTypes['Pine'])
print()
plantTypes['Oak'] = 'Shrub'
print()
del plantTypes['Cactus']
print()
print("Last key-value pair:", list(plantTypes.items())[-1])
print()
print()