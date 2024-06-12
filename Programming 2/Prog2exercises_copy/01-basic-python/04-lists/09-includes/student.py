# Write your code here
def includes(xs, ys):
    if not ys: # check empty list
        return True
    for x in range(len(xs)):
        for y in range(len(ys)):
            if ys[y] == xs[x]:
                return True
    return False