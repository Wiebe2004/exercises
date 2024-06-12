def take_while(xs, condition):
    ys = []
    for i, x in enumerate(xs):
        if condition(x):
            ys.append(x)
        else:
            return ys, xs[i:]
    return ys, []

# enumerates through the list, if it fits the condition, 
# it removes the iteration by either slicing or empty list.