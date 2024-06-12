from abc import ABC, abstractmethod


class PhoneNumber(ABC):

    """
    Abstract base class for defining phone number behaviour.
    """

    def __init__(self):
        self._phone_number = None
        self._number_type = None

    @property
    def phone_number(self):
        """
        Get the phone number.
        :return:
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        """
        Set the phone number after validation.
        :param value:
        :return:
        """
        self._phone_number = value

    @property
    def number_type(self):
        """
        Get the type of the phone number.
        :return:
        """
        return self._number_type

    @abstractmethod
    def validate_phone_number(self, number):
        """
        Validate the phone number format.
        :param number:
        :return:
        """
        pass

