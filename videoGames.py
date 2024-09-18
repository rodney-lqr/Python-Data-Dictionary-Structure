videoGamePlatforms = {
    'The Legend of Zelda': 'Nintendo Switch',
    'Fortnite': 'PlayStation 4',
    'Minecraft': 'PC',
    'Call of Duty': 'Xbox One',
    'GTA V': 'PC',
    'Among Us': 'Mobile',
    'League of Legends': 'PC',
    'FIFA 21': 'PlayStation 4'
}
print()
print(videoGamePlatforms)
print()
print("Platform of second video game:", videoGamePlatforms['Fortnite'])
print()
videoGamePlatforms['Among Us'] = 'PC'
print()
del videoGamePlatforms['Call of Duty']
print()
print("Last key-value pair:", list(videoGamePlatforms.items())[-1])
print()