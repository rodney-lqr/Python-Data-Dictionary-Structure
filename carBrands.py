car_brands = {
    'Toyota': 'Japan',
    'Ford': 'USA',
    'BMW': 'Germany',
    'Mercedes': 'Germany',
    'Honda': 'Japan',
    'Chevrolet': 'USA',
    'Hyundai': 'South Korea',
    'Tesla': 'USA',
    'Volkswagen': 'Germany',
    'Ferrari': 'Italy'
}

print()
print(car_brands)
print()
print("Country of origin of third brand:", list(car_brands.values())[2])
print()
car_brands['Hyundai'] = 'South Korea'
print()
del car_brands['Tesla']
print()
print("Last key-value pair:", list(car_brands.items())[-1])
print()