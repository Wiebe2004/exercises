import re


def contains_three_digits(string):
    return re.fullmatch('.*[0-9].*[0-9].*[0-9].*', string)


print(contains_three_digits('alle3goefdfsf524dfsdf'))