companyFounders = {
    'Apple': 'Steve Jobs',
    'Microsoft': 'Bill Gates',
    'Google': 'Larry Page',
    'Amazon': 'Jeff Bezos',
    'Facebook': 'Mark Zuckerberg',
    'Tesla': 'Elon Musk',
    'SpaceX': 'Elon Musk',
    'Netflix': 'Reed Hastings'
}
print()
print(companyFounders)
print()
print("Founder of sixth company:", companyFounders['Tesla'])
print()
companyFounders['Microsoft'] = 'Paul Allen'
print()
del companyFounders['Netflix']
print()
print("Last key-value pair:", list(companyFounders.items())[-1])
print()
print()