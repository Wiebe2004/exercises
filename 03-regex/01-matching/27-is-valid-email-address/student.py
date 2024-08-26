# Write your code here
import re


def is_valid_email_address(string):
    return re.fullmatch(r'[a-z0-9.]+@(student\.)?ucll\.be', string) #Solution version. Which makes use of ? to clarify that "student." is optional but "ucll.be" is necesary.
    # return re.fullmatch("([a-z0-9.])+@(ucll.be|student.ucll.be)", string)
