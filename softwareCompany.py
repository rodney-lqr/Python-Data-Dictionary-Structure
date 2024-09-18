softwareCompanies = {
    'Microsoft': 'Redmond, WA',
    'Google': 'Mountain View, CA',
    'Apple': 'Cupertino, CA',
    'Amazon': 'Seattle, WA',
    'Facebook': 'Menlo Park, CA',
    'IBM': 'Armonk, NY',
    'Oracle': 'Austin, TX',
    'Salesforce': 'San Francisco, CA',
    'Adobe': 'San Jose, CA',
    'Intel': 'Santa Clara, CA'
}
print()
print(softwareCompanies)
print()
print("Headquarters of third company:", list(softwareCompanies.values())[2])
print()
softwareCompanies['Salesforce'] = 'Los Angeles, CA'
print()
del softwareCompanies['Adobe']
print()
print("Last key-value pair:", list(softwareCompanies.items())[-1])
print()