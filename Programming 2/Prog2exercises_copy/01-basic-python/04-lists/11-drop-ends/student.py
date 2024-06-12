# Write your code here
def drop_ends(xs):
    del xs[:-1]
    del xs[0:]
    return xs