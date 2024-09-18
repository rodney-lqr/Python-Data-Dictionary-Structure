jobSalaries = {
    'Software Engineer': '$120,000',
    'Data Scientist': '$130,000',
    'Product Manager': '$110,000',
    'Marketing Manager': '$90,000',
    'Graphic Designer': '$65,000',
    'Accountant': '$70,000',
    'Doctor': '$200,000',
    'Teacher': '$50,000',
    'Lawyer': '$150,000',
    'Nurse': '$80,000'
}
print()
print(jobSalaries)
print()
print("Salary of third job:", jobSalaries['Product Manager'])
print()
jobSalaries['Doctor'] = '$210,000'
print()
del jobSalaries['Lawyer']
print()
print("Last key-value pair:", list(jobSalaries.items())[-1])
print()
print()