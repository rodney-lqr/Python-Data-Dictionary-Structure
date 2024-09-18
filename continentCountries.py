continentCountries = {
    'Africa': ['Nigeria', 'Kenya', 'South Africa'],
    'Asia': ['China', 'India', 'Japan'],
    'Europe': ['France', 'Germany', 'Italy'],
    'North America': ['USA', 'Canada', 'Mexico'],
    'South America': ['Brazil', 'Argentina', 'Chile'],
    'Australia': ['Australia', 'New Zealand', 'Fiji']
}
print()
print(continentCountries)
print()
print("Countries of fourth continent:", continentCountries['North America'])
print()
continentCountries['South America'] = ['Colombia', 'Peru', 'Venezuela']
print()
del continentCountries['Australia']
print()
print("Last key-value pair:", list(continentCountries.items())[-1])
print()