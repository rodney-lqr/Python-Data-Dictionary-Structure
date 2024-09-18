
animal_sounds = {
    'Cat': 'Meow',
    'Dog': 'Bark',
    'Cow': 'Moo',
    'Sheep': 'Baa',
    'Lion': 'Roar',
    'Elephant': 'Trumpet',
    'Snake': 'Hiss',
    'Duck': 'Quack'
}
print()
print(animal_sounds)
print()
print("Sound of fourth animal:", list(animal_sounds.values())[3])
print()
animal_sounds['Snake'] = 'Sssss'
print()
del animal_sounds['Lion']
print()
print("Last key-value pair:", list(animal_sounds.items())[-1])
print()