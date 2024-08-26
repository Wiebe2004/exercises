def indices_of(xs, condition):
    result = []
    for x in range(len(xs)):
        if condition(xs[x]):
            result.append(x)
    return result


def is_odd(x):
    return x % 2 != 0

print(indices_of([1, 2, 3, 4, 5, 6, 7, 8], is_odd))