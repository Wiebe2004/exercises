def indices_of(xs, condition):
    return [i for i, x in enumerate(xs) if condition(x)]