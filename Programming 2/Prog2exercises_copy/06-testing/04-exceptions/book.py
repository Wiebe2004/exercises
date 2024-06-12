class Book:
    def __init__(self, title, isbn):
        if title == "":
            raise RuntimeError("Title must not be empty")
        if not self.validate_isbn(isbn):
            raise RuntimeError("Invalid ISBN")
        self._title = title
        self._isbn = isbn

    @property
    def title(self):
        return self._title
    
    @property
    def isbn(self):
        return self._isbn
    
    def validate_isbn(self, isbn):
        digits = ''.join(c for c in isbn if c.isdigit())
        if len(digits) != 13:
            return False
        digits = list(map(int, digits))
        checksum_digits = [digit * 3 if i % 2 else digit for i, digit in enumerate(digits)]
        return sum(checksum_digits) % 10 == 0