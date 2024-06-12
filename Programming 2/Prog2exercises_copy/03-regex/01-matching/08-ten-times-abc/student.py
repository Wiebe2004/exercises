# Write your code here
import re

def ten_times_abc(string):
    if re.fullmatch("(abc){10}", string):
        return string