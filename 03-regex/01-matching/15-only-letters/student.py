# Write your code here
import re
def only_letters(string):
    return re.fullmatch('[(a-z)|(A-Z)]*',string)
# '[a-zA-Z]*' kan ook