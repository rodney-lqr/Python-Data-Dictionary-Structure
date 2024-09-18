booksAuthors = {
    '1984': 'George Orwell',
    'To Kill a Mockingbird': 'Harper Lee',
    'Pride and Prejudice': 'Jane Austen',
    'The Great Gatsby': 'F. Scott Fitzgerald',
    'Moby Dick': 'Herman Melville',
    'War and Peace': 'Leo Tolstoy',
    'The Catcher in the Rye': 'J.D. Salinger',
    'Crime and Punishment': 'Fyodor Dostoevsky',
    'The Lord of the Rings': 'J.R.R. Tolkien',
    'The Hobbit': 'J.R.R. Tolkien',
    'Ulysses': 'James Joyce',
    'Brave New World': 'Aldous Huxley'
}
print()
print(booksAuthors)
print()
print("Author of ninth book:", list(booksAuthors.values())[8])
print()
booksAuthors['Moby Dick'] = 'Mark Twain'
print()
del booksAuthors['Pride and Prejudice']
print()
print("Last key-value pair:", list(booksAuthors.items())[-1])
print()