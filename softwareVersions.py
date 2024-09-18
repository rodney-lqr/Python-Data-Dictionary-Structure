softwareVersions = {
    'Windows': '11.0',
    'macOS': '12.3',
    'Ubuntu': '22.04',
    'Photoshop': '23.1',
    'Chrome': '104.0',
    'Firefox': '100.0'
}
print()
print(softwareVersions)
print()
print("Version of fourth software:", softwareVersions['Photoshop'])
print()
softwareVersions['macOS'] = '12.4'
print()
del softwareVersions['Chrome']
print()
print("Last key-value pair:", list(softwareVersions.items())[-1])
print()