# Write your code here
def add_indices(xs):
    return [(counter,line) for counter, line in enumerate(xs, start=0)]