# Write your code here
import re

def is_dna(string):
    return re.fullmatch("[G|A|T|C]*", string)