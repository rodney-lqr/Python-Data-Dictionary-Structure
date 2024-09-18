spaceMissions = {
    'Apollo 11': 1969,
    'Voyager 1': 1977,
    'Mars Rover': 2004,
    'Hubble Telescope': 1990,
    'Cassini': 1997
}
print()
print(spaceMissions)
print()
print("Year of third mission:", spaceMissions['Mars Rover'])
print()
spaceMissions['Voyager 1'] = 1978
print()
del spaceMissions['Hubble Telescope']
print()
print("Last key-value pair:", list(spaceMissions.items())[-1])
print()