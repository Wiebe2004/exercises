import itertools


class Book:
    def __init__(self, title, isbn):
        if not Book._is_valid_title(title):
            raise RuntimeError("Title is not valid")

        if not Book._is_valid_isbn(isbn):
            raise RuntimeError("ISBN is not valid")
        self.__title = title
        self.__isbn = isbn

    @property
    def title(self):
        return self.__title

    @property
    def isbn(self):
        return self.__isbn

    @staticmethod
    def _is_valid_title(title):
        return len(title) > 0

    @staticmethod
    def _is_valid_isbn(isbn):
        digits = [int(char) for char in isbn if "0" <= char <= "9"]
        if len(digits) != 13:
            return False
        weighted_sum = sum(
            digit * weight for digit, weight in zip(digits, itertools.cycle([1, 3]))
        )
        return weighted_sum % 10 == 0
