import re

def is_valid_name(name):
    return bool(re.fullmatch("[A-Za-z]+( [A-Za-z]+)+", name))

print(is_valid_name("Machine Gun Kelly Bond"))