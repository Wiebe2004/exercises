def group_by(xs, key_function):
    bruh = {}
    for x in xs:
        key = key_function(x)
        if key not in bruh:
            bruh[key] = []
        bruh[key].append(x)
    return bruh

# Need to review dictionaries for this..
# we are basically appending every x found in xs
# as a key to our new dictionary "bruh".