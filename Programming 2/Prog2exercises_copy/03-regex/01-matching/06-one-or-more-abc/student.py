# Write your code here
import re

def one_or_more_abc(string):
    if re.fullmatch("(abc)+", string):
        return string