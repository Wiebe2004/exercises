def merge_dictionaries(d1, d2, merge_function):
    new = {}
    for k in set(d1.keys()).union(d2.keys()):
        if k in d1 and k in d2:
            new[k] = merge_function(d1[k], d2[k])
        elif k in d1:
            new[k] = d1[k]
        else:
            new[k] = d2[k]
            
    return new

# you basically make a union of the 2 dictionaries into 1 set.
# you loop through the set, by checking if "k" is in d1 & d2.
# if they are, you merge the same "k" into the "new" set.
# else, the k from d1/d2 gets added within the "new" set.