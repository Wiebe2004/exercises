# Write your code here
def contains_duplicates(xs):

    for duplicate in xs:
        if xs.count(duplicate) > 1:
            return True
    return False