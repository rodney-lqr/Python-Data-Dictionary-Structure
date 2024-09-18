productPrices = {
    'Laptop': 999.99,
    'Smartphone': 699.99,
    'Tablet': 299.99,
    'Headphones': 149.99,
    'Smartwatch': 199.99,
    'Camera': 499.99,
    'TV': 799.99,
    'Refrigerator': 1200.00,
    'Microwave': 100.00,
    'Washing Machine': 700.00
}
print()
print(productPrices)
print()
print("Price of fourth product:", productPrices['Headphones'])
print()
productPrices['Microwave'] = 120.00
print()
del productPrices['Camera']
print()
print("Last key-value pair:", list(productPrices.items())[-1])
print()
print()