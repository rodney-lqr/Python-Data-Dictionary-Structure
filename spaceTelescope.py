spaceTelescopes = {
    'Hubble': 'Study distant galaxies',
    'James Webb': 'Observe infrared light from the early universe',
    'Chandra': 'X-ray observations of black holes',
    'Kepler': 'Search for exoplanets',
    'Spitzer': 'Infrared study of space objects'
}
print()
print(spaceTelescopes)
print()
print("Mission of third telescope:", spaceTelescopes['Chandra'])
print()
spaceTelescopes['Hubble'] = 'Explore deep space and star formation'
print()
del spaceTelescopes['Kepler']
print()
print("Last key-value pair:", list(spaceTelescopes.items())[-1])
print()
print()