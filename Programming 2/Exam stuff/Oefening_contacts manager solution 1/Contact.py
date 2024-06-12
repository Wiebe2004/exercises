import re


class Contact:
    """
    Represents a contact with name, email, and phone numbers.
    """

    def __init__(self, name, email, numbers):
        self.name = name
        self.email = email
        self.numbers = numbers

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("The name should have at least 1 character!")
        self._name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        valid_email = re.fullmatch(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.[a-z]+', value) is not None
        if valid_email:
            self._email = value
        else:
            raise ValueError('Invalid email!')

    @property
    def numbers(self):
        return self._numbers

    @numbers.setter
    def numbers(self, value):
        if not value:
            raise ValueError("At least one phone number must be provided!")
        self._numbers = value

    def __repr__(self):
        return f"name = {self.name}, email = {self.email}, numbers = {self.numbers}"
