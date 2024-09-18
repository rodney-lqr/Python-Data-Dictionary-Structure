authorBooks = {
    'J.K. Rowling': 'Harry Potter',
    'George Orwell': '1984',
    'J.R.R. Tolkien': 'The Lord of the Rings',
    'Agatha Christie': 'Murder on the Orient Express',
    'Mark Twain': 'The Adventures of Tom Sawyer',
    'F. Scott Fitzgerald': 'The Great Gatsby',
    'Ernest Hemingway': 'The Old Man and the Sea',
    'Leo Tolstoy': 'War and Peace'
}
print()
print(authorBooks)
print()
print("Book of fifth author:", authorBooks['Mark Twain'])
print()
authorBooks['Ernest Hemingway'] = 'A Farewell to Arms'
print()
del authorBooks['F. Scott Fitzgerald']
print()
print("Last key-value pair:", list(authorBooks.items())[-1])
print()
print()