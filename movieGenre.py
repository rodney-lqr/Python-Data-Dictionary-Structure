movieGenres = {
    'Action': 'Mad Max: Fury Road',
    'Drama': 'The Godfather',
    'Comedy': 'Superbad',
    'Horror': 'The Exorcist',
    'Science Fiction': 'Blade Runner',
    'Fantasy': 'The Lord of the Rings',
    'Romance': 'The Notebook',
    'Thriller': 'Inception'
}
print()
print(movieGenres)
print()
print("Example movie of third genre:", movieGenres['Comedy'])
print()
movieGenres['Science Fiction'] = 'Interstellar'
print()
del movieGenres['Romance']
print()
print("Last key-value pair:", list(movieGenres.items())[-1])
print()