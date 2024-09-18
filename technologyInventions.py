technologyInventors = {
    'Telephone': 'Alexander Graham Bell',
    'Light Bulb': 'Thomas Edison',
    'Airplane': 'Wright Brothers',
    'Computer': 'Charles Babbage',
    'Internet': 'Vint Cerf',
    'Radio': 'Guglielmo Marconi'
}
print()
print(technologyInventors)
print()
print("Inventor of fourth technology:", technologyInventors['Computer'])
print()
technologyInventors['Light Bulb'] = 'Nikola Tesla'
print()
del technologyInventors['Radio']
print()
print("Last key-value pair:", list(technologyInventors.items())[-1])
print()