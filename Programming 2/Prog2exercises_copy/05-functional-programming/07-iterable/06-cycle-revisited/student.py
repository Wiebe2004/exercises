def cycle(xs):

    xs = list(xs)
    i = 0
    while True:
        yield xs[i]
        i = (i + 1) % len(xs)