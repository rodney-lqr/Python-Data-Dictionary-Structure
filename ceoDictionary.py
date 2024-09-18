companyCeos = {
    'Apple': 'Tim Cook',
    'Google': 'Sundar Pichai',
    'Microsoft': 'Satya Nadella',
    'Amazon': 'Andy Jassy',
    'Tesla': 'Elon Musk',
    'Facebook': 'Mark Zuckerberg',
    'IBM': 'Arvind Krishna',
    'Oracle': 'Safra Catz',
    'Salesforce': 'Marc Benioff',
    'Netflix': 'Ted Sarandos'
}
print()
print(companyCeos)
print()
print("CEO of sixth company:", companyCeos['Facebook'])
print()
companyCeos['Microsoft'] = 'Bill Gates'
print()
del companyCeos['Salesforce']
print()
print("Last key-value pair:", list(companyCeos.items())[-1])
print()