# Write your code here
import re

def is_valid_email_address(string):
    return re.search(r"[\w]*(\.)?[\w]*(@{1})(student\.)?(ucll\.be)$", string)