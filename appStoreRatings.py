appStoreRatings = {
    'Instagram': 4.5,
    'Facebook': 3.8,
    'WhatsApp': 4.7,
    'TikTok': 4.2,
    'Snapchat': 3.9,
    'Spotify': 4.8,
    'YouTube': 4.6,
    'Netflix': 4.4,
    'Zoom': 4.3,
    'Discord': 4.6
}
print()
print(appStoreRatings)
print()
print("Rating of sixth app:", appStoreRatings['Spotify'])
print()
appStoreRatings['Netflix'] = 4.5
print()
del appStoreRatings['Zoom']
print()
print("Last key-value pair:", list(appStoreRatings.items())[-1])
print()