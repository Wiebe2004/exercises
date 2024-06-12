# Write your code here
import re

def ababa(string):
    return re.fullmatch(r"(.+)(.+)\2", string)