# Write your code here
import re

def correct_dates(string):
    return re.sub(r'(\w+)/(\w+)/(\w+)', r'\2/\1/\3', string)