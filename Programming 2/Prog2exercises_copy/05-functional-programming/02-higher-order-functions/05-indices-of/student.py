def indices_of(xs, condition):
    odd = []
    for i, x in enumerate(xs):
        if condition(x):
            odd.append(i)
    return odd