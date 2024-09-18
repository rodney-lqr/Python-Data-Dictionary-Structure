city_population = {
    'New York': 8419600,
    'Los Angeles': 3980400,
    'Chicago': 2716000,
    'Houston': 2328000,
    'Phoenix': 1690000,
    'Philadelphia': 1584200,
    'San Antonio': 1547200,
    'San Diego': 1423851,
    'Dallas': 1356000,
    'San Jose': 1035200
}
print()
print(city_population)
print()
print("Population of sixth city:", list(city_population.values())[5])
print()
city_population['Chicago'] = 2800000
print()
del city_population['Dallas']
print()
print("Last key-value pair:", list(city_population.items())[-1])
print()