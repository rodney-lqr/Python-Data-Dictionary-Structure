riverLengths = {
    'Nile': 6650,
    'Amazon': 6400,
    'Yangtze': 6300,
    'Mississippi': 3730,
    'Yenisei': 5539,
    'Yellow River': 5464
}
print()
print(riverLengths)
print()
print("Length of second river:", riverLengths['Amazon'])
print()
riverLengths['Yenisei'] = 5540
print()
del riverLengths['Mississippi']
print()
print("Last key-value pair:", list(riverLengths.items())[-1])
print()