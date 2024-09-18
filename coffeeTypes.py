coffeeTypes = {
    'Espresso': 'Strong coffee brewed by forcing steam through ground coffee beans',
    'Latte': 'Espresso with steamed milk and a small layer of foam',
    'Cappuccino': 'Equal parts espresso, steamed milk, and foam',
    'Americano': 'Espresso with added hot water',
    'Macchiato': 'Espresso with a small amount of milk or foam',
    'Mocha': 'Espresso mixed with chocolate syrup and steamed milk',
    'Flat White': 'Espresso with steamed milk and no foam',
    'Affogato': 'Espresso poured over a scoop of ice cream',
    'Cortado': 'Equal parts espresso and steamed milk',
    'Irish Coffee': 'Coffee with whiskey and sugar, topped with cream'
}
print()
print(coffeeTypes)
print()
print("Description of fourth coffee:", coffeeTypes['Americano'])
print()
coffeeTypes['Affogato'] = 'Espresso poured over vanilla ice cream'
print()
del coffeeTypes['Macchiato']
print()
print("Last key-value pair:", list(coffeeTypes.items())[-1])
print()