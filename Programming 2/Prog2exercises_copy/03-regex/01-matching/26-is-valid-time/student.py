# Write your code here
import re

def is_valid_time(string):
    return re.search(r'^([01]\d|2[0-3]):([0-5]\d):([0-5]\d)(\.\d{3})?$', string)

# ([01]\d|2[0-3]) matches the hour part, from 00 to 19 & 20 to 23.
# ([0-5]\d):([0-5]\d) is pretty clear, minutes & seconds.
# (\.\d{3}) will match any sequence of a period followed by exactly 3 digits.
# the ? makes the group optional at the end. The "?" helps you for optional regex!