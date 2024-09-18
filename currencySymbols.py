currencySymbols = {
    'US Dollar': '$',
    'Euro': '€',
    'British Pound': '£',
    'Japanese Yen': '¥',
    'Indian Rupee': '₹',
    'Australian Dollar': 'A$',
    'Canadian Dollar': 'C$',
    'Swiss Franc': 'CHF',
    'Chinese Yuan': '¥',
    'Russian Ruble': '₽'
}
print()
print(currencySymbols)
print()
print("Symbol of fifth currency:", currencySymbols['Indian Rupee'])
print()
currencySymbols['Chinese Yuan'] = 'C¥'
print()
del currencySymbols['British Pound']
print()
print("Last key-value pair:", list(currencySymbols.items())[-1])
print()
print()
