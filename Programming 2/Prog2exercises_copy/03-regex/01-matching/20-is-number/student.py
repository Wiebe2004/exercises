# Write your code here
import re

def is_number(string):
    return re.search("^-?[0-9]+(\\.?[0-9])*$", string)

    # Other possibility:
    # return re.fullmatch("^[0-9]+(\\.[0-9]+)?$", string)
