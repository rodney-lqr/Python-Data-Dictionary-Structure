elementSymbols = {
    'Hydrogen': 'H',
    'Helium': 'He',
    'Lithium': 'Li',
    'Beryllium': 'Be',
    'Boron': 'B',
    'Carbon': 'C',
    'Nitrogen': 'N',
    'Oxygen': 'O',
    'Fluorine': 'F',
    'Neon': 'Ne'
}
print()
print(elementSymbols)
print()
print("Symbol of sixth element:", list(elementSymbols.values())[5])
print()
elementSymbols['Oxygen'] = 'O2'
print()
del elementSymbols['Fluorine']
print()
print("Last key-value pair:", list(elementSymbols.items())[-1])
print()