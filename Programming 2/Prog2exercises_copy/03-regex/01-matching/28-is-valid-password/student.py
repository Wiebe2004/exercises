# Write your code here
import re

def is_valid_password(string):

    if re.search(r"(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*\W).{12,}", string):
        if not re.search(r"(.)\1{2,}", string) and not re.search(r"(.*(.).*\2*\2.*\2)", string):
            return True
    return False