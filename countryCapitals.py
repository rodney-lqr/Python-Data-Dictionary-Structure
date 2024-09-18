countryCapitals = {
    'USA': 'Washington, D.C.',
    'Canada': 'Ottawa',
    'UK': 'London',
    'France': 'Paris',
    'Germany': 'Berlin',
    'Italy': 'Rome',
    'Japan': 'Tokyo',
    'China': 'Beijing',
    'India': 'New Delhi',
    'Russia': 'Moscow',
    'Brazil': 'Brasilia',
    'Australia': 'Canberra'
}
print()
print(countryCapitals)
print()
print("Capital of fifth country:", list(countryCapitals.values())[4])
print()
countryCapitals['China'] = 'Shanghai'
print()
del countryCapitals['Brazil']
print()
print("Last key-value pair:", list(countryCapitals.items())[-1])
print()