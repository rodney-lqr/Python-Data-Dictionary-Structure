stateCapitals = {
    'California': 'Sacramento',
    'Texas': 'Austin',
    'New York': 'Albany',
    'Florida': 'Tallahassee',
    'Illinois': 'Springfield',
    'Ohio': 'Columbus',
    'Georgia': 'Atlanta',
    'Michigan': 'Lansing',
    'Pennsylvania': 'Harrisburg',
    'Washington': 'Olympia'
}
print()
print(stateCapitals)
print()
print("Capital of fourth state:", stateCapitals['Florida'])
print()
stateCapitals['Pennsylvania'] = 'Philadelphia'
print()
del stateCapitals['Georgia']
print()
print("Last key-value pair:", list(stateCapitals.items())[-1])
print()
print()