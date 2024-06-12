# Write your code here
import re

def three_to_ten_times_abc(string):
    if re.fullmatch("(abc){3,7}", string):
        return string