import re

def parse_time(string):
    match = re.fullmatch(r"(\d{2}):(\d{2}):(\d{2})(\.\d{3})?", string)

    if (match):
        h, m, s, ms = match.groups('.000')
        
        return int(h), int(m), int(s), int(ms[1:]) if ms else 0
    
# slicing is key here, been a while lol
    