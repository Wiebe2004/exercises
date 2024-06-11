# Write your code here
def includes_faulty(xs, ys):
    for x in range(len(xs)):
        if xs[x] not in ys:
            return False
    return True


def includes(xs, ys):
    for x in xs:
        if x not in ys:
            return False
    return True

print(includes([1, 2, 3], [1, 2,4]))