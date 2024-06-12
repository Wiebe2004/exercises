# Write your code here
import re

def two_or_more_abc(string):
    if re.fullmatch("(abc)(abc)+", string):
        return string