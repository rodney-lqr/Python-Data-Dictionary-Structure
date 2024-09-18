festivalDates = {
    'Christmas': '25th December',
    'Diwali': '4th November',
    'Eid al-Fitr': '13th May',
    'Hanukkah': '28th November',
    'Thanksgiving': '25th November',
    'New Year\'s Eve': '31st December',
    'Holi': '29th March',
    'Easter': '4th April',
    'Ramadan': '12th April',
    'Halloween': '31st October'
}
print()
print(festivalDates)
print()
print("Date of third festival:", festivalDates['Eid al-Fitr'])
print()
festivalDates['Holi'] = '18th March'
print()
del festivalDates['Thanksgiving']
print()
print("Last key-value pair:", list(festivalDates.items())[-1])
print()