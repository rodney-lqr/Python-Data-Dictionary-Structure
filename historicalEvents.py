historicalEvents = {
    'Fall of the Berlin Wall': 1989,
    'Moon Landing': 1969,
    'Declaration of Independence': 1776,
    'World War II End': 1945,
    'French Revolution': 1789,
    'Renaissance Period': 1400,
    '9/11 Attacks': 2001,
    'COVID-19 Pandemic': 2020
}
print()
print(historicalEvents)
print()
print("Year of second event:", historicalEvents['Moon Landing'])
print()
historicalEvents['9/11 Attacks'] = 2000
print()
del historicalEvents['French Revolution']
print()
print("Last key-value pair:", list(historicalEvents.items())[-1])
print()