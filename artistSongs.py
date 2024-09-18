artistSongs = {
    'Taylor Swift': 'Love Story',
    'Ed Sheeran': 'Shape of You',
    'Adele': 'Hello',
    'Drake': 'God’s Plan',
    'Beyoncé': 'Halo',
    'Bruno Mars': 'Uptown Funk',
    'Billie Eilish': 'Bad Guy',
    'The Weeknd': 'Blinding Lights'
}
print()
print(artistSongs)
print()
print("Top song of third artist:", artistSongs['Adele'])
print()
artistSongs['Bruno Mars'] = 'Just the Way You Are'
print()
del artistSongs['Billie Eilish']
print()
print("Last key-value pair:", list(artistSongs.items())[-1])
print()
print()