fruitColors = {
    'Apple': 'Red',
    'Banana': 'Yellow',
    'Grapes': 'Purple',
    'Orange': 'Orange',
    'Blueberry': 'Blue',
    'Watermelon': 'Green',
    'Strawberry': 'Red',
    'Lemon': 'Yellow'
}
print()
print(fruitColors)
print()
print("Color of sixth fruit:", list(fruitColors.values())[5])
print()
fruitColors['Orange'] = 'Yellow-Orange'
print()
del fruitColors['Strawberry']
print()
print("Last key-value pair:", list(fruitColors.items())[-1])
print()