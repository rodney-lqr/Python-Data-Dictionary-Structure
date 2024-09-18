dinosaurFossils = {
    'Tyrannosaurus Rex': 'North America',
    'Stegosaurus': 'Western United States',
    'Triceratops': 'Montana, USA',
    'Velociraptor': 'Mongolia',
    'Brachiosaurus': 'Tanzania',
    'Spinosaurus': 'North Africa',
    'Diplodocus': 'Colorado, USA'
}
print()
print(dinosaurFossils)
print()
print("Fossil location of fourth dinosaur:", dinosaurFossils['Velociraptor'])
print()
dinosaurFossils['Stegosaurus'] = 'Utah, USA'
print()
del dinosaurFossils['Spinosaurus']
print()
print("Last key-value pair:", list(dinosaurFossils.items())[-1])
print()
print()