carSpecs = {
    'Toyota Camry': '2.5L 4-cylinder',
    'Ford Mustang': '5.0L V8',
    'Honda Accord': '1.5L turbo',
    'Chevrolet Camaro': '6.2L V8',
    'Tesla Model S': 'Electric',
    'BMW 3 Series': '2.0L 4-cylinder',
    'Audi A4': '2.0L 4-cylinder',
    'Mercedes C-Class': '2.0L 4-cylinder',
    'Porsche 911': '3.0L turbocharged flat-6',
    'Lexus RX': '3.5L V6'
}
print()
print(carSpecs)
print()
print("Specifications of fourth car model:", carSpecs['Chevrolet Camaro'])
print()
carSpecs['Porsche 911'] = '4.0L flat-6'
print()
del carSpecs['Tesla Model S']
print()
print("Last key-value pair:", list(carSpecs.items())[-1])
print()
print()