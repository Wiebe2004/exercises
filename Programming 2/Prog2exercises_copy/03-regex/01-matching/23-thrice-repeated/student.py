# Write your code here
import re

def thrice_repeated(string):
    return re.fullmatch(r'(.+)\1\1', string)

# r at the start denotes a raw string. In raw strings, 
# backslashes are treated as literal characters and not as escape characters. 
# This is often used with regular expressions because they frequently contain backslashes.

# '(.+)\1\1' is the regular expression pattern.

# . matches any character except a newline.

# + is a quantifier that means "one or more" of the preceding element.

# () is a group. Everything matched inside the parentheses can be referred to later.

# \1 is a backreference that refers to the contents of the first group.

# So, the regular expression r'(.+)\1\1' matches any string that contains a 
# sequence of one or more characters repeated three times in a row. 
# For example, it would match 'abcabcabc' or '111'.