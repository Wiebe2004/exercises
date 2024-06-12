import re

from PhoneNumber import PhoneNumber


class MobilePhone(PhoneNumber):
    """
    Represents a mobile phone number.
    """

    def __init__(self):
        super().__init__()
        self._number_type = "mobile"

    def validate_phone_number(self, number):
        """
        Validate a mobile phone number. Supports both local formats.
        :param number:
        :return:
        """
        return re.fullmatch(r'(^04\d{8}$)|(^(\+32|0032)4\d{8}$)', number) is not None

