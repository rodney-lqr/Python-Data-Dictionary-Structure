holidayDates = {
    'New Year': 'January 1',
    'Independence Day': 'July 4',
    'Christmas': 'December 25',
    'Thanksgiving': 'November 23',
    'Labor Day': 'September 5',
    'Halloween': 'October 31',
    'Valentine\'s Day': 'February 14',
    'Easter': 'April 17',
    'Memorial Day': 'May 30',
    'Veterans Day': 'November 11'
}
print()
print(holidayDates)
print()
print("Date of fourth holiday:", holidayDates['Thanksgiving'])
print()
holidayDates['Memorial Day'] = 'May 31'
print()
del holidayDates['Independence Day']
print()
print("Last key-value pair:", list(holidayDates.items())[-1])
print()