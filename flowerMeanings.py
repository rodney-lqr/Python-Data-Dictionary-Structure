flowerMeanings = {
    'Rose': 'Love',
    'Lily': 'Purity',
    'Tulip': 'Perfect Love',
    'Daisy': 'Innocence',
    'Sunflower': 'Adoration',
    'Orchid': 'Strength',
    'Lavender': 'Serenity',
    'Carnation': 'Admiration'
}
print()
print(flowerMeanings)
print()
print("Meaning of fifth flower:", flowerMeanings['Sunflower'])
print()
flowerMeanings['Lavender'] = 'Calmness'
print()
del flowerMeanings['Orchid']
print()
print("Last key-value pair:", list(flowerMeanings.items())[-1])
print()