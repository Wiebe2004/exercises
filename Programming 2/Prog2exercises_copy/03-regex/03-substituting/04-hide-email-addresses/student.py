# Write your code here
import re

def hide_email_addresses(string):
    def n(match):
        return '*' * len(match.group())

    return re.sub(r'[\w.-]+@[\w.-]+', n, string)