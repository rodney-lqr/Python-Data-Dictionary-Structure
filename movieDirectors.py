movieDirectors = {
    'Inception': 'Christopher Nolan',
    'Titanic': 'James Cameron',
    'Pulp Fiction': 'Quentin Tarantino',
    'The Godfather': 'Francis Ford Coppola',
    'The Dark Knight': 'Christopher Nolan',
    'Avatar': 'James Cameron',
    'Interstellar': 'Christopher Nolan',
    'Fight Club': 'David Fincher',
    'The Matrix': 'Lana Wachowski, Lilly Wachowski',
    'The Shawshank Redemption': 'Frank Darabont'
}
print()
print(movieDirectors)
print()
print("Director of fifth movie:", list(movieDirectors.values())[4])
print()
movieDirectors['The Matrix'] = 'Wachowski Sisters'
print()
del movieDirectors['Interstellar']
print()
print("Last key-value pair:", list(movieDirectors.items())[-1])
print()