# import pytest
# from book import Book

# VALID_ISBNS = [
#     '9781779501127',
#     '9780735611313',
#     '9781593275990',
# ]

# VALID_TITLES = [
#     'a',
#     'b',
#     'xyz',
# ]


# @pytest.mark.parametrize('title', VALID_TITLES)
# @pytest.mark.parametrize('isbn', VALID_ISBNS)

import pytest
from book import Book

VALID_ISBNS = [
    '9781779501127',
    '9780735611313',
    '9781593275990',
]

VALID_TITLES = [
    'a',
    'b',
    'xyz',
]

INVALID_TITLES = [
    '',  # Empty title
]

INVALID_ISBNS = [
    '9781779501128',  # Invalid checksum
    '978073561131',   # Too short
    '97807356113135', # Too long
    '1234567890123',  # Invalid checksum
]

@pytest.mark.parametrize('title', VALID_TITLES)
@pytest.mark.parametrize('isbn', VALID_ISBNS)
def test_valid_creation(title, isbn):
    book = Book(title, isbn)
    assert book.title == title
    assert book.isbn == isbn

@pytest.mark.parametrize('title', INVALID_TITLES)
@pytest.mark.parametrize('isbn', VALID_ISBNS)
def test_creation_with_invalid_title(title, isbn):
    with pytest.raises(RuntimeError, match="Title is not valid"):
        Book(title, isbn)

@pytest.mark.parametrize('title', VALID_TITLES)
@pytest.mark.parametrize('isbn', INVALID_ISBNS)
def test_creation_with_invalid_isbn(title, isbn):
    with pytest.raises(RuntimeError, match="ISBN is not valid"):
        Book(title, isbn)
