phoneModels = {
    'iPhone 13': 'Apple',
    'Galaxy S21': 'Samsung',
    'Pixel 6': 'Google',
    'OnePlus 9': 'OnePlus',
    'Xperia 5': 'Sony',
    'Mi 11': 'Xiaomi',
    'P40': 'Huawei',
    'Moto G Power': 'Motorola',
    'Redmi Note 10': 'Xiaomi',
    'Oppo Reno 6': 'Oppo'
}
print()
print(phoneModels)
print()
print("Manufacturer of second phone model:", phoneModels['Galaxy S21'])
print()
phoneModels['Moto G Power'] = 'Lenovo'
print()
del phoneModels['Mi 11']
print()
print("Last key-value pair:", list(phoneModels.items())[-1])
print()
print()