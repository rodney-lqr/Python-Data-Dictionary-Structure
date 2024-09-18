dogBreeds = {
    'Labrador Retriever': 'Large',
    'Beagle': 'Medium',
    'Bulldog': 'Medium',
    'Poodle': 'Small',
    'German Shepherd': 'Large',
    'Dachshund': 'Small',
    'Golden Retriever': 'Large',
    'Shih Tzu': 'Small',
    'Chihuahua': 'Small',
    'Great Dane': 'Large'
}
print()
print(dogBreeds)
print()
print("Size of fifth breed:", dogBreeds['German Shepherd'])
print()
dogBreeds['Shih Tzu'] = 'Medium'
print()
del dogBreeds['Dachshund']
print()
print("Last key-value pair:", list(dogBreeds.items())[-1])
print()
print()