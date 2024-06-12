def find(books, condition):
    for book in books:
        if condition(book):
            return book
    return None